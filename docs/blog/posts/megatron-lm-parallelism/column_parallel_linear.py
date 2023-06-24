import os

import torch
import torch.nn.functional as F
from torch.nn.parameter import Parameter
from torch.multiprocessing import Process
import torch.distributed as dist


class f(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input, weight, bias):
        return F.linear(input, weight, bias)

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
    def __init__(self, input_size: int, output_size: int, world_size: int):
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
        output_parallel = f.apply(input, self.weight, self.bias)
        outputs = g.apply(output_parallel)
        return outputs


def compute_non_parallel_output(model, input):
    world_size = torch.distributed.get_world_size()

    weights = [torch.empty_like(model.weight) for _ in range(world_size)]
    torch.distributed.all_gather(weights, model.weight)
    weights = torch.cat(weights, dim=0).contiguous()
    weights.requires_grad = True

    biases = [torch.empty_like(model.bias) for _ in range(world_size)]
    torch.distributed.all_gather(biases, model.bias)
    biases = torch.cat(biases, dim=0).contiguous()
    biases.requires_grad = True

    non_parallel_output = F.linear(input, weights, biases)

    return non_parallel_output


def run_parallel(rank, world_size, input_size, output_size, input):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12359'
    torch.distributed.init_process_group(
        "gloo",
        rank=rank,
        world_size=world_size
    )

    model = ColumnParallelLinear(input_size, output_size, world_size)
    parallel_output = model(input)
    non_parallel_output = compute_non_parallel_output(model, input)

    print(f"rank: {rank}, output.shape: {parallel_output.shape}, non_parallel_output.shape: {non_parallel_output.shape}")
    print(f"Is output correct? {torch.allclose(parallel_output, non_parallel_output, rtol=1e-3)}")
    torch.distributed.destroy_process_group()


if __name__ == "__main__":
    world_size = 4
    input_size = 16
    output_size = 12
    input = torch.randn(input_size, requires_grad=False)

    processes = []
    for rank in range(world_size):
        p = Process(target=run_parallel, args=(rank, world_size, input_size, output_size, input))
        p.start()

    for p in processes:
        p.join()
