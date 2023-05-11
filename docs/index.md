---
hide:
  - navigation
  - toc
---
<style>
  /*
    over-ride default margings for markdown content in material
  */
  .md-main__inner {
    margin-top: 0;
  }
 .md-grid {
    max-width: 100vw;
  }
  .md-content__inner {
    margin: 0;
    padding: 0;
  }
  .md-content__inner::before {
    height: 0;
  }
</style>

<div class="flex-col">

  <div class="announce grid-2 items-center primary-swapped-bg-fg pb-2 m-0">
    <img src="images/pancakes.svg" style="max-height: 12rem; auto;" draggable="false" class="swap-first m-auto">
    <div class="mb-8 mx-4 swap-last">
      <h2><strong>{{ config.site_description }}</strong></h2>
      <p><br></p>
      <a href="/llm-bootcamp" class="md-button md-button--primary">
        Free LLM Bootcamp Available Now!
      </a>
    </div>
  </div>

  <div class="grid-2 items-center px-4 py-4">
    <div class="mb-4 swap-last">
        <h2>Building an AI-powered product is much more than just training a model or writing a prompt.</h2>
        <p>The Full Stack brings people together to learn and share best practices across the entire lifecycle of an AI-powered product:
            from defining the problem and picking a GPU or foundation model to production deployment and continual learning
            to user experience design.
        </p>
    </div>
    <img src="images/full_stack_description.png" class="swap-first">
  </div>

  <div class="grid-2 items-center py-4 px-4 primary-swapped-bg-fg">
    <a href="llm-bootcamp"><img src="llm-bootcamp/opengraph.png"></a>
    <div class="mb-4">
        <h2>Get up to speed on the latest in AI-powered apps with the new <a href="llm-bootcamp">Large Language Models Bootcamp</a>.</h2>
        <br>
        <p>
          Learn best practices and tools for building applications powered by LLMs. </p> <p> Cover the full stack from <a href="llm-bootcamp/prompt-engineering">prompt engineering</a> and <a href="llm-bootcamp/llmops">LLMops</a> to <a href="llm-bootcamp/ux-for-luis">user experience design</a>.
        </p>
    </div>
  </div>

  <div class="grid-2 items-center px-4 py-4">
    <a href="course"><img src="images/positioning.png" class="swap-first" draggable="false"></a>
    <div class="swap-last">
        <h2>Build an AI-powered application from the ground up in our <a href="course">Deep Learning Course</a>.</h2>
        <p>
          You've trained your first (or 100th) model, and you're ready to take your skills to the next level.
        </p>
        <p>
            Join thousands from <a href="https://bit.ly/berkeleyfsdl">UC Berkeley</a>,
            <a href="https://bit.ly/uwfsdl">University of Washington</a>, and <a
                href="https://youtube.com/c/FullStackDeepLearning">all over the world</a>
            and learn best practices for building AI-powered products from scratch with deep neural networks.
        </p>
    </div>
  </div>

  <div class="mb-8 px-4">
      <div style="text-align: center; margin-top: 1em;">
          <a class="md-button md-button--primary" href="https://fsdl.me/join-discord">🚀 Join us on Discord 🚀</a>
      </div>
  </div>
  </div>

</div>
