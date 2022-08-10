---
description: Birds-Eye View of the Text Recognizer Architecture
hide:
    - toc
---
# Lab Overview

<div align="center">
  <iframe width="720" height="405" src="https://www.youtube.com/embed/hltjXcaxExY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published July 25, 2022.
</div>

As part of Full Stack Deep Learning 2022,
we will incrementally develop a complete codebase
to create a deep neural network that understands the content of hand-written paragraphs
and deploy it as a simple text recognition application.

Software architectures are inherently about trade-offs:
decisions that make for better scaling trades might make for worse security or
tools that encourage faster iteration reduce transparency.

We design our architecture with _agility_ and _simplicity_ as the prime directives.
We want to empower individuals to understand the "full stack" of the application,
from GPUs in model development up to serverless cloud functions acting on requests in production.
And we want that individual to be able to quickly iterate on the application,
especially in response to user feedback.

## Architecture Diagram

We put together a handy architecture diagram summarizing the application here:

<div align="center">
  <iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVOrOHcOg=/?moveToViewport=-756,-1203,2371,1920&embedAutoplay=true" frameBorder="0" scrolling="no" allowFullScreen></iframe>
</div>

For a guided tour of this architecture, watch the video or
click the badge below to open an interactive Jupyter notebook on Google Colab:

<div align="center">
  <a href="https://fsdl.me/2022-overview"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240> </a>
</div>
