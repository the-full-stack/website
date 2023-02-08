---
hide:
  - navigation
description: April 21-22, San Francisco -- Best practices and tools for building LLM-powered apps
embed_image: https://staging.fullstackdeeplearning.com/llm-bootcamp/opengraph.jpg
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

  .newsletter-signup {
    display: flex;
    align-items: center;
  }

  .newsletter-signup input[type="email"] {
    width: 100%;
    padding: 0.5rem;
    border-radius: 0.25rem;
    border-width: 1px;

    border-style: solid;
    color: black;
  }

  .newsletter-signup #mc_embed_signup_scroll {
    display: flex;
  }

  .newsletter-signup .mc-field-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
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

We are at the cusp of a technology unlock of a magnitude not seen since the early days of the Internet.

Rapid AI progress is fulfilling the old promise of Language User Interfaces (*LUI*s), which will revolutionize software just as GUIs did in the 90's.

The way AI-powered apps are built is also changing:
 
- Before LLMs, an idea would bottleneck first on training models from scratch, and then on scalable deployment.
- Now, an MVP based on pretrained, promptable LLM models and APIs can be configured and serving users in an hour.

An entirely new ecosystem of tools and tool vendors has formed around LLMs and LUIs. Even ML veterans are scrambling to orient themselves to what is now possible and figure out the most productive techniques and tools.

Engineers are asking themselves:

- Is *Prompt Engineering* a sick joke?
- Are there any good open-source LLMs?
- What is my moat if I rely on OpenAI APIs?
- Do I need to buy a cluster of NVIDIA A100s?
• How can I gather and use feedback from users?
- Should I be able to code a Transformer from scratch?
- Jesus H. Christ, how am I supposed to test these damn things?

## What

We have put together a two-day program based on emerging best practices in the LLM community and the latest research results to help you answer these questions and make the transition.

**Our goal is to get you 100% ready to build and deploy LLM applications, and be caught up with state of the art in the field.**

### Tentative Schedule

<table>
  <thead>
    <tr>
      <th></th>
      <th>Friday (April 21)</th>
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
          <li>Learn how vendors like OpenAI, Cohere, and AI21 compare with each other and with OSS options like FLAN-T5 and GLM.
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

<table>
  <thead>
    <tr>
      <th></th>
      <th>Saturday (April 22)</th>
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

## Who

We are <a href="https://fullstackdeeplearning.com">Full Stack Deep Learning</a>.
We're a team of UC Berkeley PhD alumni with years of industry experience who are passionate about teaching people how to make deep neural networks work in the real world.

Since 2018, we have taught in-person bootcamps, online multi-week cohorts, and official semester-long courses at top universities.

As former academics, we always make sure that all of our materials become accessible for free, right here on [this website](../course/2022).

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

!!! question "What do I need to know already?"
    We aim to get anyone with experience programming in Python ready to start building applications that use LLMs.

    Experience with at least one of machine learning, frontend, or backend will be helpful but not needed.

<div class="tiers">
  <div class="tier">
    <div class="tier--header">Regular</div>
    <div class="tier--price">
      <div><strike>$1450</strike> 🐣<span style="color: orange;">$950</span></div>
    </div>
    <div>
    <p>🐣 Early birds: Until we're ⅓ full, tickets are ⅓ off! 🐣<br />Sorry, we cannot accomodate any other discount requests.</p>
      <a href="https://fsdl.me/2023-llmbc-reg" style="width: 100%" class="md-button md-button--primary">Register</a>
    </div>
  </div>
  <div class="tier">
    <div class="tier--header">Academic</div>
    <div class="tier--price">
      <div><strike>$450</strike> 🐣<span style="color: orange;">$295</span></div>
    </div>
    <div>
      <p>We know what it's like to be broke in school 😅.<br />If you are a <strong>current</strong> full-time student, enjoy a lower price.</p>
      <a href="https://fsdl.me/2023-llmbc-academic" style="width: 100%" class="md-button md-button--secondary"> Get discount code </a>
    </div>
  </div>
</div>

### Can't make it?

Join 24K subscribers and we'll notify you when we eventually put the materials online.

<!-- Begin Mailchimp Signup Form -->
<div id="mc_embed_signup" class="newsletter-signup">
  <form action="https://fullstackdeeplearning.us18.list-manage.com/subscribe/post?u=68cabce2e74766ca3d2c089d6&amp;id=79e6eb0052&amp;f_id=00b517e7f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_self">
    <div id="mc_embed_signup_scroll">
      <div class="mc-field-group">
      	<label for="mce-EMAIL">Email Address</label>
      	<input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL" required>
      	<span id="mce-EMAIL-HELPERTEXT" class="helper_text"></span>
      </div>
    	<div id="mce-responses" class="clear">
    		<div class="response" id="mce-error-response" style="display:none"></div>
    		<div class="response" id="mce-success-response" style="display:none"></div>
    	</div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
      <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_68cabce2e74766ca3d2c089d6_79e6eb0052" tabindex="-1" value=""></div>
      <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="md-button md-button--secondary"></div>
    </div>
  </form>
</div>

<!--End mc_embed_signup-->

While you're at it, follow us on
<a href="https://twitter.com/full_stack_dl" target="_blank" rel="noopener">
    <span class="twemoji twitter" style="color: #1DA1F2">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <path
                d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z">
            </path>
        </svg>
    </span>
    <strong>Twitter</strong>
</a> and <a href="https://www.youtube.com/c/FullStackDeepLearning?sub_confirmation=1" target="_blank" rel="noopener">
    <span class="twemoji youtube" style="color: #FF0000;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
                d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z">
            </path>
        </svg>
    </span>
    <strong>YouTube</strong>
</a>!

## Sponsors

We're grateful to a number of sponsors who are helping us make this event happen.

### Compute Credit Sponsors

<div style="display:grid;grid-template-columns: 30% 30% 30%; row-gap: 2rem; column-gap:3%;">
  <div class="logo" markdown>
    <a href="https://modal.com"><img src="/images/modal-logo.jpg" class="person--image" height="160px" width="160px" loading="lazy" alt="Logo of Modal"></a>
    </div>
  <div class="logo" markdown>
    <a href="https://banana.dev"><img src="/images/banana-logo.jpg" height="160px" width="160px" loading="lazy" alt="Logo of banana.dev"></a>
    </div>
  <div class="logo" markdown>
    <a href="https://lambdalabs.com/cloud"><img src="/images/lambdalabs-logo.png" height="160px" width="160px" loading="lazy" alt="Logo of LambdaLabs"></a>
    </div>
</div>

We're partnering with compute vendors to offer free cloud credits to all attendees, including credits for [Modal](https://modal.com), [banana.dev](https://banana.dev), the [LambdaLabs GPU Cloud](https://lambdalabs.com/cloud) and the [OpenAI API](https://openai.com/api/).

### Direct Sponsors

<div style="display:grid;grid-template-columns: 30% 30% 30%; row-gap: 2rem; column-gap:3%;">
  <div class="logo" markdown>
    <a href="https://wandb.com"><img src="/images/wandb-logo.jpg" height="160px" width="160px" loading="lazy" alt="Logo of Weights & Biases"></a>
    </div>
</div>

Interested in sponsoring this event so you can connect with the builders of the next generation of LLM-powered tech?
You can read more about tiers and benefits [here](./sponsors).
Contact [`sponsorships @ fullstackdeeplearning.com`](mailto:sponsorships@fullstackdeeplearning.com) with inquiries.
