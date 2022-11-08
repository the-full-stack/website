---
description: Learn how to run and manage deep learning experiments.
---
# Lab 4: Experiment Management

<div align="center">
<iframe width="720" height="405" src="https://www.youtube.com/embed/NEGDJuINE9E?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published August 17, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/lab04-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

In this lab,
we'll work through
an entire experiment management workflow
for model development,
using a tool called Weights & Biases.

## Outline

- 00:00 Why do we need experiment management?
- 02:24 Tracking experiments with TensorBoard
- 04:16 Experiment management with Weights & Biases
- 06:48 A guided tour of the W&B run interface
- 12:12 Exploratory data analysis with W&B Tables
- 14:00 Project management with W&B
- 16:27 Artifact versioning with W&B
- 18:52 Programmatic API access to W&B
- 20:14 Collaboration tools in W&B
- 25:00 Hyperparameter sweeps in W&B
- 28:15 Overview of exercises

!!! info "Wait, what happened to labs 1 through 3?"

    The first three labs review some pre-requisites for the course --
    DNN architectures and the basics of model training.

    You can find them
    [here](https://fullstackdeeplearning.com/course/2022/labs-1-3-cnns-transformers-pytorch-lightning).

    If you're already basically familiar with training neural networks
    in any framework, you really only need to review
    [Lab 02a](https://fsdl.me/2022-lab-02-video),
    on using PyTorch Lightning.
