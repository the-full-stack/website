from typing import List, Tuple
from contextlib import contextmanager
from queue import Queue
from threading import Thread
import time
import os
from copy import deepcopy
import time

import torch
from torch import nn
import torch.multiprocessing as mp

from layers import ColumnParallelLinear, RowParallelLinear
from utils import load_param


def wait_and_execute(in_queue: Queue, out_queue: Queue):
    """Wait for a task and execute it."""
    while True:
        # print(f"thread {thread_id} is waiting for a task")
        # time.sleep(1)
        task = in_queue.get()

        try:
            output = task()
            # print(f"thread {thread_id} executed a task")
        except Exception:
            # print(f"thread {thread_id} got error while executing a task")
            out_queue.put(output)
            continue

        out_queue.put(output)
        # print(f"thread {thread_id} put the output of a task")


@contextmanager
def spawn_worker(
    n_workers: int,
):
    in_queues: List[Queue] = []
    out_queues: List[Queue] = []

    in_queue = Queue()
    out_queue = Queue()

    thread = Thread(target=wait_and_execute, args=(in_queue, out_queue), daemon=True)
    thread.start()

    for _ in range(n_workers):
        in_queues.append(in_queue)
        out_queues.append(out_queue)

    yield (in_queues, out_queues)


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
    ) -> None:
        """Initialize the pipeline.

        Args:
            batches (List[Batch]): A list of micro-batches.
            partitions (List[nn.Sequential]): A partitioned model.
            devices (Optional[List[torch.device]], optional): A list of devices. Defaults to None.
            scheduler (BaseScheduler, optional): _description_. Defaults to DetermisticScheduler().
        """
        self.batches = batches
        self.partitions = partitions

    def fit(self):
        batches = self.batches
        partitions = self.partitions

        n_batches = len(batches)
        n_partitions = len(partitions)
        n_workers = len(batches)

        with spawn_worker(n_workers) as (in_queues, out_queues):
            for schedule in clock_cycles(n_batches, n_partitions):
                self._compute(schedule, in_queues, out_queues)

    def _compute(self, schedule: List[Tuple[int, int]], in_queues: List[Queue], out_queues: List[Queue]):
        """Compute the partitions."""
        batches = self.batches
        partitions = self.partitions

        for microbatch_idx, partition_idx in schedule:
            batch = batches[microbatch_idx]
            partrition = partitions[partition_idx]

            def compute(batch, partrition):
                def wrapper():
                    return partrition(batch)
                return wrapper

            if microbatch_idx == 2 and partition_idx == 0:
                print("debug")

            in_queues[partition_idx].put(compute(batch, partrition))
            print(f"microbatch_idx={microbatch_idx}, partition_idx={partition_idx}, putted")

        for microbatch_idx, partition_idx in schedule:
            if microbatch_idx == 2 and partition_idx == 0:
                print("debug")

            print(f"microbatch_idx={microbatch_idx}, partition_idx={partition_idx}, wait to get")
            # time.sleep(1)
            output = out_queues[partition_idx].get()
            print(f"microbatch_idx={microbatch_idx}, partition_idx={partition_idx}, got")

            # put the output back to the batch
            batches[microbatch_idx] = output


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
                # time.sleep(0.5)
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

    # pass

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


def run_pipeline(rank, world_size, input_size, hidden_size, output_size, microbatches, weights, biases, outputs, weight_grads, bias_grads):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12359'
    torch.distributed.init_process_group(
        "gloo",
        rank=rank,
        world_size=world_size
    )

    partitions = [
        nn.Sequential(ColumnParallelLinear(input_size, hidden_size), nn.ReLU()),
        nn.Sequential(RowParallelLinear(hidden_size, output_size)),
    ]

    partitions = load_param(rank, world_size, weights, biases, partitions)
    pipeline = Pipeline(microbatches, partitions)

    assert pipeline.batches == microbatches
    assert pipeline.partitions == partitions

    pipeline.fit()

    parallel_outputs = microbatches
    print(f"rank={rank}, outputs.shape: {len(parallel_outputs)}\n")
    print(parallel_outputs[0].shape)

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

        print(f"rank={rank}, is the gradient of the weight correct? {torch.allclose(partitions[layer_idx][0].weight.grad, grad_chunks[rank])}\n")
        if layer_idx == 0:
            print(f"rank={rank}, is the gradient of the bias correct? {torch.allclose(partitions[layer_idx][0].bias.grad, bias_chunks[rank])}\n")
        else:
            print(f"rank={rank}, is the gradient of the bias correct? {torch.allclose(partitions[layer_idx][0].bias.grad, bias_grads[grad_idx])}\n")


def test_tensor_parallelism_with_pipeline():
    world_size = 4
    batch_size, input_size, output_size = 10, 16, 12
    hidden_size = output_size * world_size

    batch = torch.randn(batch_size, input_size, dtype=torch.float32)
    microbatches = [x.unsqueeze(0) for x in batch.unbind(dim=0)]

    model = nn.Sequential(
        nn.Linear(input_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, output_size),
    )
    outputs = model(batch)
    outputs.sum().backward()

    def extract_params(model):
        weights = [model[0].weight.data.detach(), model[2].weight.data.detach()]
        biases = [model[0].bias.data.detach(), model[2].bias.data.detach()]
        return weights, biases

    def extract_grads(model):
        weight_grads = [
            model[0].weight.grad.detach().requires_grad_(False),
            model[2].weight.grad.detach().requires_grad_(False)
        ]
        bias_grads = [
            model[0].bias.grad.detach().requires_grad_(False),
            model[2].bias.grad.detach().requires_grad_(False)

        ]
        return weight_grads, bias_grads

    weights, biases = extract_params(model)
    weight_grads, bias_grads = extract_grads(model)

    mp.spawn(
        run_pipeline,
        nprocs=world_size,
        args=(
            world_size,
            input_size, hidden_size, output_size,
            microbatches, deepcopy(weights), deepcopy(biases),
            outputs.detach().requires_grad_(False),
            deepcopy(weight_grads), deepcopy(bias_grads),
        )
    )


if __name__ == "__main__":
    # test_pipeline()
    test_tensor_parallelism_with_pipeline()
