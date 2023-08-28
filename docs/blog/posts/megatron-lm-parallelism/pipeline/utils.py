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
