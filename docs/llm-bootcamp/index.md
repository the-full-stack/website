---
hide:
  - navigation
description: April 21-22, San Francisco -- Best practices and tools for building LLM-powered apps
embed_image: https://llm-bootcamp/opengraph.jpg
---

<style>
  .admonition.abstract p, .admonition.abstract ul {
    font-size: large;
  }
   [dir=ltr] .md-typeset .admonition.abstract .admonition-title {
    padding-left: 0.6rem;
  }
  .admonition.abstract .admonition-title::before {
    display: none;
  }
</style>

# LLM Bootcamp
<div class="flex flex-col items-center justify-center" markdown>
!!! abstract "🚀 Announcing Full Stack Deep Learning LLM Bootcamp 🚀"
    - In person in San Francisco on **April 21-22**
    - Learn **best practices and tools** for building LLM-powered apps
    - **Network** with a couple hundred other builders
    - Get cloud credits from OpenAI and other [sponsors](#sponsors)

  [Register now](#register){ .md-button .md-button--primary }
</div>
## Why

**We are at the cusp of a technology unlock of a magnitude not seen since the early days of the Internet.**

Large language models (LLMs) understand text both semantically and syntactically,
fulfilling the promise of an old idea in artificial intelligence and human-computer interaction:
_Natural Language User Interfaces_, or LUIs.

As with GUIs, LUIs promise to revolutionize how we use and interface with computing systems and become the specialty of a new class of developer.

At the same time that LLMs have made LUIs possible,
the process for developing an application around machine learning models has become easier.

Where once an idea for a useful, delightful, and intelligent technology
would bottleneck on training models from scratch
and then on deployment,
now an MVP based on pretrained models and APIs can be configured and serving users in an hour.

<h3>With a gold rush come new shovels and shovel-sellers.</h3>
An entirely new ecosystem of tools and tool vendors has formed around LLMs and LUIs. Even ML veterans are scrambling to orient themselves to the new possible and figure out the most productive new sets of techniques and tools.

Engineers are asking themselves:

- Is *Prompt Engineering* a joke?
- Are there good open-source LLMs?
- Do I need to buy a cluster of NVIDIA A100s?
- What is my moat if I’m relying on OpenAI APIs?
- Should I be able to code a Transformer from scratch?
- How can I gather feedback from users and use it to improve AI?
- Jesus H. Christ, how am I supposed to test these damn things?

<!-- - How do principles like compositionality, data structures, and recursion transfer? -->
<!-- - What's the deal with linear-time attention mechanisms? -->
<!-- - How do software engineering workflows like CI/CD and test-driven design transfer? -->

## What

We have put together a two-day program
based on emerging conventions in the LLM community and the latest research results
to help you answer these questions and make the transition.

!!! question "What do I need to know already?"
    We aim to get anyone with experience programming in Python ready to start building applications that use LLMs.

    Experience with at least one of machine learning, frontend, or backend will be helpful but not needed.

### Tentative Schedule

<div class="md-typeset__scrollwrap">
  <div class="md-typeset__table">
    <table style="width: 85%">
    <thead>
      <tr>
        <th></th>
        <th><h2>Friday (April 21)</h2></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>9 am</td>
        <td>Registration &amp; Breakfast</td>
      </tr>
      <tr>
        <td>10 am</td>
        <td>
          <strong>🚀 Launch an LLM App in 1 Hour</strong>
          <ul>
          <li> We'll go from idea to user-ready website in one hour
          </ul>
        </td>
      </tr>
      <tr>
        <td>11 am</td>
        <td>
          <strong>🗿 Foundations of Foundation Models</strong>
          <br />
        <ul>
          <li>Learn the core concepts behind transformer architectures, self-supervised learning, and text generation
          <li>Develop clear intuitions for model internals based on the latest work in "reverse engineering" LLMs
        </ul>
        </td>
      </tr>
      <tr>
        <td>12 pm</td>
        <td>Lunch and networking</td>
      </tr>
      <tr>
        <td>1 pm</td>
        <td>
          <strong>✨ Learn to Spell: Effectively Using LLMs</strong>
          <ul>
            <li>Learn how vendors, like OpenAI, Cohere, and AI21, compare with each other and with open source options like FLAN-T5 and GLM.
            <li>Prompt engineering tips and tricks: few-shot examples, chain-of-thought, formatting
            <li>Context engineering concepts: incorporating local information into LLM context, the wishlist-fulfillment architecture, long-term memory
            <li>Software tools: LangChain, GPTIndex, Everyprompt, dust.tt
          </ul>
        </td>
      </tr>
      <tr>
        <td>2 pm</td>
        <td>
          <strong>👀 Search 2.0</strong>
          <ul>
            <li>How text embeddings enable semantic search everywhere
            <li>Choosing between vector stores, like FAISS, Milvus, Pinecone, Weaviate, and Vespa
            <li>Jointly embedding multiple types of data for multi-modal semantic search
          </ul>
        </td>
      </tr>
      <tr>
      <td>3 pm</td>
      <td>Coffee and networking</td>
      </tr>
      <tr>
      <td>4 pm</td>
      <td>
        👷‍♂️ <strong>askFSDL Walkthrough</strong>
          <ul>
          <li> Detailed breakdown of a well-documented sample project demonstrating use of LLM APIs and frameworks, traditional and vector databases, and user feedback ingestion
          </ul>
      </td>
      </tr>
      <tr>
      <td>5 pm</td>
      <td>Invited Talk</td>
      </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="md-typeset__scrollwrap">
  <div class="md-typeset__table">
    <table style="width:85%">
    <thead>
      <tr>
        <th></th>
        <th><h2> Saturday (April 22) </h2></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>9 am</td>
        <td>Breakfast</td>
      </tr>
      <tr>
        <td>10 am</td>
                <td>
          <strong>🌳 Demo Garden</strong>
          <ul>
            <li>Present your project
            <li>Review other cool projects
          </ul>
        </td>
      </tr>
      <tr>
        <td>11 am</td>
        <td>
          <strong>🤷 UX for LUIs</strong>
          <ul>
            <li>Review of the best AI-powered apps today
            <li>Principles of successful design for AI-powered apps
          </ul>
        </td>
      </tr>
      <tr>
        <td>12 pm</td>
        <td>Lunch and networking</td>
      </tr>
      <tr>
        <td>1 pm</td>
        <td>
          <strong>🏎️ Deploying and Learning in Production</strong>
          <ul>
            <li>Deploying on CPUs vs GPUs
            <li>Why "learn in prod" is the new "test in prod"
            <li>How to monitor models, trace chains, and record feedback
            <li>Methods for learning from user data, like reinforcement learning from human feedback (RLHF), and from chains of LLMs, like Constitutional AI
          </ul>
        </td>
      </tr>
      <tr>
        <td>2 pm</td>
        <td>
          <strong>🔮 Future Directions</strong>
          <ul>
            <li>Lightning tour of things that are surprisingly possible today
            <li>What you should expect to be possible within a couple of years
            <li>What are still hard research problems
          </ul>
        </td>
      </tr>
      <tr>
      <td>3 pm</td>
      <td>Coffee and networking</td>
      </tr>
      <tr>
      <td>4 pm</td>
      <td>
        🦜🔗 <strong>Harrison Chase</strong>: Creator of LangChain
      </td>
      </tr>
      <tr>
      <td>5 pm</td>
      <td>Invited Talk</td>
      </tr>
      </tbody>
    </table>
  </div>
</div>

## Who

We are Full Stack Deep Learning.
We're a team of UC Berkeley PhD alumni with years of industry experience who are passionate about teaching people how to make deep neural networks work in the real world.

Since 2018, we have taught in-person bootcamps, online multi-week cohorts, and official semester-long courses at top universities.

We make sure that all of our materials becomes accessible for free, right here on [this website](../course/2022) -- please [explore](../cloud-gpus/)[!](../404)

<div class="grid-3">
  <img src="/images/group-march2019.jpg" width="480px">
  <img src="/images/group-august2018.jpg" width="480px">
  <img src="/images/group-november2019.jpg" width="480px">
</div>

### Instructor Team

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(20rem, 1fr));  row-gap: 2rem; column-gap:3%;">
  <div class="person" markdown>
    <img src="/images/charles.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Charles Frye">
    <div><strong>Charles Frye</strong> educates people in AI. He has worked on AI/ML tooling with Weights & Biases and Gantry since getting a PhD in Theoretical Neuroscience at UC Berkeley.</div>
  </div>
  <div class="person" markdown>
    <img src="/images/sergey.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Sergey Karayev">
    <div markdown>
    <strong>Sergey Karayev</strong> builds AI-powered products as Co-founder of Volition. He co-founded Gradescope after getting a PhD in AI at UC Berkeley.
    </div>
  </div>
  <div class="person" markdown>
    <img src="/images/josh.png" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Josh Tobin">
    <div markdown>
    <strong>Josh Tobin</strong> builds tooling for AI products as Co-founder and CEO of Gantry. He worked as a Research Scientist at OpenAI and received a PhD in AI at UC Berkeley.
    </div>
  </div>
</div>

### Guest Talks

<div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(20rem, 1fr)); row-gap: 2rem; column-gap:5%;">
  <div class="person" markdown>
    <img src="/images/harrison.jpg" class="person--image" height="160px" width="160px" loading="lazy" alt="Photo of Harrison Chase">
    <div><strong>Harrison Chase</strong> is the creator of LangChain.</div>
  </div>
</div>

## When and Where

The event will be **in-person** and run **all day** on **Friday, April 21, 2023** and **Saturday, April 22, 2023** at the [South San Francisco Conference Center](https://ssfconf.com/).

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d74597.27001002253!2d-122.39849142057383!3d37.69637486488224!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808f79b47d5d81ad%3A0xfd9c1f0af6155a3d!2sSouth%20San%20Francisco%20Conference%20Center!5e0!3m2!1sen!2sus!4v1674094089226!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

## Register

<div class="flex flex-col justify-center" style="align-items: flex-start" markdown>
!!! abstract "🐣 Discount for Early Birds 🐣"
    Until we're ⅓ full, tickets are ⅓ off!
</div>

<div class="tiers">
  <div class="tier">
    <div class="tier--header">Regular</div>
    <div class="tier--price">
      <div><strike>$1450</strike> 🐣$950</div>
    </div>
    <div>
    <p>We are not able to accomodate discount requests.</p>
      <a href="https://fsdl.me/2023-llmbc-reg" style="width: 100%" class="md-button md-button--primary">Register</a>
    </div>
  </div>
  <div class="tier">
    <div class="tier--header">Academic</div>
    <div class="tier--price">
      <div><strike>$450</strike> 🐣$295</div>
    </div>
    <div>
      <p>If you are a current full-time student or postdoc.</p>
      <a href="https://fsdl.me/2023-llmbc-academic" style="width: 100%" class="md-button md-button--secondary"> Get discount code </a>
    </div>
  </div>
