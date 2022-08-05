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

**We welcome your help in adding more cloud GPU providers and keeping the pricing info current!**

Please make a pull request to this repo, editing [this file](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/index.md) and/or [cloud-gpus.csv](https://github.com/full-stack-deep-learning/website/blob/main/docs/cloud-gpus/cloud-gpus.csv).

<div id="cloud-gpus-table"></div>

### Notes

- GCP does not have GPU "instances" in the same way that AWS and Azure do. Instead, any suitable machine can be connected to a configuration of GPUs. We have selected machines that are roughly equivalent to AWS options.
- Regions were set to be the west or central parts of the United States. GPU availability depends on the region.
- AWS has more A10G instances available with different numbers of vCPUs and amounts of RAM.
- Raw data can be found in a [Google sheet](https://docs.google.com/spreadsheets/d/1nyMIbl0FzJfKpx6BjnDrX2ABIbgaSXQHBwBL5Us0KRw/edit?usp=sharing).

## GPUs

Below are the TFLOPs of the different GPUs available from cloud providers.

| Model | FP32 | Mixed-precision | FP16 | Source         |
| ----- | ---- | --------------- | ---- | -------------- |
| A100  | 19.5 | 156             | 312  | [Datasheet][1] |
| A10G  | 35   | 35              | 70   | [Datasheet][2] |
| A6000 | 38   | ?               | ?    | [Datasheet][3] |
| V100  | 14   | 112             | 28   | [Datasheet][4] |
| T4    | 8.1  | 65              | ?    | [Datasheet][5] |
| P4    | 5.5  | N/A             | N/A  | [Datasheet][6] |
| P100  | 9.3  | N/A             | 18.7 | [Datasheet][7] |
| K80   | 8.73 | N/A             | N/A  | [Datasheet][8] |

[1]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf
[2]: https://d1.awsstatic.com/product-marketing/ec2/NVIDIA_AWS_A10G_DataSheet_FINAL_02_17_2022.pdf
[3]: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/proviz-print-nvidia-rtx-a6000-datasheet-us-nvidia-1454980-r9-web%20(1).pdf
[4]: https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf
[5]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-t4/t4-tensor-core-datasheet-951643.pdf
[6]: https://images.nvidia.com/content/pdf/tesla/184457-Tesla-P4-Datasheet-NV-Final-Letter-Web.pdf
[7]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-p100/pdf/nvidia-tesla-p100-PCIe-datasheet.pdf
[8]: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/tesla-product-literature/Tesla-K80-BoardSpec-07317-001-v05.pdf

<figure markdown>
  ![Benchmark of different GPUs on a single ImageNet epoch, by AIME](aime_benchmarks.jpg)
  <figcaption markdown>Benchmark of different GPUs on a single ImageNet epoch, by [AIME](https://www.aime.info/en/blog/deep-learning-gpu-benchmarks-2021/)</figcaption>
</figure>

<figure markdown>
  ![Benchmark of different GPUs on a mix of tasks, by Lambda Labs](lambda_benchmarks.png)
  <figcaption markdown>Benchmark of different GPUs on a mix of tasks, by [Lambda Labs](https://lambdalabs.com/gpu-benchmarks)</figcaption>
</figure>