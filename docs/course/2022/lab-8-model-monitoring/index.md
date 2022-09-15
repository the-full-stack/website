---
description: Learn how to monitor and debug an ML-powered application
---
# Lab 8: Model Monitoring

<div align="center">
<iframe width="720" height="405" src="https://www.youtube.com/embed/-mKzxSC0r7w?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl). Published September 14, 2022.
</div>

<div align="center">
  <a href="https://fsdl.me/lab08-colab"> <img src=https://colab.research.google.com/assets/colab-badge.svg width=240></a>
</div>

In this lab,
we'll add flagging to our ML-powered application
so that users can give us feedback.

Then, we'll explore some data logged based on feedback from
actual users of the
[FSDL Text Recognizer](https://fsdl-text-recognizer.ngrok.io)
to the model monitoring and continual learning platform
[Gantry](https://gantry.io).

## Outline

- 00:00 Basic user feedback with gradio
- 04:51 Logging feedback to Gantry
- 08:34 Checking for model toxicity with Gantry projections
- 14:23 Detecting model bugs in the Gantry UI with distributions and filters
- 19:01 Discovering surprising user data in the Gantry UI
- 29:53 Outro
