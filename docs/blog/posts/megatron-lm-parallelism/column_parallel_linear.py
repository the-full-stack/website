import os

import torch
import torch.nn.functional as F
from torch.nn.parameter import Parameter
from torch.multiprocessing import Process
import torch.distributed as dist


class f(torch.autograd.Function):
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


class g(torch.autograd.Function):
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
        input_parallel = f.apply(input)
        output_parallel = F.linear(input_parallel, self.weight, self.bias)
        outputs = g.apply(output_parallel)
        return outputs


def run_parallel(
    rank, world_size,
    input_size, output_size,
    input, weight, bias, non_parallel_output,
    weight_grad, bias_grad
):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12359'
    torch.distributed.init_process_group(
        "gloo",
        rank=rank,
        world_size=world_size
    )

    model = ColumnParallelLinear(input_size, output_size, world_size)

    # Partition the weights and biases and assign to the model
    weight_partition_size = weight.shape[0] // world_size
    bias_partition_size = bias.shape[0] // world_size

    model.weight.data = weight[rank*weight_partition_size:(rank+1)*weight_partition_size].detach().requires_grad_(True)
    model.bias.data = bias[rank*bias_partition_size:(rank+1)*bias_partition_size].detach().requires_grad_(True)

    parallel_output = model(input.detach().requires_grad_(False))
    parallel_output.sum(dim=-1).backward()

    print(f"rank={rank}, parallel_output.shape: {parallel_output.shape}, non_parallel_output.shape: {non_parallel_output.shape}")
    print(f"rank={rank}, is the forward correct? {torch.allclose(parallel_output, non_parallel_output, rtol=1e-3)}")
    print(f"rank={rank}, is the gradient of the weight correct? {torch.allclose(model.weight.grad, weight_grad[rank], rtol=1e-3)}")
    print(f"rank={rank}, is the gradient of the bias correct? {torch.allclose(model.bias.grad, bias_grad[rank], rtol=1e-3)}")

    torch.distributed.destroy_process_group()


if __name__ == "__main__":
    world_size = 4
    input_size = 16
    output_size = 12

    torch.random.manual_seed(69)

    input = torch.randn(input_size, requires_grad=False)
    weight = torch.randn(output_size, input_size, requires_grad=True)
    bias = torch.randn(output_size, requires_grad=True)

    non_parallel_output = F.linear(input, weight, bias)
    non_parallel_output.sum(dim=-1).backward()

    # because we detach the weight and bias from the computational graph
    # so have to make a copy of the gradients
    weight_grad = weight.grad.clone()
    bias_grad = bias.grad.clone()

    processes = []
    for rank in range(world_size):
        p = Process(target=run_parallel, args=(
            rank, world_size,
            input_size, output_size,
            # because pytorch does not support sending tensors that
            # require gradient through inter-process communication
            # so we gotta detach them from the computational graph
            input, weight.detach(), bias.detach(), non_parallel_output.detach(),
            weight_grad, bias_grad
        ))
        p.start()

    for p in processes:
        p.join()
