---
description: Birds-Eye View of the Text Recognizer Architecture
---
# Lab Overview

<div align="center">
<iframe width="720" height="405" src="https://www.youtube-nocookie.com/embed/hltjXcaxExY?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published July 25, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/2022-overview"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240> </a>
</div>

## What are these labs for?

In the lab portion of Full Stack Deep Learning 2022,
we will incrementally develop a complete codebase
to train a deep neural network to recognize characters in hand-written paragraphs
and deploy it inside a simple web application.

These labs act as an opportunity to work through the nitty-gritty details that come up
when implementing some of the recommendations given in the lectures in a concrete system.
It's also a chance for you to gain familiarity with some of the tools we recommend
in the lectures.

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

## Running the labs

### One-click setup on Colab

To make it as easy as possible to run the labs,
we've made them compatible with
[Google Colab](https://colab.research.google.com/github/anthony-agbay/python-resource-guide/blob/master/notebooks/intro-notebooks.ipynb).

Wherever you see an "Open in Colab" badge, like the one below,
just click on it and you'll be dropped into a hosted notebook environment for the lab,
complete with free GPU.
The badge below opens the first main-track lab,
[Lab 4 on experiment management](https://fullstackdeeplearning.com/course/2022/lab-4-experiment-management/).

<div align="center">
  <a href="https://fsdl.me/lab00-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

You can read more
[here](https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2022-labs/tree/main/setup#colab).

### Setup on your own Linux machine

<div align="center">
  <iframe src="https://share.descript.com/embed/QAe9ZpPMkdY" width="720" height="405" frameborder="0" allowfullscreen></iframe>
</div>

If you have a Linux machine with an NVIDIA GPU and drivers,
either locally or in the cloud,
you can also run the labs there.
The video above and text instructions
[here](http://fsdl.me/2022-local-setup)
should be enough to get you going.

!!! info "Don't get stuck on setup!"
    Remember that Google Colab is always there as an option if you run into issues while setting up.

    Rather than getting frustrated with some obnoxious library linking or driver issue that's irrelevant
    to the material you are really trying to learn and getting stuck in an installation quagmire,
    just run the labs on Colab so you can get back to learning about machine learning!

[yt-logo]: https://fsdl.me/yt-logo-badge
[open-in-colab]: https://colab.research.google.com/assets/colab-badge.svg
