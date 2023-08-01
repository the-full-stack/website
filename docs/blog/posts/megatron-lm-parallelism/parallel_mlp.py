import os
from copy import deepcopy

import torch
from torch import nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter
from torch.multiprocessing import Process
import torch.distributed as dist


class Broadcast(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        return input

    @staticmethod
    def backward(ctx, grad_output):
        torch.distributed.all_reduce(
            grad_output,
            op=torch.distributed.ReduceOp.SUM
        )
        return grad_output


class Gather(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        world_size = torch.distributed.get_world_size()
        inputs = [torch.empty_like(input) for _ in range(world_size)]
        dist.all_gather(inputs, input)
        inputs = torch.cat(inputs, dim=-1)
        return inputs

    @staticmethod
    def backward(ctx, grad_output):
        rank = torch.distributed.get_rank()
        world_size = torch.distributed.get_world_size()
        dim_size = grad_output.shape[-1]
        dim_size_per_partition = dim_size // world_size
        grad_chunks = torch.split(grad_output, dim_size_per_partition, dim=-1)
        return grad_chunks[rank]


class Scatter(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        rank = torch.distributed.get_rank()
        world_size = torch.distributed.get_world_size()
        last_dim_size = input.shape[-1]
        n_chunks = last_dim_size // world_size
        input_chunks = torch.split(input, n_chunks, dim=-1)
        return input_chunks[rank]

    @staticmethod
    def backward(ctx, grad_output):
        world_size = torch.distributed.get_world_size()
        grad_outputs = [torch.empty_like(grad_output) for _ in range(world_size)]
        dist.all_gather(grad_outputs, grad_output)
        grad_outputs = torch.cat(grad_outputs, dim=-1)
        return grad_outputs


class Reduce(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        world_size = torch.distributed.get_world_size()
        if world_size == 1:
            return input
        torch.distributed.all_reduce(input)
        return input

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output


class ColumnParallelLinear(torch.nn.Module):
    def __init__(self, input_size, output_size, world_size):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.output_size_per_partition = output_size // world_size

        self.weight = Parameter(torch.empty(
            self.output_size_per_partition,
            self.input_size,
        ))
        self.bias = Parameter(torch.empty(
            self.output_size_per_partition,
        ))

    def forward(self, input):
        input_parallel = Broadcast.apply(input)
        output_parallel = F.linear(input_parallel, self.weight, self.bias)
        outputs = Gather.apply(output_parallel)
        return outputs


class RowParallelLinear(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        world_size = torch.distributed.get_world_size()
        input_size_per_partition = input_size // world_size

        self.weight = nn.Parameter(torch.randn(
            output_size,
            input_size_per_partition
        ))
        self.bias = nn.Parameter(torch.randn(output_size))

    def forward(self, input):
        input_parallel = Scatter.apply(input)
        output_parallel = F.linear(input_parallel, self.weight)
        outputs = Reduce.apply(output_parallel)
        return outputs + self.bias


def run_parallel(
    rank, world_size,
    input_size, output_size,
    inputs, weights, biases, outputs,
    weight_grads, bias_grads
):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12359'
    torch.distributed.init_process_group(
        "gloo",
        rank=rank,
        world_size=world_size
    )

    torch.use_deterministic_algorithms(True)
    torch.random.manual_seed(rank)

    hidden_size = output_size * 4
    model = nn.Sequential(
        ColumnParallelLinear(input_size, hidden_size, world_size),
        nn.ReLU(),
        RowParallelLinear(hidden_size, output_size),
    )

    def load_data(model, layer_idx, idx):
        if layer_idx == 0:
            partition_size = weights[idx].shape[0] // world_size
        elif layer_idx == 2:
            partition_size = weights[idx].shape[1] // world_size

        partition_start, partition_end = rank * partition_size, (rank + 1) * partition_size

        if layer_idx == 0:
            model[layer_idx].weight.data = weights[idx][partition_start: partition_end].detach().requires_grad_(True)
            model[layer_idx].bias.data = biases[idx][partition_start:partition_end].detach().requires_grad_(True)
        elif layer_idx == 2:
            model[layer_idx].weight.data = weights[idx][:, partition_start:partition_end].detach().requires_grad_(True)
            model[layer_idx].bias.data = biases[idx][:partition_end].detach().requires_grad_(True)
        return model

    model = load_data(model, layer_idx=0, idx=0)
    model = load_data(model, layer_idx=2, idx=1)

    outputs_parallel = model(inputs)
    outputs_parallel.sum().backward()

    print(f"rank={rank}, parallel_output.shape: {outputs_parallel.shape}, non_parallel_output.shape: {outputs.shape}\n")
    print(f"rank={rank}, is the forward correct? {torch.allclose(outputs_parallel, outputs, rtol=0.01)}\n")


    for layer_idx, grad_idx in [[0, 0], [2, 1]]:
        if layer_idx == 0:
            partition_size = weight_grads[grad_idx].shape[0] // world_size
            grad_chunks = torch.split(weight_grads[grad_idx], partition_size, dim=0)
        elif layer_idx == 2:
            partition_size = weight_grads[grad_idx].shape[1] // world_size
            grad_chunks = torch.split(weight_grads[grad_idx], partition_size, dim=1)

        print(f"rank={rank}, is the gradient of the weight correct? {torch.allclose(model[layer_idx].weight.grad, grad_chunks[rank], rtol=0.01)}\n")

    # print(f"rank={rank}, is the gradient of the bias correct? {torch.allclose(model[0].bias.grad, bias_grads[0][rank], rtol=0.01)}\n")

    torch.distributed.destroy_process_group()


if __name__ == "__main__":
    processes = []
    world_size = 4
    batch_size, input_size, output_size = 10, 16, 12
    hidden_size = output_size * 4

    inputs = torch.randn(2, input_size, requires_grad=False)

    model = nn.Sequential(
        nn.Linear(input_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, output_size),
    )
    outputs = model(inputs)
    outputs.sum().backward()

    weights = [
        model[0].weight.data.detach(),
        model[2].weight.data.detach(),
    ]
    biases = [model[0].bias.data.detach(), model[2].bias.data.detach()]
    weight_grads = [
        model[0].weight.grad.detach().requires_grad_(False),
        model[2].weight.grad.detach().requires_grad_(False)
    ]
    bias_grads = [
        model[0].bias.grad.detach().requires_grad_(False),
        model[2].bias.grad.detach().requires_grad_(False)

    ]

    for rank in range(world_size):
        p = Process(target=run_parallel, args=(
            rank, world_size,
            input_size, output_size,
            # Because PyTorch does not support sending tensors
            # that require gradients through inter-process communication
            # we need to detach them from the computational graph
            inputs, deepcopy(weights), deepcopy(biases), outputs.detach(),
            deepcopy(weight_grads), deepcopy(bias_grads)
        ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
