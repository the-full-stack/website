---
hide:
  - navigation
description: Best practices and tools for building LLM-powered apps
embed_image: https://fullstackdeeplearning.com/llm-bootcamp/opengraph.png
---

<style>
  .admonition.abstract p, .admonition.abstract ul {
    font-size: large;
  }
  [dir=ltr] .md-typeset .admonition.abstract .admonition-title {
    padding-left: 0.6rem;
    text-align: center;
  }
  .admonition.abstract .admonition-title::before {
    display: none;
  }
  .md-typeset .admonition.abstract>:last-child {
    margin-bottom: 1.25rem;
  }

  .md-typeset table:not([class]) {
    font-size: inherit;
    line-height: inherit;
  }
  .md-typeset table:not([class]) td {
    vertical-align: top;
  }
  .md-typeset table:not([class]) th {
    white-space: nowrap;
    min-width: 5rem;
  }

  .emoji-bullets {
    list-style-type: none; /* Remove default bullet points */
    padding: 0; /* Remove default padding */
  }

  .emoji-bullets li {
    position: relative; /* Create a positioning context for the emoji */
    margin-bottom: 0.5rem; /* Add some space between list items */
    padding-left: 0.5em
  }

  .emoji-bullets li::marker {
  content: ''; /* Remove the default marker */
  }

  .emoji-bullets .emoji {
    position: absolute; /* Position the emoji relative to the li element */
    left: -1.5em; /* Move the emoji to the left of the list item */
  }
</style>

# LLM Bootcamp

<div class="admonition abstract">
  <p class="admonition-title">🚀 Full Stack LLM Bootcamp 🚀</p>
  <div class="grid-2 items-center">
    <ul>
      <li>Learn <strong>best practices and tools</strong> for building LLM-powered apps</li>
      <li>Lectures released via YouTube from <strong>May 22 - June 16</strong></li>
      <li>Join the <strong>project cohort</strong> and get feedback on your work</li>
      <li>Get <strong>cloud credits</strong> from OpenAI and others to help you build and run your LLM app</li>
    </ul>
    <div class="flex items-center justify-center">
      <img alt="Venn diagram showing that FSDL is at the intersection of a course, a hackathon, and a conference." src="/images/fsdl-2023-overview.png" width="480px">
    </div>
  </div>
  <div class="flex justify-center mt-8 mb-2">
    <a href="spring-2023" class="md-button">Access the materials!</a>
  </div>
</div>


<div class="flex items-center justify-center">
  <img alt="Image of the instructors and attendees at the 2023 FSDL LLM Bootcamp" src="/images/llmbc-2023-audience.jpg" width="100%">
</div>


## Why

We are at the cusp of a technology unlock of a magnitude not seen since the early days of the Internet.
Rapid AI progress is fulfilling the old promise of Language User Interfaces (*LUI*s), which will revolutionize software just as GUIs did in the 90s.

The way AI-powered apps are built is rapidly changing:

- Before LLMs, an idea would bottleneck on training models from scratch, and then it'd bottleneck again on scalable deployment.
- Now an MVP based on pretrained, promptable LLM models and APIs can be configured and serving users in an hour.

An entirely new ecosystem of techniques, tools, and tool vendors is forming around LLMs and LUIs. Even ML veterans are scrambling to orient themselves to what is now possible and figure out the most productive techniques and tools.

## What

We're releasing the lecture materials from our
[in-person LLM bootcamp](./april-2023/)
for free, for everyone!
We'll be posting them on
[our YouTube channel](https://youtube.com/c/@FullStackDeepLearning)
over the coming weeks.

We'd like to use this opportunity to bring
together people who are interested in building LLM-powered apps.
And while there are lots of in-person one-day hackathons,
there are fewer opportunities to work on projects
online and over the course of multiple days or weeks.

So if you're interested in building an LLM app and
getting feedback from experts,
join our [project cohort](#register)!
You'll get:

- Immediate access to the lecture videos when the course starts
- Compute credits, including $50 for the OpenAI API, to help you get your app off the ground
- Developer access to ChatGPT plugins
- Access to a private Discord, weekly Q&A sessions, and office hours

We think the best software is built by teams,
so we're encouraging cohort members to form groups to work on their projects.
If you already have a team of three or more,
[fill out this form](https://fsdl.me/llmbc-online-teams)
for a 10% discount on registration!

!!! question "What do I need to know already?"
    The lectures aim to get anyone with experience programming in Python ready to start building applications that use LLMs.

    Experience with at least one of machine learning, frontend, or backend will be very helpful.

    If you want to participate in the project cohort,
    you should either be comfortable with building the stack your project requires
    or willing to contribute your specific skills to a team.

## When

| Date           | Lecture Release                    | Q&A Session     | Project              |
|----------------|------------------------------------|-----------------|----------------------|
| **2023.05.22** | Launch an LLM App in an Hour       | Course Overview | -                    |
| **2023.05.24** | LLM Foundations                    | -               | -                    |
| **2023.05.25** | Learn to Spell: Prompt Engineering | -               | Proposal due         |
| **2023.05.29** | Augmented LMs: Retrieval           | LLM Foundations | Feedback on proposal |
| **2023.05.31** | Augmented LMs: Tools               | -               | -                    |
| **2023.06.02** | askFSDL Project Overview           | -               | -                    |
| **2023.06.05** | UX for LUIs                        | Augmented LMs   | -                    |
| **2023.06.07** | LLMOps                             | -               | -                    |
| **2023.06.09** | What's Next?                       | -               | Submit project       |
| **2023.06.12** | -                                  | What's Next?    | Feedback on project  |
| **2023.06.16** | -                                  | -               | Top projects present |

## Who

We are <a href="https://fullstackdeeplearning.com">Full Stack Deep Learning</a>.
We're a team of UC Berkeley PhD alumni with years of industry experience who are passionate about teaching people how to make deep neural networks work in the real world.

Since 2018, we have taught in-person bootcamps, online multi-week cohorts, and official semester-long courses at top universities.

<div class="grid-3">
  <img alt="Group photo of the attendees of FSDL March 2019 bootcamp" src="/images/group-march2019.jpg" width="480px">
  <img alt="Group photo of the attendees of FSDL August 2018 bootcamp" src="/images/group-august2018.jpg" width="480px">
  <img alt="Group photo of the attendees of FSDL November 2019 bootcamp" src="/images/group-november2019.jpg" width="480px">
</div>

### Instructor Team

<div class="grid-2">
  <div class="person">
    <img src="/images/charles.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Charles Frye">
    <div><strong>Charles Frye</strong> educates people in AI. He has worked on AI/ML tooling with Weights & Biases and Gantry since getting a PhD in Theoretical Neuroscience at UC Berkeley.</div>
  </div>
  <div class="person">
    <img src="/images/sergey.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Sergey Karayev">
    <div>
    <strong>Sergey Karayev</strong> builds AI-powered products as Co-founder of Volition. He co-founded Gradescope after getting a PhD in AI at UC Berkeley.
    </div>
  </div>
  <div class="person">
    <img src="/images/josh.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Josh Tobin">
    <div>
    <strong>Josh Tobin</strong> builds tooling for AI products as Co-founder and CEO of Gantry. He worked as a Research Scientist at OpenAI and received a PhD in AI at UC Berkeley.
    </div>
  </div>
</div>

## Register

<div class="pricing">
  <div class="tier">
    <div class="tier--header">On-Your-Own</div>
    <div class="tier--price">
      $0.00
    </div>
    <div class="tier--priceCaption" style="visibility: hidden;">
    <!-- hidden but present to align the two tiers -->
      <div><a href="https://fsdl.me/llmbc-online-academics">50% discount for students and post-docs</a></div>
    <!-- hidden but present to align the two tiers -->
      <div><a href="https://fsdl.me/llmbc-online-teams">10% discount for teams of three or more</a></div>
    </div>
    <ul class="tier--features emoji-bullets">
      <li><span class="emoji">📹</span> Lecture videos released on YouTube</li>
    </ul>
    <div style="margin-top: auto;">
      <a href="http://eepurl.com/dxYwXj" style="width: 100%" class="md-button">Sign Up for Mailing List</a>
    </div>

  </div>
  <div class="tier">
    <div class="tier--header">Project Cohort</div>
    <div class="tier--price">
      <span>$495</span>
    </div>
    <div class="tier--priceCaption">
      <div><a href="https://fsdl.me/llmbc-online-academics">50% discount for students and post-docs</a></div>
      <div><a href="https://fsdl.me/llmbc-online-teams">10% discount for teams of three or more</a></div>
    </div>
    <ul class="tier--features emoji-bullets">
      <li><span class="emoji"> 🎨 </span>Build a portfolio project and get feedback
      <li><span class="emoji"> 🏆 </span>Top projects featured on FSDL website and YouTube channel
      <li><span class="emoji"> 📹 </span>Immediate access to lecture videos
      <li><span class="emoji"> ❓ </span>Weekly Q&A, live Monday am Pacific & recorded
      <li><span class="emoji"> 🧑‍🏫 </span>Video conference office hours
      <li><span class="emoji"> 💲 </span>Cloud credits and ChatGPT plugin access
      <li><span class="emoji"> 🌐 </span>Private Discord forum with instructors and fellow builders
      <li><span class="emoji"> 🔜 </span>Starts May 22nd, 2023
    </ul>
    <div style="margin-top: auto">
      <a href="https://fsdl.me/llmbc-online-register" style="width: 100%" class="md-button">Register</a>
    </div>
  </div>
</div>

If you have any questions about the bootcamp, contact
[`admin @ fullstackdeeplearning.com`](mailto:admin@fullstackdeeplearning.com).
We cannot honor requests for additional discounts.
