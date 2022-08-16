---
description: Birds-Eye View of the Text Recognizer Architecture
---
# Lab Overview

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hltjXcaxExY?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published July 25, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/2022-overview"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240> </a>
</div>

## What are these labs for?

In the lab portion of Full Stack Deep Learning 2022,
we will incrementally develop a complete codebase
to train a deep neural network to recognizer characters in hand-written paragraphs
and deploy it inside a simple web application.

These labs act as an opportunity to work through the nitty-gritty details that come up
when implementing some of the recommendations given in the lectures in a concrete system.
It's also a chance for you to gain familiarity with the tools we recommend.

This lab reviews the overall architecture of the system.

## Architecture of the Text Recognizer

Software architectures are inherently about trade-offs:
decisions that make for better scaling might make for worse security or
tools that encourage faster iteration might reduce transparency.

We design our architecture with _agility_ and _simplicity_ as the prime directives.
We choose simplicity in order to empower individuals to understand the "full stack" of the application,
from GPUs crunching tensors in model development up to serverless cloud functions acting on requests in production.
And we choose _agility_ so that individual is able to quickly iterate on the application,
especially in response to user feedback.

### Architecture Diagram

We put together a handy architecture diagram summarizing the application here:

<div align="center">
  <iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVOrOHcOg=/?moveToViewport=-756,-1203,2371,1920&embedAutoplay=true" frameBorder="0" scrolling="no" allowFullScreen></iframe>
</div>

For a guided tour of this architecture, watch the video at the top of the page or
click the badge below to open an interactive Jupyter notebook on Google Colab:

<div align="center">
  <a href="https://fsdl.me/2022-overview"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240> </a>
</div>
