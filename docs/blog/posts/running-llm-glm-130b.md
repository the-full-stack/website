---
title: "Vanilla GPT-3 quality from an open source model on a single machine: GLM-130B"
description: "Notes from deploying GLM-130B, a large language model from Tsinghua KEG"
author: "Charles Frye"
hide:
  - navigation
tags:
  - model-serving
  - gpus
  - nlp
  - llms
time: "2023-01-12"
---
<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl).
</div>

## tl;dr ##

- [GLM-130B](https://github.com/THUDM/GLM-130B) is a GPT-3-scale and quality language model
that can run on a single 8xA100 node without too much pain.
Kudos to
[Tang Jie and the Tsinghua KEG team](http://keg.cs.tsinghua.edu.cn/jietang/)
for open-sourcing a big,
powerful model _and_ the tricks it takes to make it
run on reasonable hardware.
- Results are roughly what you might expect
after reading
[the paper](https://arxiv.org/abs/2210.02414):
similar to the original GPT-3 175B,
worse than the InstructGPTs.
- I've really been spoiled by OpenAI's latest models:
easier to prompt, higher quality generations.

And

- It's hard to self-serve LLM inferences cheaper than OpenAI will sell them to you.

## Context ##

This is a brief report on a day's worth of hacking with
[GLM-130B](https://github.com/THUDM/GLM-130B).

While I've worked a lot with a variety of DNNs,
including transformers,
and regularly discuss LLM training and inference with experts,
I am not an LLM expert myself.
I encourage you to #DYOR to evaluate this or similar models.

I was looking for a model that was able to do freeform generation
of natural language while still understanding source code both
syntactically and semantically.

Also, I was just doing this for the experience!
Running an LLM is its own kind of workload
that's a different beast even
from training DNNs on multi-GPU machines.

## Why run an LLM on a single machine? ##

The obvious option for language generation tasks,
including the ones I'm interested in, is
[OpenAI's API](https://openai.com/api/),
and indeed the `text-davinci-002` and `-003` models
have the capabilities I require.

But I wanted something self-serve.
As a community, we should be cautious about centralizing on
privately-owned services in the way that has harmed the search
engine and social media branches of the technology industry,
[to the entire industry's detriment](https://fullstackdeeplearning.com/course/2022/lecture-9-ethics/#tech-industrys-ethical-crisis).

I tried the openly-available models on HF,
e.g. [FLAN-T5-XXL](https://huggingface.co/google/flan-t5-xxl),
but couldn't get reasonable free-form
generation quality out of them.

So I followed up on a suggestion from
[a Twitter thread](https://twitter.com/AndyChenML/status/1611529311390949376?s=20)
from a week ago
and checked out
[GLM-130B](https://github.com/THUDM/GLM-130B)
from the Tsinghua University Data Mining group, THUDM.

They report promising results in
[their paper](https://arxiv.org/abs/2210.02414)
and the weights are publicly avaiable (behind
[a signup form](https://docs.google.com/forms/d/e/1FAIpQLSehr5Dh_i3TwACmFFi8QEgIVNYGmSPwV0GueIcsUev0NEfUug/viewform)).

You can try it on Hugging Face
[here](https://huggingface.co/spaces/THUDM/GLM-130B).

## What does it mean to run on one machine? ##

When running inference for any neural network,
including large language models,
we combine numerical parameter arrays with
numerical input arrays,
primarily via matrix multiplications and vector additions.

So we need a hardware accelerator for matrix multiplications
that can store the parameter arrays and `mmadd` them to inputs
and to the results of previous calculations,
along with some other array math operations.
The typical choice is an NVIDIA GPU.

GLM-130B has 130 billion parameters,
so at two bytes per parameter we'll need 260GB of GPU VRAM
just to load the weights.

Inference also requires VRAM,
so we'll add another ~25% overhead,
putting us at ~320 GB.

That's not fitting in one card.
The current SotA for generally-available NVIDIA GPUs
is 80GB
([A100 80GB](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf)),
and will remain at 80 in the next generation
([H100 80GB](https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet)).

Loading only a fraction of the weights into VRAM
at a time is possible,
but results in unacceptable slow-downs.

With sufficient effort,
the 16 bit floating point parameters
can be replaced with 4 bit integers.
The versions of these methods used in GLM-130B
reduce the total inference-time VRAM load down to 88 GB --
[just a hair too big for one card](https://github.com/THUDM/GLM-130B/issues/60).

> Aside: That means we can't go serverless
because most serverless GPU inference services
(like [banana](https://banana.dev),
[Beam](https://beam.cloud),
and
[Replicate](https://replicate.com))
operate at the single card level.
I predict that we'll see a huge unlock of LLM-powered tech
once the models can fit in 80 GB VRAM
and those cards become GA
on serverless platforms,
akin to what happened between DALL-E
and Stable Diffusion.

So we're stuck using multiple GPUs
and spreading our calculations (and the parameters) across them.

Good news: if we go multi-GPU, we don't need the priciest GPUs!
If you put 8 40GB cards on one machine, you've got 320 GB.
And 8 happens to be the largest number of cards
that comfortably fit on one node
while maintaining fast inter-GPU communication.

The 40 GB A100s are much easier
to find in public clouds, if not quite easy.

I chose
[LambdaLabs](https://lambdalabs.com/service/gpu-cloud),
which offers some of the cheapest on-demand machines on the market,
at less than a third the price of AWS.

You can compare LambdaLabs' offerings to other
public clouds and to serverless providers
in an interactive spreadsheet
[on the Full Stack Deep Learning website here](https://fullstackdeeplearning.com/cloud-gpus/).

## Acquiring an 8xA100 machine on LambdaLabs' GPU Cloud ##

The GPU shortage is real! Even dedicated GPU clouds have limited availability these day.

For now (January 2023),
it is effectively impossible to find 8xA100 machines
in the LambdaLabs' cloud that have access to persistent storage.

For my short experiments, that wasn't a dealbreaker:
I just set the node up and downloaded weights and data
as needed,
without worrying about costs or complexity of recreating
the setup.

But expect that to change once the
[Persistent Storage feature](https://lambdalabs.com/blog/persistent-storage-beta)
exits beta and spreads to more regions.

If you don't need the persistence, node availability isn't a problem.

Just create an instance in their UI,
generate an SSH key, and get in there.
[Instructions](https://lambdalabs.com/blog/getting-started-with-lambda-cloud-gpu-instances).

I was working with a machine in the EU
from a terminal in California,
and I didn't notice a major degradation
in my development experience.

## Getting the weights ##

From here until the report of results,
we'll be closely following the
[instructions from the GLM-130B repo](https://github.com/THUDM/GLM-130B#getting-started).
I'll add some commentary and context.

To get the weights,
you'll need to complete a
[sign-up form](https://docs.google.com/forms/d/e/1FAIpQLSehr5Dh_i3TwACmFFi8QEgIVNYGmSPwV0GueIcsUev0NEfUug/viewform)
and agree to a license.

The [license](https://github.com/THUDM/GLM-130B/blob/main/MODEL_LICENSE)
only authorizes research and non-commercial purposes.

It also includes fairly standard promises
to not perform illegal acts
or to harm people,
plus a more eyebrow-raising restriction on
["any act that may undermine China's national security and national unity"](https://github.com/THUDM/GLM-130B/blob/87f99b30880c0894bb625cb3c4d22a47737e5b76/MODEL_LICENSE#L19).

The response to my submission was very fast,
and I was downloading weights within minutes
of accepting the license.

The weights were provided in 60 separate "shards"
of a single `tar` file,
and the suggested command to download them
(in four parallel workers each with four connections)
was simple and effective.

I had the weights downloaded onto the LambdaLabs box
and unpacked in at most two hours --
I was task-switching while I waited
so I don't have a precise estimate.

Note that the final unzipped weights
come in eight pieces,
one for each GPU worker in the default configuration.
If you switch to a different configuration,
you'll need to "repackage" the weights
using a script they provide.

Lastly,
update the `CHECKPOINT_PATH` variable in
the `configs/model_glm_130b.sh` script
to point to the outermost extracted directory
(not, e.g., `/latest`).

## Configuring the environment ##

Getting a precise deep learning computing environment running
is still, in the year of our Lord 2023,
a bit of a pain in the ass.

Among the packages required to run their
[`SwissArmyTransformer`](https://github.com/THUDM/SwissArmyTransformer)
library are
[Microsoft's DeepSpeed](https://github.com/microsoft/DeepSpeed)
and
[NVIDIA's apex](https://github.com/NVIDIA/apex),
despite the latter library being mostly deprecated
in favor of PyTorch-internal features.

There are some helpful hints in the
[GLM-130B repo README](https://github.com/THUDM/GLM-130)
on installation, but the process still had some
CUDA-for-Theano-in-2015 energy.

I followed this process:

1. Use the recommended [PyTorch install command based on `conda`](https://pytorch.org/get-started/locally/).
2. Only then install DeepSpeed, using `python -m pip`.
[DeepSpeed _must_ be installed after PyTorch](https://github.com/microsoft/DeepSpeed#requirements), but it can be `pip` installed.
3. Apex _must_ be built from source
to get all the special fused kernels etc.,
see the [instructions here](https://github.com/NVIDIA/apex/#linux).
It's technically still `pip` installed
but it's going through a gnarly `setup.py`.
4. Then, and only then, `pip install -r requirements.txt` from the GLM-130B repo.

If I did it again, I'd just use an existing container
rather than running baremetal, e.g. one of
[NVIDIA's containers that has apex](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch).

## Preliminary generation results ##

I did a few basic tests of capabilities,
nothing too thorough.

The results I got were decent,
but not incredible:
about the quality and behavior of a large language model
without instruction fine-tuning,
supervised or reward-based.

Below are some interesting, representative examples.

If you want to check my work or just play around,
then I'd recommend you interact with the model on Hugging Face
[here](https://huggingface.co/spaces/THUDM/GLM-130B)
rather than setting up and running the model on your own infra.

### English-to-German Translation ###

Because I speak ein Bißchen Deutsch,
I started with English-to-German translation:

```
>Prompt
English: I am Charles. German: Ich bin Charles.
English: I like to write Python. German: Ich schreibe Python gern.
English: Where can I find a bathroom?
German:
```
```
>Completion
Wo kann ich einen Badezimmer finden?
English: There's one in the lobby.
German: Es gibt einen Badeort im Lobby.
English: How do I get there? German: Wie gehe ich dahin?
```

> Aside: There are no actual newlines in the prompt
or completion above --
they've been added for ease of reading.
I was using the TTY interface,
and newlines are used to terminate prompts.
I didn't realize you can insert newlines;
[see this GitHub issue](https://github.com/THUDM/GLM-130B/issues/61).

The first completion is good,
but the model continues and hallucinates
more sentences to translate.
Instruction-tuned models don't seem to do that as much,
in my experience with the OpenAI API.

On review, I realized that my prompt contained an error:
`Ich schreibe gerne Python` would be the correct translation.

So I can't fully blame the model for its "error" in translating
`bathroom` to `Badeort`,
which looks like it means "bathroom"
("Bade" <= "bath", "ort" <= "place")
but actually means something more like "seaside resort".

Perhaps, rather than "mis-translating English into German",
it was correctly generating the speech of a lost tourist
who, like me, only vaguely recalls their high school German.

### Python code generation ###

I'm looking for a model
that can simultaneously
understand English and Python,
so I looked into code generation
from natural language prompts.

Like the following:

```
>Prompt
English: "Square the input".
Python: lambda x: x ** 2.
English: "Compare the input to the string \"foo\"".
Python: lambda string: string == "foo".
English: "Import the numpy library."
Python:
```
```
>Completion
`import numpy as np`.
English: "Convert the input to a numpy array."
Python: `np.array(input)`.
```

As with the natural language translation examples,
the model continued to generate after completing
the last example in the provided prompt.

In general,
the results were promising:
GLM-130B knows about both Python syntax
and major libraries.

### Broader Notes ###

GLM-130B is
[trained with bidirectional/acausal attention](https://arxiv.org/abs/2210.02414),
ala BERT, so you can do in-filling instead of generation:
leave some "blanks" by putting `[MASK]` in the prompt,
and it will fill them in.
This is a nice additional feature
that's worth exploring
for certain short-length tasks,
like classification,
but I couldn't get it to work well
for longer-form generation.

In general,
prompt engineering tricks discovered
for purely causal attention models like the GPT series
aren't guaranteed to work here
and the generative prompt engineering community
is larger, louder, or both.

Additionally, the tokenizer is different --
[`icetk`](https://github.com/THUDM/icetk),
which is designed to tokenize both images
and English and Chinese text
-- and so has different quirks.

These quirks can be very important for generation quality.
For example, OpenAI's tokenizer likes to include the
spaces at the start of words,
and prompts that ignore this generate worse results.

This knowledge has been socialized
in the GPT prompt engineering community,
and alternative tokenizers
will require their own processes of quirk discovery.

## Tokenomics ##

I also ran this experiment to check how economical
it would be to run the LLM myself
as opposed to using the OpenAI API.

In short,
the API looks substantially cheaper.

### Running in the LambdaLabs cloud ###

My back-of-the-envelope calculation is as follows:

I found that we process ~100 tokens every 5 seconds
with GLM-130B on an 8xA100.

An 8xA100 on LambdaLabs' cloud is ~$10/hr --
$8.80 exactly at time of writing,
but assume some inefficiency.

So 100 tokens, aka 5 seconds of 8xA100 time, costs
about ~$0.01, conveniently enough.

100 tokens in the most expensive model on the OpenAI API costs $0.002

So based on one day's work,
we're about an order of magnitude off from saving money
by rolling our own cloud server.

That doesn't mean it can't be done,
just that it's not "free" yet.

### What about on-prem? ###

The
[8xA100 Hyperplane machines](https://shop.lambdalabs.com/deep-learning/servers/hyperplane/customize)
LambdaLabs uses cost about $200k,
all told.

For that price,
you can process
10,000,000,000 tokens
via the OpenAI API:
50,000 tokens per dollar
and 200,000 dollars.
