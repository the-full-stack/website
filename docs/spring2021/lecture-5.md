# Lecture 5: ML Projects

Learn how to set up Machine Learning projects like a pro. This includes an understanding of the ML lifecycle, an acute mind of the feasibility and impact, an awareness of the project archetypes, and an obsession with metrics and baselines.

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/pxisK6RMn1s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Slides

<iframe src="//www.slideshare.net/slideshow/embed_code/key/jGIcGsyNmqY3KA" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

[Download slides as PDF](https://drive.google.com/file/d/1btKp1aGQzdvn2QCCPFVAUN1aTsl3B0j_/view?usp=sharing)

## Notes

*Lecture by [Josh Tobin](http://josh-tobin.com).
Notes transcribed by [James Le](https://twitter.com/le_james94) and [Vishnu Rachakonda](https://www.linkedin.com/in/vrachakonda/).*

### 1 - Why Do ML Projects Fail?

Based on [<u>a report from
TechRepublic</u>](https://www.techrepublic.com/article/why-85-of-ai-projects-fail/)
a few years back, despite increased interest in adopting machine
learning (ML) in the enterprise, 85% of machine learning projects
ultimately fail to deliver on their intended promises to business.
Failure can happen for many reasons; however, a few glaring dangers will
cause any AI project to crash and burn.

-   ML is still very much a research endeavor. Therefore it is very
 challenging to aim for a 100% success rate.

-   Many ML projects are technically infeasible or poorly scoped.

-   Many ML projects never leap production, thus getting stuck at the
 prototype phase.

-   Many ML projects have unclear success criteria because of a lack of
 understanding of the value proposition.

-   Many ML projects are poorly managed because of a lack of interest
 from leadership.

### 2 - Lifecycle

It’s essential to understand what constitutes all of the activities in a
machine learning project. Typically speaking, there are four major
phases:

1.  **Planning and Project Setup**: At this phase, we want to decide the problem to work on, determine the requirements and goals, figure out how to allocate resources properly, consider the ethical implications, etc.

2.  **Data Collection and Labeling**: At this phase, we want to collect training data and potentially annotate them with ground truth, depending on the specific sources where they come from. We may find that it’s too hard to get the data, or it might be easier to label for a different task. If that’s the case, go back to phase 1.

3.  **Model Training and Model Debugging**: At this phase, we want to implement baseline models quickly, find and reproduce state-of-the-art methods for the problem domain, debug our implementation, and improve the model performance for specific tasks. We may realize that we need to collect more data or that labeling is unreliable (thus, go back to phase 2). Or we may recognize that the task is too challenging and there is a tradeoff between project requirements (thus, go back to phase 1).

4.  **Model Deploying and Model Testing**: At this phase, we want to pilot the model in a constrained environment (i.e., in the lab), write tests to prevent regressions, and roll the model into production. We may see that the model doesn’t work well in the lab, so we want to keep improving the model’s accuracy (thus, go back to phase 3). Or we may want to fix the mismatch between training data and production data by collecting more data and mining hard cases (thus go back to phase 2). Or we may find out that the metric picked doesn’t actually drive downstream user behavior, and/or performance in the real world isn’t great. In such situations, we want to revisit the projects’ metrics and requirements (thus, go back to phase 1).

<img src="/spring2021/lecture-5-notes-media/image4.png" style="width:4.42708in;height:4.12966in" />

Besides the per-project activities mentioned above, there are two other
things that any ML team will need to solve across any projects they get
involved with: (1) building the team and hiring people; and (2) setting
up infrastructure and tooling to build ML systems repeatedly and at
scale.

Additionally, it might be useful to understand state-of-the-art results
in your application domain so that you know what’s possible and what to
try next.

### 3 - Prioritizing Projects

To prioritize projects to work on, you want to find high-impact problems
and assess the potential costs associated with them. The picture below
shows a general framework that encourages us to target projects with
high impact and high feasibility.

<img src="/spring2021/lecture-5-notes-media/image2.png" style="width:6.5in;height:3.55556in" />

#### High Impact

There are no silver bullets to find high-impact ML problems to work on,
but here are a few useful mental models:

-   Where can you take advantage of cheap prediction?

-   Where is there friction in your product?

-   Where can you automate complicated manual processes?

-   What are other people doing?

#### Cheap Prediction

 In the book “[<u>Prediction
Machines</u>](https://www.amazon.com/Prediction-Machines-Economics-Artificial-Intelligence/dp/1633695670),”
the authors (Ajay Agrawal, Joshua Gans, and Avi Goldfarb) come up with
an excellent mental model on the economics of Artificial Intelligence:
*As AI reduces the cost of prediction and prediction is central for
decision making, cheap predictions would be universal for problems
across business domains*. Therefore, you should look for projects where
cheap predictions will have a huge business impact.

#### Product Needs

Another lens is to think about what your product needs. In the article
“[<u>Three Principles for Designing ML-Powered
Products</u>](https://spotify.design/article/three-principles-for-designing-ml-powered-products),”
the Spotify Design team emphasizes the importance of building ML from a
product perspective and looking for *parts of the product experience
with high friction*. Automating those parts is exactly where there is a
lot of impact for ML to make your business better.

#### ML Strength

In his popular blog post “[<u>Software
2.0</u>](https://medium.com/@karpathy/software-2-0-a64152b37c35),”
Andrej Karpathy contrasts software 1.0 (which are traditional programs
with explicit instructions) and software 2.0 (where humans specify
goals, while the algorithm searches for a program that works). Software
2.0 programmers work with datasets, which get compiled via
optimization — which works better, more general, and less
computationally expensive. Therefore, you should look for *complicated
rule-based software* where we can learn the rules instead of programming
them.

#### Inspiration From Others

Instead of reinventing the wheel, you can look at what other companies
are doing. In particular, check out papers from large frontier
organizations (Google, Facebook, Nvidia, Netflix, etc.) and blog posts
from top earlier-stage companies (Uber, Lyft, Spotify, Stripe, etc.).

Here is a list of excellent ML use cases to check out (credit to Chip
Huyen’s [<u>ML Systems Design Lecture 2
Note</u>](https://docs.google.com/document/d/15vCMf7SbDuxST9Q-rWtx8o7qHJQN2pE5urCDFTYI1zs/edit?usp=sharing)):

-   [<u>Human-Centric Machine Learning Infrastructure at
 Netflix</u>](https://www.youtube.com/watch?v=XV5VGddmP24) (Ville
 Tuulos, InfoQ 2019)

-   [<u>2020 state of enterprise machine
 learning</u>](https://algorithmia.com/state-of-ml)
 (Algorithmia, 2020)

-   [<u>Using Machine Learning to Predict Value of Homes On
 Airbnb</u>](https://medium.com/airbnb-engineering/using-machine-learning-to-predict-value-of-homes-on-airbnb-9272d3d4739d)
 (Robert Chang, Airbnb Engineering & Data Science, 2017)

-   [<u>Using Machine Learning to Improve Streaming Quality at
 Netflix</u>](https://medium.com/netflix-techblog/using-machine-learning-to-improve-streaming-quality-at-netflix-9651263ef09f)
 (Chaitanya Ekanadham, Netflix Technology Blog, 2018)

-   [<u>150 Successful Machine Learning Models: 6 Lessons Learned at
 Booking.com</u>](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)
 (Bernardi et al., KDD, 2019)

-   [<u>How we grew from 0 to 4 million women on our fashion app, with a
 vertical machine learning
 approach</u>](https://medium.com/hackernoon/how-we-grew-from-0-to-4-million-women-on-our-fashion-app-with-a-vertical-machine-learning-approach-f8b7fc0a89d7)
 (Gabriel Aldamiz, HackerNoon, 2018)

-   [<u>Machine Learning-Powered Search Ranking of Airbnb
 Experiences</u>](https://medium.com/airbnb-engineering/machine-learning-powered-search-ranking-of-airbnb-experiences-110b4b1a0789)
 (Mihajlo Grbovic, Airbnb Engineering & Data Science, 2019)

-   [<u>From shallow to deep learning in
 fraud</u>](https://eng.lyft.com/from-shallow-to-deep-learning-in-fraud-9dafcbcef743)
 (Hao Yi Ong, Lyft Engineering, 2018)

-   [<u>Space, Time and
 Groceries</u>](https://tech.instacart.com/space-time-and-groceries-a315925acf3a)
 (Jeremy Stanley, Tech at Instacart, 2017)

-   [<u>Creating a Modern OCR Pipeline Using Computer Vision and Deep
 Learning</u>](https://dropbox.tech/machine-learning/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning)
 (Brad Neuberg, Dropbox Engineering, 2017)

-   [<u>Scaling Machine Learning at Uber with
 Michelangelo</u>](https://eng.uber.com/scaling-michelangelo/)
 (Jeremy Hermann and Mike Del Balso, Uber Engineering, 2019)

-   [<u>Spotify’s Discover Weekly: How machine learning finds your new
 music</u>](https://hackernoon.com/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe)
 (Sophia Ciocca, 2017)

#### High Feasibility

The three primary cost drivers of ML projects in order of importance are
data availability, accuracy requirement, and problem difficulty.

<img src="/spring2021/lecture-5-notes-media/image6.png" style="width:6.5in;height:3.02778in" />

#### Data Availability

Here are the questions you need to ask concerning the data availability:

-   How hard is it to acquire data?

-   How expensive is data labeling?

-   How much data will be needed?

-   How stable is the data?

-   What are the data security requirements?

#### Accuracy Requirement

Here are the questions you need to ask concerning the accuracy
requirement:

-   How costly are wrong predictions?

-   How frequently does the system need to be right to be useful?

-   What are the ethical implications?

It is worth noting that ML project **costs tend to scale
super-linearly** in the accuracy requirement. The fundamental reason is
that you typically need a lot more data and more high-quality labels to
achieve high accuracy numbers.

#### Problem Difficulty

Here are the questions you need to ask concerning the problem
difficulty:

-   Is the problem well-defined?

-   Is there good published work on similar problems?

-   What are the computing requirements?

-   Can a human do it?

So what’s still hard in machine learning? As a caveat, it’s historically
very challenging to predict what types of problems will be difficult for
ML to solve in the future. But generally speaking, both **unsupervised
learning** and **reinforcement learning** are still hard, even though
they show promise in limited domains where tons of data and compute are
available.

Zooming into **supervised learning**, here are three types of hard
problems:

-   *Output is complex:* These are problems where the output is
 high-dimensional or ambiguous. Examples include 3D reconstruction,
 video prediction, dialog systems, open-ended recommendation
 systems, etc.

-   *Reliability is required:* These are problems where high precision
 and robustness are required. Examples include systems that can
 fail safely in out-of-distribution scenarios, is robust to
 adversarial attacks, or needs to tackle highly precise tasks.

-   *Generalization is required:* These are problems with
 out-of-distribution data or in the domains of reasoning, planning,
 and causality. Examples include any systems for self-driving
 vehicles or any systems that deal with small data.

Finally, this is a nice checklist for you to run an ML feasibility
assessment:

-   Are you sure that you need ML at all?

-   Put in the work upfront to define success criteria with all of the
 stakeholders.

-   Consider the ethics of using ML.

-   Do a literature review.

-   Try to build a labeled benchmark dataset rapidly.

-   Build a minimal viable product with manual rules

-   Are you “really sure” that you need ML at all?

### 4 - Archetypes

So far, we’ve talked about the lifecycle and the impact of all machine
learning projects. Ultimately, we generally want these projects, or
applications of machine learning, to be useful for products. As we
consider how ML can be applied in products, it’s helpful to note that
there are common machine learning product **archetypes** or recurrent
patterns through which machine learning is applied to products. You can
think of these as “mental models” you can use to assess your project and
easily prioritize the needed resources.

There are three common archetypes in machine learning projects:
**Software 2.0**, **Human-in-the-loop**, and **autonomous systems**.
They are shown in the table below, along with common examples and
questions. We’ll dive deeper into each.

<table>
<thead>
<tr class="header">
<th><strong>Archetype</strong></th>
<th><strong>Examples</strong></th>
<th><strong>Questions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Software 2.0</td>
<td><p>- Improve code completion in IDE</p>
<p>- Build customized recommendation system</p>
<p>- Build a better video game AI</p></td>
<td><p>- Do your models truly improve performance?</p>
<p>- Does performance improvement generate business value?</p>
<p>- Do performance improvements lead to a data flywheel?</p></td>
</tr>
<tr class="even">
<td>Human-in-the-loop</td>
<td><p>- Turn sketches into slides</p>
<p>- Email auto-completion</p>
<p>- Help radiologists do job faster</p></td>
<td><p>- How good does the system need to be to be useful?</p>
<p>- How can you collect enough data to make it good?</p></td>
</tr>
<tr class="odd">
<td>Autonomous Systems</td>
<td><p>- Full self-driving</p>
<p>- Automated customer support</p>
<p>- Automated website design</p></td>
<td><p>- What is an acceptable failure rate for the system?</p>
<p>- How can you guarantee that it won’t exceed the failure rate?</p>
<p>- How inexpensively can you label data from the system?</p></td>
</tr>
</tbody>
</table>

### Software 2.0

Software 2.0, which we previously alluded to from [<u>the Karpathy
article</u>](https://medium.com/@karpathy/software-2-0-a64152b37c35), is
defined as “**augmenting existing rules-based or deterministic software
with machine learning, a probabilistic approach**.” Examples of this are
taking a code completer in an IDE and improving the experience for the
user by adding an ML component. Rather than suggesting a command based
solely on the leading characters the programmer has written, you might
add a model that suggests commands based on previous commands the
programmer has written.

As you build a software 2.0 project, strongly consider the concept of
the **data flywheel**. For certain ML projects, as you improve your
model, your product will get better and more users will engage with the
product, thereby generating more data for the model to get even better.
It’s a classic virtuous cycle and truly the gold standard for ML
projects.

<img src="/spring2021/lecture-5-notes-media/image3.png" style="width:4.51563in;height:3.33806in" />

In embarking on creating a data flywheel, critically consider where the
model could fail in relation to your product. For example, do more users
lead to collecting more data that is useful for improving your model? An
actual system needs to be set up to capture this data and ensure that
it's meaningful for the ML lifecycle. Furthermore, consider whether more
data will lead to a better model (your job as an ML practitioner) or
whether a better model and better predictions will actually lead to
making the product better. Ideally, you should have a quantitative
assessment of what makes your product “better” and map model improvement
to it.

#### Human-in-the-Loop (HIL)

HIL systems are defined as **machine learning systems where the output
of your model will be reviewed by a human before being executed in the
real world**. For example, consider translating sketches into slides. An
ML algorithm can take a sketch’s input and suggest to a user a
particular slide design. Every output of the ML model is considered and
executed upon by a human, who ultimately has to decide on the slide’s
design.

#### Autonomous Systems

Autonomous systems are defined as **machine learning systems where the
system itself makes decisions or engages in outputs that are almost
never reviewed by a human**. Canonically, consider the self-driving car!

#### Feasibility

<img src="/spring2021/lecture-5-notes-media/image7.png" style="width:6.5in;height:3.97222in" />

Let’s discuss how the product archetypes relate back to project
**priority.** In terms of feasibility and impact, the two axes on which
we consider priority, software 2.0 tends to have high feasibility but
potentially low impact. The existing system is often being optimized
rather than wholly replaced. However, this status with respect to
priority is not static by any means. Building a data flywheel into your
software 2.0 project can improve your product’s impact by improving the
model’s performance on the task and future ones.

In the case of human-in-the-loop systems, their feasibility and impact
sit squarely in between autonomous systems and software 2.0. HIL
systems, in particular, can benefit disproportionately in their
feasibility and impact from effective product design, which naturally
takes into account how humans interact with technology and can mitigate
risks for machine learning model behavior. Consider how the Facebook
photo tagging algorithm is implemented. Rather than tagging the user
itself, the algorithm frequently asks the user to tag themselves. This
effective product design allows the model to perform more effectively in
the user’s eye and reduces the impact of false classifications.
[<u>Grammarly</u>](https://www.grammarly.com/) similarly solicits user
input as part of its product design through offering explanations.
Finally, recommender systems also implement this idea. In general,
**good product design can smooth the rough edges of ML** (check out the
concept of [<u>designing collaborative
AI</u>](https://medium.com/@Ben_Reinhardt/designing-collaborative-ai-5c1e8dbc8810)).

There are industry-leading resources that can help you merge product
design and ML. [<u>Apple’s ML product design
guidelines</u>](https://developer.apple.com/design/human-interface-guidelines/machine-learning/overview/introduction/)
suggest three key questions to anyone seeking to put ML into a product:

1.  What role does ML play in your product?

2.  How can you learn from your users?

3.  How should your app handle mistakes?

Associated with each question is a set of design paradigms that help
address the answers to each question. There are similarly great
resources from
[<u>Microsoft</u>](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/)
and
[<u>Spotify</u>](https://spotify.design/article/three-principles-for-designing-ml-powered-products).

Finally, autonomous systems can see their priority improved by improving
their feasibility. Specifically, you can add humans in the loop or
reduce the system’s natural autonomy to improve its feasibility. In the
case of self-driving cars, many companies add safety drivers as
guardrails to improve autonomous systems. In
[<u>Voyage</u>](https://voyage.auto/)’s case, they take a more dramatic
approach of constraining the problem for the autonomous system: they
only run self-driving cars in senior living communities, a narrow subset
of the broader self-driving problem.

### 5 - Metrics

So far, we’ve talked about the overall ideas around picking projects and
structuring them based on their archetypes and the specific
considerations that go into them. Now, we’ll shift gears and be a little
more tactical to focus on metrics and baselines, which will help you
execute projects more effectively.

#### Choosing a Metric

**Metrics help us evaluate models**. There’s a delicate balance between
the real world (which is always messy and multifaceted) and the machine
learning paradigm (which optimizes a single metric) in choosing a
metric. In practical production settings, we often care about multiple
dimensions of performance (i.e., accuracy, speed, cost, etc.). The
challenge is to reconcile all the possible evaluation methods with the
reality that ML systems work best at optimizing a single number. How can
we balance these competing needs in building an ML product?

As you start evaluating models, **choose a single metric to focus on
first**, such as precision, accuracy, recall, etc. This can serve as an
effective first filter of performance. Subsequently, you can put
together a formula that combines all the metrics you care about. Note
that it’s important to be flexible and regularly update this formula as
your models or the requirements for the product change.

#### Combining Metrics

Two simple ways of combining metrics into a formula are **averaging**
and **thresholding**.

Averaging is less common but easy and intuitive; you can just take a
simple average or a weighted average of the model’s metrics and pick the
highest average.

More practically, you can apply a threshold evaluation to the model’s
metrics. In this method, out of n evaluation metrics, you threshold n-1
and optimize the nth metric. For example, if we look at a model’s
precision, memory requirement, and cost to train, we might threshold the
memory requirement (no more than X MB) and the cost (no more than $X)
and optimize precision (as high as possible). As you choose which
metrics to threshold and what to set their threshold values to, make
sure to consider domain-specific needs and the actual values of the
metrics (how good/bad they might be).

<img src="/spring2021/lecture-5-notes-media/image5.png" style="width:6.5in;height:3.43056in" />

### 6 - Baselines

In any product development process, setting expectations properly is
vital. For machine learning products, **baselines help us set
expectations for how well our model will perform**. In particular,
baselines set a useful lower bound for our model’s performance. What’s
the minimum expectation we should have for a model’s performance? The
better defined and clear the baseline is, the more useful it is for
setting the right expectations. Examples of baselines are human
performance on a similar task, state-of-the-art models, or even simple
heuristics.

Baselines are especially important for helping decide the next steps.
Consider the example below of two models with the same loss curve but
differing performance with respect to the baseline. Clearly, they
require different action items! As seen below, on the left, where we are
starting to approach or exceed the baseline, we need to be mindful of
overfitting and perhaps incorporate regularization of some sort. On the
right, where the baseline hugely exceeds our model’s performance, we
clearly have a lot of work to do to improve the model and address its
underfitting.

<img src="/spring2021/lecture-5-notes-media/image1.png" style="width:6.5in;height:2.22222in" />

There are a number of sources to help us define useful baselines.
Broadly speaking, there are **external baselines** (baselines defined by
others) or **internal baselines** you can define yourself. With internal
baselines, in particular, you don’t need anything too complicated, or
even something with ML! Simple tests like averaging across your dataset
can help you understand if your model is achieving meaningful
performance. If your model can’t exceed a simple baseline like this, you
might need to really re-evaluate the model.

Human baselines are a particularly powerful form of baseline since we
often seek to replace or augment human actions. In creating these
baselines, note that there’s usually an inverse relationship between the
quality of the baseline and the ease of data collection. In a nutshell,
**the harder it is to get a human baseline, the better and more useful
it probably is**.

<img src="/spring2021/lecture-5-notes-media/image8.png" style="width:6.5in;height:3.26389in" />

For example, a Mechanical Turk-created baseline is easy to generate
nowadays, but the quality might be hit or miss because of the variance
in annotators. However, trained, specialized annotators can be hard to
acquire, but the specificity of their knowledge translates into a great
baseline. Choosing where to situate your baseline on this range, from
low quality/easy to high quality/hard, depends on the domain.
Concentrating data collection strategically, ideally in classes where
the model is least performant, is a simple way of improving the quality
of the baseline.

### TLDR

1.  Machine learning projects are iterative. Deploy something fast to
 begin the cycle.

2.  Choose projects with high impact and low cost of wrong predictions.

3.  The secret sauce to make projects work well is to build automated
 data flywheels.

4.  In the real world, you care about many things, but you should always
 have just one to work on.

5.  Good baselines help you invest your effort the right way.

### Further Resources

-   Andrew Ng’s “[<u>Machine Learning
 Yearning</u>](https://d2wvfoqc9gyqzf.cloudfront.net/content/uploads/2018/09/Ng-MLY01-13.pdf)”

-   Andrej Kaparthy’s “[<u>Software
 2.0</u>](https://medium.com/@karpathy/software-2-0-a64152b37c35)”

-   Agrawal, Gans, and Goldfarb’s “[<u>The Economics of
 AI</u>](https://www.economicsofai.com/)”

-   Chip Huyen’s “[<u>Introduction to Machine Learning Systems
 Design</u>](https://docs.google.com/document/d/15vCMf7SbDuxST9Q-rWtx8o7qHJQN2pE5urCDFTYI1zs/edit?usp=sharing)”

-   Apple’s “[<u>Human-Interface Guidelines for Machine
 Learning</u>](https://developer.apple.com/design/human-interface-guidelines/machine-learning/overview/introduction/)”

-   Google’s “[<u>Rules of Machine
 Learning</u>](https://developers.google.com/machine-learning/guides/rules-of-ml)”
