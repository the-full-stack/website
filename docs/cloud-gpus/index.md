---
template: cloud-gpus.html
hide:
    - toc
    - navigation
description: Detailed comparison table of all cloud GPU providers.
---

<h1 class="h1-with-author">Cloud GPUs</h1>

<div class="author" markdown>
By [Sergey Karayev](https://twitter.com/sergeykarayev). Updated August 5, 2022.
</div>

## Cloud Comparison

We have assembled cloud GPU vendor pricing all in one table, sortable and filterable to your liking!

**We welcome your help in adding more cloud GPU providers and keeping the pricing info current.**

Please [file an issue](https://github.com/full-stack-deep-learning/website/issues/new?assignees=sergeyk&labels=cloud-gpu&template=gpu-cloud-pricing-update.md&title=update+GPU+Cloud+Pricing) or make a pull request to [this repo](https://github.com/full-stack-deep-learning/website/), editing [this file](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/index.md) to update the text on this page and/or [cloud-gpus.csv](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/cloud-gpus.csv) to update the data.

<center>*All prices are in $/hr.*</center>

<div id="cloud-gpus-table"></div>

### Notes

- GCP does not have GPU "instances" in the same way that AWS and Azure do. Instead, any suitable machine can be connected to a configuration of GPUs. We have selected machines that are roughly equivalent to AWS options.
- Regions were set to be the west or central parts of the United States. GPU availability depends on the region.
- Raw data can be found in a [Google sheet](https://docs.google.com/spreadsheets/d/1nyMIbl0FzJfKpx6BjnDrX2ABIbgaSXQHBwBL5Us0KRw/edit?usp=sharing).

## GPUs

Below are the TFLOPs of the different GPUs available from cloud providers.

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

<figure markdown>
  ![Benchmark of different GPUs on a single ImageNet epoch, by AIME](aime_benchmarks.jpg)
  <figcaption markdown>Benchmark of different GPUs on a single ImageNet epoch, by [AIME](https://www.aime.info/en/blog/deep-learning-gpu-benchmarks-2021/)</figcaption>
</figure>

<figure markdown>
  ![Benchmark of different GPUs on a mix of tasks, by Lambda Labs](lambda_benchmarks.png)
  <figcaption markdown>Benchmark of different GPUs on a mix of tasks, by [Lambda Labs](https://lambdalabs.com/gpu-benchmarks)</figcaption>
</figure>
