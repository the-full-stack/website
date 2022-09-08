---
description: Learn how to spin up an ML-powered application
---
# Lab 7: Web Deployment

<div align="center">
<iframe width="720" height="405" src="https://www.youtube.com/embed/2j6rG-4zS6w?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published September 7, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/lab07-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

In this lab,
we'll take the leap
from ML model
to ML-powered application
by packaging our text recognizer
into a portable TorchSript binary,
wrapping that binary up into a serverless cloud function,
and building a simple UI in Python with gradio.

## Outline

- 00:00 Overview
- 01:06 Compiling the model to TorchScript
- 06:00 Why not deploy on GPUs?
- 08:58 Building a GUI with gradio
- 15:34 Spinning up a model service
- 21:11 Creating a public URL with ngrok
- 24:52 Writing a Dockerfile for our server
- 30:06 Recap
