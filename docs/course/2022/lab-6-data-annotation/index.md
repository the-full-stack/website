---
description: Learn how to annotate data with Label Studio
---
# Lab 6: Data Annotation

<div align="center">
<iframe width="720" height="405" src="https://www.youtube.com/embed/zoS5Fx2Ou1Y?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published August 31, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/lab06-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

In this lab,
we'll see how raw data becomes useful data
via data annotation
and how structured data stored on disk
becomes neural network-ready
with preprocessing and PyTorch `Dataset`s.

We'll also spin up a data annotation server using
[Label Studio](https://labelstud.io).

## Outline

- 00:00 Overview
- 00:36 Loading annotated data and synthesizing data
- 02:39 Setting up a data annotation server with Label Studio
- 06:54 Uploading data to Label Studio
- 09:15 Building and using an annotation interface in Label Studio
- 13:17 Exercises
