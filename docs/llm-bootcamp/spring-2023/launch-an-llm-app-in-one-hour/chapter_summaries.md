## Chapter Summaries

### Why now?

![Chapter 0 Cover Image](chapter_0.jpg)

- Excitement about large language models and artificial intelligence is high, especially since one tool can now accomplish tasks that previously required multiple specialized tools.
- Language user interfaces (LUIs) enable more natural interaction with computers through speech and natural language. Large language models, like GPT-3, make LUIs more flexible and capable.
- Products and applications are being built with these models, including OpenAI's ChatGPT and GitHub Copilot, hinting at a promising future.
- However, the gap between demos and actual products is significant. Overpromising and underdelivering in the past led to "AI winters," so it's important to create valuable products and tools to maintain funding and interest.
- The playbook for building applications with language models is emerging, and this boot camp will cover aspects of that process.

### Prototyping & Iteration in a Playground

![Chapter 1 Cover Image](chapter_1.jpg)

- Attended various hackathons focused on using machine learning tools
- Explored the potential of high-capability hosted models, such as OpenAI's, in a simple chat interface to quickly test capabilities
- Used a notebook environment for quick tinkering, building prototypes, and discovering limitations of language models
- Started with a problem statement: using large language models to learn about large language models
- Discovered difficulties with language models, such as having outdated and limited information
- Found that providing specific sources or papers can help improve answers from the model

### Prototyping & Iteration in a Notebook

![Chapter 2 Cover Image](chapter_2.jpg)

- Experiment with automating steps in ephemeral notebook environment like Collab.
- OpenAI API allows interaction with language models and offers various SDKs.
- Lang chain is a popular open-source framework for interacting with these models; it's fast-evolving and provides all necessary components.
- Develop a process to find information and bring it to context. Utilize Python libraries like `archive` for data sourcing.
- Utilize document loaders, such as the one built into Lang chain, to extract content from PDFs.
- Use embedding search for large scale information retrieval within documents.
- Prototype and tinker with language models to constantly improve them.
- Look for similar existing projects to jump off or even default examples provided, such as Lang chain's default example.
- Turn these experiments into something usable by people at a larger scale.
- The workflow with modern language models is more flexible and faster compared to the past machine learning processes.

### Deploying an MVP

![Chapter 3 Cover Image](chapter_3.jpg)

- Building an MVP version of an application requires focusing on what's useful to a broad range of users.
- Prioritize the user interface and gather feedback from users quickly.
- Cloud-native tooling and serverless infrastructure like Model are helpful in swiftly scaling applications and addressing data processing bottlenecks.
- Use various tech stacks for different tasks, such as OpenAI for language models, Pinecone for quick search, MongoDB for data storage, and AWS for running lightweight Discord bot servers.
- Implement the application, then monitor usage data to make improvements and learn from successes and failures.

