from typing import List, Tuple
from contextlib import contextmanager
from queue import Queue
from threading import Thread
import os

import torch
from torch import nn
import torch.multiprocessing as mp
import torch.distributed as dist

from utils import load_param

from minitron.linear import ColumnParallelLinear, RowParallelLinear


def wait_and_execute(in_queue: Queue, out_queue: Queue):
    """Wait for a task and execute it."""
    while True:
        task = in_queue.get()

        try:
            output = task()
        except Exception:
            raise Exception("task failed")

        out_queue.put(output)


@contextmanager
def spawn_worker():
    in_queue = Queue()
    out_queue = Queue()

    thread = Thread(target=wait_and_execute, args=(in_queue, out_queue), daemon=True)
    thread.start()

    yield (in_queue, out_queue)


def clock_cycles(n_microbatches, n_partritions):
    n_clock_cycles = n_partritions + n_microbatches - 1
    for clock_idx in range(n_clock_cycles):
        start_partrition = max(clock_idx+1-n_microbatches, 0)
        end_partrition = min(clock_idx+1, n_partritions)

        tasks = []
        for partrition_idx in range(start_partrition, end_partrition):
            microbatch_idx = clock_idx-partrition_idx
            task = (microbatch_idx, partrition_idx)
            tasks.append(task)

        yield tasks


class Pipeline:
    """A base class for pipeline."""

    def __init__(
        self,
        batches: List[torch.Tensor],
        partitions: List[nn.Sequential],
    ):
        self.batches = batches
        self.partitions = partitions

    def fit(self):
        batches = self.batches
        partitions = self.partitions

        n_batches = len(batches)
        n_partitions = len(partitions)

        with spawn_worker() as (in_queue, out_queue):
            for schedule in clock_cycles(n_batches, n_partitions):
                self._compute(schedule, in_queue, out_queue)

    def _compute(self, schedule: List[Tuple[int, int]], in_queue: Queue, out_queue: Queue):
        """Compute the partitions."""
        for microbatch_idx, partition_idx in schedule:
            batch = self.batches[microbatch_idx]
            partrition = self.partitions[partition_idx]

            def compute(batch, partrition):
                def wrapper():
                    return partrition(batch)
                return wrapper

            in_queue.put(compute(batch, partrition))

        for microbatch_idx, partition_idx in schedule:
            output = out_queue.get()
            # put the output back to input list
            self.batches[microbatch_idx] = output


def test_pipeline():
    N_MICROBATCHES = 3
    N_PARTITIONS = 2

    forward_timeline = []
    backward_timeline = []

    def backward_hook(module, grad_input, grad_output):
        backward_timeline.append((module.microbatch_idx - 1, module.partition_idx))
        module.microbatch_idx -= 1

    class AddOne(nn.Module):
        def __init__(self, partition_idx, is_logging):
            super().__init__()
            self.microbatch_idx = 0
            self.partition_idx = partition_idx
            self.is_logging = is_logging
            self.net = nn.Linear(1, 1)
            self.register_backward_hook(backward_hook)

        def forward(self, x):
            if self.is_logging:
                forward_timeline.append((self.microbatch_idx, self.partition_idx))
                self.microbatch_idx += 1

            return self.net(x)

    def create_non_parallel_model(partitions):
        non_parallel_model = nn.Sequential(*[AddOne(partition_idx=x, is_logging=False) for x in range(len(partitions))])
        for non_parallel_layer, original_partition in zip(non_parallel_model, partitions):
            non_parallel_layer.load_state_dict(original_partition[0].state_dict())
        return non_parallel_model

    def create_non_parallel_batch(batch):
        non_parallel_batch = batch.detach().clone()
        non_parallel_batch.grad = None
        return non_parallel_batch

    def loss_func(x):
        return x.mean()

    batch = torch.arange(0, N_MICROBATCHES, dtype=torch.float32, requires_grad=True)
    microbatches = [x.unsqueeze(0) for x in batch.unbind()]
    partitions = [nn.Sequential(AddOne(partition_idx=x, is_logging=True)) for x in range(N_PARTITIONS)]

    non_parallel_model = create_non_parallel_model(partitions)
    non_parallel_batch = create_non_parallel_batch(batch)

    pipeline = Pipeline(microbatches, partitions)

    assert pipeline.batches == microbatches
    assert pipeline.partitions == partitions

    pipeline.fit()

    assert forward_timeline == [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (2, 1)] or [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)]

    outputs = microbatches
    non_parallel_outputs = [non_parallel_model(x.unsqueeze(0)) for x in non_parallel_batch.unbind()]

    for x, y in zip(outputs, non_parallel_outputs):
        assert torch.allclose(x, y)

    for x in outputs:
        loss = loss_func(x)
        loss.backward()

    assert backward_timeline == [(2, 1), (2, 0), (1, 1), (1, 0), (0, 1), (0, 0)] or backward_timeline == [
        (2, 1),
        (2, 0),
        (1, 1),
        (0, 1),
        (1, 0),
        (0, 0),
    ]

    for x in non_parallel_outputs:
        loss = loss_func(x)
        loss.backward()

    assert batch.grad is not None

    for partition in partitions:
        for param in partition.parameters():
            assert param.grad is not None

    for partition_idx in range(N_PARTITIONS):
        for w1, w2 in zip(partitions[partition_idx].parameters(), non_parallel_model[partition_idx].parameters()):
            assert torch.allclose(w1.grad, w2.grad)


def run_pipeline(rank, world_size, input_size, hidden_size, output_size, microbatches, params, outputs):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12359'
    dist.init_process_group(
        "gloo",
        rank=rank,
        world_size=world_size
    )

    partitions = [
        nn.Sequential(ColumnParallelLinear(input_size, hidden_size), nn.ReLU()),
        nn.Sequential(RowParallelLinear(hidden_size, output_size)),
    ]

    # partitions = load_param(rank, world_size, weights, biases, partitions)

    def load_params(rank, world_size, params, partitions):
    for partition in partitions:
        for module_name, module in partition.named_modules():
            if isinstance(module, torch.nn.Linear):
                # Calculate the size of the partition
                weight_size = params[module_name]['weights'].shape[0] // world_size
                bias_size = params[module_name]['biases'].shape[0] // world_size

                # Calculate the start and end indices for the partition
                start_idx = rank * weight_size
                end_idx = start_idx + weight_size

                # Load the weights and biases for this partition
                module.weight.data = params[module_name]['weights'][start_idx:end_idx]
                module.bias.data = params[module_name]['biases'][start_idx:end_idx]

    return partitions

    pipeline = Pipeline(microbatches, partitions)

    assert pipeline.batches == microbatches
    assert pipeline.partitions == partitions

    pipeline.fit()

    parallel_outputs = microbatches

    for x, y in zip(outputs, parallel_outputs):
        assert torch.allclose(x, y, rtol=0.01)

    for x in parallel_outputs:
        x.sum().backward()

    for layer_idx, grad_idx in [[0, 0], [1, 1]]:
        if layer_idx == 0:
            partition_size = weight_grads[grad_idx].shape[0] // world_size
            grad_chunks = torch.split(weight_grads[grad_idx], partition_size, dim=0)
            bias_chunks = torch.split(bias_grads[grad_idx], partition_size, dim=0)
        elif layer_idx == 1:
            partition_size = weight_grads[grad_idx].shape[1] // world_size
            grad_chunks = torch.split(weight_grads[grad_idx], partition_size, dim=1)

        assert torch.allclose(partitions[layer_idx][0].weight.grad, grad_chunks[rank])
        if layer_idx == 0:
            assert torch.allclose(partitions[layer_idx][0].bias.grad, bias_chunks[rank])
        else:
            assert torch.allclose(partitions[layer_idx][0].bias.grad, bias_grads[grad_idx])


def test_tensor_parallelism_with_pipeline():
    world_size = 4
    batch_size, input_size, output_size = 10, 16, 12
    hidden_size = output_size * world_size

    batch = torch.randn(batch_size, input_size, dtype=torch.float32)
    microbatches = [x.unsqueeze(0) for x in batch.unbind(dim=0)]

    # model = nn.Sequential(
    #     nn.Linear(input_size, hidden_size),
    #     nn.ReLU(),
    #     nn.Linear(hidden_size, output_size),
    # )
    class ToyMLP(nn.Module):
        def __init__(self, input_size, hidden_size, output_size) -> None:
            super().__init__()
            self.dense_h_to_4h = nn.Linear(input_size, hidden_size)
            self.relu = nn.ReLU()
            self.dense_4h_to_h = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            return self.dense_4h_to_h(self.relu(self.dense_h_to_4h(x)))

    model = ToyMLP(input_size, hidden_size, output_size)

    outputs = model(batch)
    outputs.sum().backward()

    # def extract_params(model):
    #     weights = [model.dense_h_to_4h.weight.data.detach(), model.dense_4h_to_h.weight.data.detach()]
    #     biases = [model.dense_h_to_4h.bias.data.detach(), model.dense_4h_to_h.bias.data.detach()]
    #     return weights, biases

    # def extract_grads(model):
    #     weight_grads = [
    #         model.dense_h_to_4h.weight.grad.detach().requires_grad_(False),
    #         model.dense_4h_to_h.weight.grad.detach().requires_grad_(False)
    #     ]
    #     bias_grads = [
    #         model.dense_h_to_4h.bias.grad.detach().requires_grad_(False),
    #         model.dense_4h_to_h.bias.grad.detach().requires_grad_(False)

    #     ]
    #     return weight_grads, bias_grads

    def extract_params_and_grads(model):
        params_and_grads_dict = {}

        for module_name, module in model.named_modules():
            if isinstance(module, torch.nn.Linear):
                params_and_grads_dict[module_name] = {
                    'weights': module.weight.data.detach(),
                    'biases': module.bias.data.detach(),
                    'weight_grads': module.weight.grad.detach().requires_grad_(False) if module.weight.grad is not None else None,
                    'bias_grads': module.bias.grad.detach().requires_grad_(False) if module.bias.grad is not None else None
                }

        return params_and_grads_dict

    params = extract_params_and_grads(model)

    mp.spawn(
        run_pipeline,
        nprocs=world_size,
        args=(
            world_size,
            input_size, hidden_size, output_size,
            microbatches, params,
            outputs.detach().requires_grad_(False),
            # weight_grads, bias_grads,
        )
    )


if __name__ == "__main__":
    # test_pipeline()
    test_tensor_parallelism_with_pipeline()
