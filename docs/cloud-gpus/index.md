---
template: cloud-gpus.html
hide:
    - toc
    - navigation
description: Detailed comparison table of all cloud GPU providers.
---

<div class="author" markdown>
By [Sergey Karayev](https://twitter.com/sergeykarayev) and [Charles Frye](https://twitter.com/charles_irl). Updated January 10, 2023.
</div>

Training and running neural networks often requires hardware acceleration,
and the most popular hardware accelerator is the venerable _graphics processing unit_,
or GPU.

We have assembled cloud GPU vendor pricing all into tables, sortable and filterable to your liking!

We have split the vendor offerings into two classes:

- **GPU Cloud Servers**, which are long-running (but possibly pre-emptible) machines, and
- **Severless GPUs**, which are machines that scale-to-zero in the absence of traffic (like an AWS Lambda or Google Cloud Function)

**We welcome your help in adding more cloud GPU providers and keeping the pricing info current.**

Please [file an issue](https://github.com/full-stack-deep-learning/website/issues/new?assignees=sergeyk&labels=cloud-gpu&template=gpu-cloud-pricing-update.md&title=update+GPU+Cloud+Pricing) or make a pull request to [this repo](https://github.com/full-stack-deep-learning/website/), editing [this file](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/index.md) to update the text on this page or one of the CSV files to update the data: [`cloud-gpus.csv`](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/cloud-gpus.csv) for servers and [`serverless-gpus.csv`](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/serverless-gpus.csv) for serverless options.

<center>*All prices are in $/hr.*</center>

## GPU Cloud Server Comparison

### Notes

- GCP does not have GPU "instances" in the same way that AWS and Azure do. Instead, any suitable machine can be connected to a configuration of GPUs. We have selected machines that are roughly equivalent to AWS options.
- Regions were set to be the west or central parts of the United States. GPU availability depends on the region.
- Raw data can be found in a [csv on GitHub](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/cloud-gpus.csv).

<div id="cloud-gpus-table"></div>

## Serverless GPUs

### Notes

- We use the classic definition of "serverless", courtesy of [the original AWS announcement on serverless computing](https://www.jeremydaly.com/not-so-serverless-neptune/): no server management, flexible scaling, high availability, and no idle capacity. We only include services that fit this criterion in our options below.
- Direct price comparisons are trickier for serverless offerings: cold boot time and autoscaling logic substantially impact cost-of-traffic.
- Serverless GPUs are a newer technology, so there are fewer players, the details change quickly, and you can expect bugs/growing pains. Stay frosty!
- If you know a bit about your anticipated traffic patterns, you can use [this tool](https://paylesstoaws.com/) to compare prices for AWS A100 GPU machines and Banana's serverless equivalent. Note that is is made by the developers of [Banana](https://banana.dev/), so may be biased.
- [Modal](https://modal.com) allows configurable selection of CPU and RAM. [Pricing](https://modal.com/pricing) is, as of January 10 2023, the same for all GPU types and all CPU/RAM configurations. We've shown the default values.
- Raw data can be found in a [csv on GitHub](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/serverless-gpus.csv).

<div id="serverless-gpus-table"></div>

## How do I choose a GPU?

This page is intended to track and make explorable
the current state of pricing and hardware for cloud GPUs.

If you want advice on which machines and cards are best for your use case,
we recommend
[Tim Dettmer's blog post on GPUs for deep learning](https://timdettmers.com/2023/01/16/which-gpu-for-deep-learning).

The whole post is a tutorial and FAQ on GPUS for DNNs,
but if you just want the resulting heuristics for decision-making, see the
["GPU Recommendations" section](https://timdettmers.com/2023/01/16/which-gpu-for-deep-learning/#GPU_Recommendations).

## GPU Raw Performance Numbers and Datasheets

Below are the raw TFLOPs of the different GPUs available from cloud providers.

| Model | Arch   | FP32 | Mixed-precision | FP16 | Source             |
| ----- | ------ | ---- | --------------- | ---- | ------------------ |
| A100  | Ampere | 19.5 | 156             | 312  | [Datasheet][a100]  |
| A10G  | Ampere | 35   | 35              | 70   | [Datasheet][a10g]  |
| A6000 | Ampere | 38   | ?               | ?    | [Datasheet][a6000] |
| V100  | Volta  | 14   | 112             | 28   | [Datasheet][v100]  |
| T4    | Turing | 8.1  | 65              | ?    | [Datasheet][t4]    |
| P4    | Pascal | 5.5  | N/A             | N/A  | [Datasheet][p4]    |
| P100  | Pascal | 9.3  | N/A             | 18.7 | [Datasheet][p100]  |
| K80   | Kepler | 8.73 | N/A             | N/A  | [Datasheet][k80]   |
| A40   | Ampere | 37   | 150             | 150  | [Datasheet][a40]   |

[a100]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf
[a10g]: https://d1.awsstatic.com/product-marketing/ec2/NVIDIA_AWS_A10G_DataSheet_FINAL_02_17_2022.pdf
[a6000]: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/proviz-print-nvidia-rtx-a6000-datasheet-us-nvidia-1454980-r9-web%20(1).pdf
[v100]: https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf
[t4]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet-951643.pdf
[p4]: https://images.nvidia.com/content/pdf/tesla/184457-Tesla-P4-Datasheet-NV-Final-Letter-Web.pdf
[p100]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-p100/pdf/nvidia-tesla-p100-PCIe-datasheet.pdf
[k80]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-product-literature/Tesla-K80-BoardSpec-07317-001-v05.pdf
[a40]: https://images.nvidia.com/content/Solutions/data-center/a40/nvidia-a40-datasheet.pdf

## GPU Performance Benchmarks

Below are some basic benchmarks for GPUs on common deep learning tasks.

<figure markdown>
  ![Benchmark of different GPUs on a single ImageNet epoch, by AIME](aime_benchmarks.jpg)
  <figcaption markdown>Benchmark of different GPUs on a single ImageNet epoch, by [AIME](https://www.aime.info/en/blog/deep-learning-gpu-benchmarks-2021/)</figcaption>
</figure>

<figure markdown>
  ![Benchmark of different GPUs on a mix of tasks, by Lambda Labs](lambda_benchmarks.png)
  <figcaption markdown>Benchmark of different GPUs on a mix of tasks, by [Lambda Labs](https://lambdalabs.com/gpu-benchmarks)</figcaption>
</figure>
