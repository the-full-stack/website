---
description: Learn to test Python code and troubleshoot PyTorch performance
---
# Lab 5: Troubleshooting & Testing

<div align="center">
<iframe width="720" height="405" src="https://www.youtube.com/embed/D65SlCSoS-0?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published August 24, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/lab05-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

In this lab,
we'll check out the basic tools
required to write clean Python code
and
see how to write memorization tests
for training code in PyTorch Lightning.
Then we'll take a deep dive into
the trace of a PyTorch training step
and use it to debug performance issues
in GPU-accelerated code.


## Outline

- 00:00 Overview
- 00:51 Linting: pre-commit, black, flake8
- 05:42 Testing: pytest, doctest, memorization testing
- 11:15 Troubleshooting PyTorch performance
- 16:13 A guided tour of a PyTorch trace
