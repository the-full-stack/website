---
title: "Implement single node pipeline parallelism from scratch"
description: ""
author: "xrsrke"
hide:
  - navigation
tags:
  - 3d-parallelism
  - pipeline-parallelism
  - llms
---

```python
# just some utils, readers, please ignore this
def load_param(rank, world_size, weights, biases, partitions):
    def calculate_start_end_idx(rank, idx):
        if idx == 0: # column parallel
            partition_size = weights[idx].shape[0] // world_size
        elif idx == 1: # row parallel
            partition_size = weights[idx].shape[1] // world_size
        return rank * partition_size, (rank + 1) * partition_size

    def load(model, idx):
        partition_start, partition_end = calculate_start_end_idx(rank, idx)
        if idx == 0:  # column parallel
            model[idx][0].weight.data = weights[idx][partition_start: partition_end].detach().requires_grad_(True)
            model[idx][0].bias.data = biases[idx][partition_start:partition_end].detach().requires_grad_(True)
        elif idx == 1:  # row parallel
            model[idx][0].weight.data = weights[idx][:, partition_start:partition_end].detach().requires_grad_(True)
            model[idx][0].bias.data = biases[idx][:partition_end].detach().requires_grad_(True)
        return model

    partitions = load(partitions, idx=0)
    partitions = load(partitions, idx=1)
    return partitions
```


```python
from typing import List, Tuple
from contextlib import contextmanager
from queue import Queue
from threading import Thread
import os
from copy import deepcopy

import torch
from torch import nn
import torch.multiprocessing as mp
import torch.distributed as dist


from minitron.linear import ColumnParallelLinear, RowParallelLinear
```

In the world of neural networks, size matters. As scaling laws suggests, the larger the model, the better the performance. But when you have a giant model that won't fit in the memory of a single device, things get complicated. This is where pipeline parallelism comes into play, acting as a super-efficient assembly line for large neural network models. In this blog post, we will walk through the concept and build a a toy pipeline parallelism gpipe from scratch.

### ****Naive Pipeline Parallelism vs. GPipe****

Pipeline parallelism is a process that can be distilled down to a few core steps:

- Step 1: **Partition the Model**: Our big model is divided into smaller partitions. Each partition corresponds to a section of the neural network and runs on a separate device.
- Step 2: **Micro-Batching**: We split our training data mini-batch into several smaller micro-batches.
- Step 3: **Forward and Backward Passes**: These partitions and micro-batches go through both the forward and backward computation passes.
- Step 4: **Gradient Averaging**: Once the whole pipeline finishes, we collect the gradients and average them to update the model.

To illustrate, let's imagine we have a big model with 10 layers, like a Transformer model, and we've got five devices to run our model. We want to split this model into five parts, or 'partitions', and each part will run on one device.

There's a catch, though. In a Transformer model, each layer needs the result from the previous layer before it can do its work. It's like a relay race, you can't start running until you've got the baton from the runner before you. So if we split our model into 5 parts, then the second part can't start until the first part is done, the third part can't start until the second part is done, and so on. That means that most of the time, most of our devices are just sitting around doing nothing. That's a bummer!

So what can we do? Here's where GPipe comes in. Instead of feeding a big batch of data to our model all at once, GPipe splits that batch into smaller chunks, which we're gonna call 'micro-batches'. And here's the trick: while one micro-batch is being processed by the second part of our model, the next micro-batch can start being processed by the first part of the model.

This way, there's always something for each part of the model to do. It's like a factory assembly line. As soon as one car is done with one station, it moves to the next station and a new car moves into the first station. This keeps all our devices busy (although they might still have some idle time, like when a worker in the factory is waiting for the next car to arrive).

The GPipe's scheduler orchestrates this process. It works in 'clock cycles', figuring out which partitions should be active and which micro-batch each partition should work on for each clock cycle.

### Cracking the Schedule Algorithm

A "clock cycle" is like a unit of time for our pipeline. Each clock cycle activates a new partition and passes it a micro-batch.

`n_clock_cycles = n_partritions + n_microbatches - 1`

If we have `m` micro-batches and `n` partitions, it'll take `m + n - 1` clock cycles to get everything through the pipeline. Why is that , because it takes `m` clock cycles for all micro-batches to pass through the first partition. Once the last micro-batch enters the first partition, it needs to go through the remaining partitions. Since there are `n` partitions, this requires `n-1` additional clock cycles because the first clock cycle is already counted when the micro-batch enters the first partition.

`end_partrition = min(clock_idx+1, n_partritions)`

In pipeline parallelism, for each clock cycle, a new partrition actives in the pipeline. If we are currently in `clock_idx`, it means that `clock_idx` partritions have already been actived.

The next partritions will be `clock_idx+1`. However, we cannot exceed the total number of partitions (`n_partitions`), so we use the min function to limit the range.

So, what happens in each clock cycle? Good question! In each clock cycle, we determine which partitions are active and what they should be working on. Our scheduler assigns tasks in the form of `(microbatch_index, partition_index)` for each clock cycle. This basically tells each device what chunk of the neural network it should process and with which micro-batch.


```python
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
```


```python
n_microbatches = 5
n_partitions = 3

tasks = clock_cycles(n_microbatches, n_partitions)
```


```python
[task for task in tasks]
```




    [[(0, 0)],
     [(1, 0), (0, 1)],
     [(2, 0), (1, 1), (0, 2)],
     [(3, 0), (2, 1), (1, 2)],
     [(4, 0), (3, 1), (2, 2)],
     [(4, 1), (3, 2)],
     [(4, 2)]]



### Behind the Scenes: Worker Threads

The key players are worker threads. Each pipeline stage or GPU has a dedicated worker thread running in the background. This thread continually checks an input queue for new tasks. When a fresh task appears, the worker grabs it and sends it to the GPU for execution. The key is that workers run independently in threads, executing tasks as they appear in the input queue. The main thread coordinates by assigning new tasks and shuttling outputs between stages. And there you have it, pipeline parallelism.

Just to demonstrate the idea, here we will only provide an implementation in which a single worker thread runs in the background and manages all pipeline stages.


```python
def wait_and_execute(in_queue: Queue, out_queue: Queue):
    """Wait for a task and execute it."""
    while True:
        task = in_queue.get()

        try:
            output = task()
        except Exception:
            raise Exception("task failed")

        out_queue.put(output)

```

Queues follow a first-in, first-out order, which is exactly what we need. Newly added tasks get executed first. Once the GPU finishes a task, the result gets placed in an output queue.


```python
@contextmanager
def spawn_worker():
    in_queue = Queue()
    out_queue = Queue()

    thread = Thread(target=wait_and_execute, args=(in_queue, out_queue), daemon=True)
    thread.start()

    yield (in_queue, out_queue)
```

### A sneak to the real worly, and distributed systems

Let's say you have one node that connects to 8 GPUs. In the early training, only a few GPUs are active based on the schedule from the gpipe scheduler. But as we go to the middle of training, all of these GPUs become active. So how do we dynamically change the number of worker threads during training? Because if the number of workers is less than the number of active GPUs, then idle GPUs have to wait for at least one worker to become available, so it can pick up tasks from the queue and send them to the idle GPUs for execution.

But here is the catch - in distributed systems, things fail all the time. What if worker threads fail? Okay, let's say we build a pool watcher that monitors if worker threads die and spawns new ones. Okay, but what if the pool watcher itself fails? It could cause deadlock, or even fail to execute a task. So how do we automatically retry failed tasks? You know, since in pipeline parallelism the next pipeline stage depends on the previous stage, even a single node failure could cause all other nodes to stop working...

### Issuing Tasks On-the-Fly

Remember that during each clock cycle, the scheduler generates a list of active pipeline stages along with their corresponding microbatch for that cycle. So for every clock cycle, the main thread appends these tasks to the appropriate worker threads' input queues on the go.

The scheduler generates a list of active pipeline stages and their corresponding microbatches for each clock cycle. The main thread is responsible for coordinating the execution across pipeline stages. For each clock cycle, the main thread appends the task for each pipeline stage to the input queue of the appropriate worker thread on-the-fly.


```python
def fit(self):
    batches = self.batches
    partitions = self.partitions

    n_batches = len(batches)
    n_partitions = len(partitions)

    with spawn_worker() as (in_queue, out_queue):
        for schedule in clock_cycles(n_batches, n_partitions):
            self._compute(schedule, in_queue, out_queue)
```

Once a worker thread finishes executing a task, it places the result in its output queue. The main thread retrieves the result from the worker's output queue and enqueues it into the input queue of the worker thread responsible for the next pipeline stage. So it goes like:

- Step 1: Worker finishes task, puts result in output queue
- Step 2: Main thread takes result from output queue
- Step 3: Main thread puts result in next worker's input queue


```python
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
```

In Python, a `queue.get()` will block the CPU execution of the thread until there's at least one item in the queue. It then retrieves the item, removes the item from the queue, and executes the next line. Hence, after a worker thread sends its task to the GPU for execution and waits for the result, the worker thread will put the result into its output. The main thread, which works in parallel with the worker thread, also waits for its output and places it into batches, where we store the output activations.


```python
class Pipeline:
    """A base class for pipeline."""

    def __init__(
        self,
        batches: List[torch.Tensor],
        partitions: List[nn.Sequential],
    ):
        self.batches = batches
        self.partitions = partitions
```


```python
Pipeline.fit = fit
Pipeline._compute = _compute
```

Now, let's test the pipeline. We will split the tests into two parts: one for the execution timeline of the forward pass and backward pass, and one to test running pipeline parallelism with tensor parallelism


```python
def run_pipeline(rank, world_size, input_size, hidden_size, output_size, microbatches, weights, biases, outputs, weight_grads, bias_grads):
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

    partitions = load_param(rank, world_size, weights, biases, partitions)
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

        assert torch.allclose(partitions[layer_idx][0].weight.grad, grad_chunks[rank], rtol=1e-3)
        if layer_idx == 0:
            assert torch.allclose(partitions[layer_idx][0].bias.grad, bias_chunks[rank], rtol=1e-3)
        else:
            assert torch.allclose(partitions[layer_idx][0].bias.grad, bias_grads[grad_idx], rtol=1e-3)


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

    # NOTE: In the third clock cycle, two partitions are active:
    # (1, 0) and (0, 1). We log them based on
    # which one finishes first, so sometimes
    # one partition finishes before the other
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
```


```python
test_pipeline()
```

    /usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py:1344: UserWarning: Using a non-full backward hook when the forward contains multiple autograd Nodes is deprecated and will be removed in future versions. This hook will be missing some grad_input. Please use register_full_backward_hook to get the documented behavior.
      warnings.warn("Using a non-full backward hook when the forward contains multiple autograd Nodes "



```python
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
        weights = [deepcopy(model[0].weight.data.detach()), deepcopy(model[2].weight.data.detach())]
        biases = [deepcopy(model[0].bias.data.detach()), deepcopy(model[2].bias.data.detach())]
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

    processes = []
    for rank in range(world_size):
        p = mp.Process(target=run_pipeline, args=(
            rank, world_size,
            input_size, hidden_size, output_size,
            microbatches, weights, biases,
            outputs.detach().requires_grad_(False),
            weight_grads, bias_grads,
        ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

```


```python
test_tensor_parallelism_with_pipeline()
```
