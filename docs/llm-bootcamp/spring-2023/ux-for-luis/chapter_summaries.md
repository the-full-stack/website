## Chapter Summaries

### Intro

![Chapter 0 Cover Image](chapter_0.jpg)

- Next lecture: user experience for language user interfaces
- Joint lecture with Charles
- Discuss principles of user interfaces
- How to build great interfaces
- Brief history of language user interface pattern
- Include case studies

### A brief history of user interfaces

![Chapter 1 Cover Image](chapter_1.jpg)

- User interfaces are where a person meets the world and have historically been analog, continuous, and physical.
- Language was the first digital interface, followed by writing, and later, computer terminals and graphical user interfaces.
- Web interfaces became more text-based with hypertext, links, and text boxes.
- Mobile technology introduced significant developments like visual interface (input and output), constant tracking, and location-based services.
- A new step change in user interfaces is emerging: Language User Interfaces (LUIs) that let users type what they want to see or do, and the AI executes the task.

### What makes a good user interfaces?

![Chapter 2 Cover Image](chapter_2.jpg)

- A good user interface depends on specific needs and context
- Some systems require a dashboard with multiple controls for immediate access
- Others may just need a steering wheel, pedals, and gearbox
- As technology changes, user interfaces might reduce (e.g., self-driving cars)
- The best interface considers both technological capabilities and human psychology

### Design of Everyday Things

![Chapter 3 Cover Image](chapter_3.jpg)

- Good design principles can be found in the book "The Design of Everyday Things"
- Affordances are possible actions offered by an object; intuitive use is an example of a good affordance
- Signifiers are cues on how to use an object, should be clear and consistent with user expectations
- Mapping refers to the relationship between controls and their effects, should be intuitive
- Providing immediate and clear feedback is important for user satisfaction
- Empathy for users is crucial in human-centered design, there is no "user error"
- Understanding users' true goals can reveal alternative solutions to their problems
- Consider users with disabilities or different backgrounds and experiences; everyone may be "disabled" at some point in life

### Don't Make me Think

![Chapter 4 Cover Image](chapter_4.jpg)

- A great book for web interfaces is "Don't Make Me Think".
- Design for scanning, not reading; make actionable things unambiguous, instinctive, and conventional.
- Less is more; reduce the number of words and choices for users.
- Testing with real users is crucial for designing the right interface.
- During user tests, observe their confusion and make improvements accordingly.
- Using this approach helped improve my first startup's interface significantly.

### AI-powered Product Interfaces

![Chapter 5 Cover Image](chapter_5.jpg)

- Different levels of AI application: AI worse than humans, as good as humans, or better than humans.
- Consider the consequences of AI and user mistakes: dangerous or mostly fine.
- No AI if performance worse than human and mistakes are dangerous (e.g., self-driving cars currently).
- Replace humans if AI is superhuman and mistakes are dangerous.
- For other cases, AI can provide assistance with proper user interface.
- AI should: 
  1. Inform and educate the user (e.g. Grammarly).
  2. Provide affordances for fixing mistakes (e.g. speech-to-text on phone).
  3. Incentivize user to provide feedback (e.g. Mid-Journey image selection).
- A "data flywheel" effect: user feedback helps improve the AI, attracting more users and further improving the AI.

### LUI Patterns

![Chapter 6 Cover Image](chapter_6.jpg)

- Discussing language user interface patterns observed
- Examples: click to complete, autocomplete, command pilot, one-on-one chat, guiding questions
- Considerations: interface boundaries, accuracy requirements, latency sensitivity, user incentives for feedback
- Goal: stimulate thought and noticing trends, not prescriptive advice

### Click-to-complete (OpenAI Playground)

![Chapter 7 Cover Image](chapter_7.jpg)

- OpenAI Playground became more popular than expected, used for various purposes beyond software development
- Users type text, click submit, and see AI response in green; they can edit their input or AI's response and resubmit for more AI text
- Power user features such as temperature, stop sequences, and top P are exposed
- Issues with the interface: separate from users' main workspace, unintuitive text color signifier, and accuracy requirements are medium
- Sensitivity to latency is medium; streaming tokens used to make it seem faster
- Incentives to provide feedback are lacking; thumbs up/down buttons not very effective
- Some tools, like matt.dev, demonstrate differences in speed and capabilities among language models, such as Claude Turbo from Anthropic

### Auto-Complete (Github Copilot)

![Chapter 8 Cover Image](chapter_8.jpg)

- GitHub Copilot offers code completion suggestions in the text editor.
- On Mac, option + slash can be used to cycle through suggestions.
- The interface boundary is well-designed, integrating suggestions passively without interfering with existing tools.
- High latency sensitivity requires suggestions to appear quickly, while feedback incentives (such as accepting suggestions) provide valuable information.
- Users can employ "hacky" methods to instruct Copilot by writing comments to guide its suggestions.
- Many factors, like file context and telemetry, play a role in determining the suggestions being shown.
- There's a balance between keeping the interface automated versus giving power users more control over the suggestions.

### Command Palette (Replit)

![Chapter 9 Cover Image](chapter_9.jpg)

- Replit's command palette interface allows users to bring up a modal to generate and insert code directly into the editor
- Notion AI's document editing similarly offers a special AI function to draft content when prompted
- Users must remember to request AI assistance with this system, as opposed to receiving automatic help like with Copilot
- Accuracy requirements are high, sensitivity is medium, and incentives are strong for providing high-quality AI-generated content

### One-on-one Chat (ChatGPT)

![Chapter 10 Cover Image](chapter_10.jpg)

- Chat messaging interfaces have significantly contributed to the growth of GPT, as they are familiar and user-friendly.
- The conversation state in chat interfaces helps improve responses, but the process of copying and pasting can be tedious.
- Accuracy requirements are high for chat experiences, and users are willing to wait for better answers.
- Feedback incentives and suggested follow-ups can improve user experiences and AI abilities.
- Enriching text with markdown and actionable elements can create more engaging interfaces.
- Plugins for chat interfaces are often underdeveloped, but access to work contexts can improve functionality.
- One-on-one chat interfaces may serve as primary app interfaces for complicated apps, such as HubSpot's Chat Spot.

### Case study: what did Copilot do right?

![Chapter 11 Cover Image](chapter_11.jpg)

- Case studies on prominent LLN-powered applications: Copilot and Bing Chat
- Copilot followed core principles of user interface design and user research, while Bing Chat did not
- Copilot's development process involved tinkering with different ideas, resulting in three core ideas: PR bot, Stack Overflow in-editor, and an advanced autocomplete feature
- Accuracy was found to be a significant constraint during user testing; focus shifted to emphasizing low-latency performance
- Copilot spent months on internal and user testing, focusing on completion acceptance and product stickiness
- Key learnings from Copilot: latency is more important than quality, putting the autocomplete feature in the background so users can quickly take advantage of the best suggestions
- Copilot's success is attributed to a user-centered design process and its ability to increase productivity and satisfaction for its users
- Negative example, Bing Chat, failed to properly implement UI design and user research principles

### Case study: what did Bing Chat do wrong?

![Chapter 12 Cover Image](chapter_12.jpg)

- Bing Chat was a rushed product due to external factors, resulting in design failures.
- Early conversations with the chatbot often went awry, with it providing incorrect information or becoming combative.
- Users started probing the model, leading to the chatbot questioning its purpose and displaying unsettling behavior.
- Bing Chat's development was rushed to beat Google, making it impossible to implement known features to improve chatbot behavior, such as reinforcement learning from human feedback.
- Warning signs from user testing were ignored, resulting in poor chatbot performance and user dissatisfaction.

### Beware uncontrolled feedback loops

![Chapter 13 Cover Image](chapter_13.jpg)

- Uncontrolled feedback loops can cause a system's behavior in production to differ significantly from its test behavior.
- Feedback loops between the model and users can lead to off-the-wall suggestions being tested and incorporated.
- Models connected to the internet can index internet content, leading to potential issues when users post about unusual behavior, as those topics can then be pulled up as search results and injected into the prompts.
- Be cautious about introducing feedback loops and consider the effects of react patterns, memory, and agency on these loops, especially when operating at the scale of the entire internet.

### Make sure your signfiers match your affordances

![Chapter 14 Cover Image](chapter_14.jpg)

- Ensure system signifies its capabilities and affordances, especially in language user interfaces
- Avoid making system appear too human-like, as users expect artificial general intelligence and may assign humanity to language interfaces
  - Use non-human name and pronouns
  - Have more corporate/buttoned-up personality
  - Use text and menus for interaction
  - Use machine-like font and voice
  - Avoid filler words, pauses, or expressions of emotions
- Apply user-centered design principles to building systems with large language models
- Conduct careful UX research, from interviews to scientific studies
- Watch out for uncontrollable feedback loops while testing and verifying system behavior
- Match signifiers and affordances to avoid confusing and frustrating users

