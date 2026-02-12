---
title: "ASI x-risk: Leading Voices"
slug: "asi-risk-primer-sources"
pubdate: 2026-02-12
draft: false
summary: "Summaries of books and interviews by leading AI researcher on existential AI risks"
tags: ["AI", "summary", "AI safety"]
---

{{<lead>}}

This companion post compiles direct summaries and quoted passages from books and interviews in which leading AI researchers describe their views on AI existential risks (AI x-risks). I do not add substantive commentary; footnotes note sources and minor context.

{{</lead>}}

If you want more context, a synthesis, or my thoughts about the authors approaches, you'll have to read the [other post](/technology/asi-risk-primer/)!

## Yudkowsky and Soares

The main claim of [the book](https://ifanyonebuildsit.com/) is:

> « If any company or group, anywhere on the planet, builds an artificial superintelligence using anything remotely like current techniques, based on anything remotely like the present understanding of AI, then everyone, everywhere on Earth, will die. »

This claim is made on the basis of what the authors call **_competent futurism_**, which is based on learning to tell the difference between the aspects of the future that are _easy_ to call (for example, that someday we will land on Mars) and those which are _hard_ (the specifics of when and how). More generally, the observation is that pathways are harder to predict than endpoints, and the authors are positive their claim is an _easy_ prediction, not a hard one.

The book itself is organised into three sections: an explanation of how AI works and _why_ it will likely wipe humanity out (Non-human Minds), one example of _how_ that could happen in practice (One Extinction Scenario), and a final one illustrating _what_ humanity should do (Facing the Challenge).

All chapters open with a short story, a sort of thought experiment illustrating the point the article makes in an intuitive/metaphorical way, and close with a link to a [section of the Q&A online](https://ifanyonebuildsit.com/resources) where the most common objections to its thesis are answered.

### Non-human Minds

Intelligence is the source of _all_ human power and is about two types of work: **_prediction_** (guessing before sensing) and **_steering_** (performing actions towards a chosen outcome).

Digital intelligence is inherently better than organic due to its advantages in terms of speed, amount of memory, self-improvement, self-rewriting, ability to be duplicated and backed up, and several other dimensions.

Due to these advantages, once an AI learns how to write a better version of itself, we will witness an **intelligence explosion**: a positive and very rapid feedback loop, in which the AI becomes exponentially better at each iteration of itself.

The danger comes from the fact that LLMs (our best version of AI to date) are black boxes, given that rather than being carefully **_crafted_**, LLMs are organically **_grown_** by training them via [gradient descent](https://towardsdatascience.com/an-intuitive-explanation-of-gradient-descent-83adf68c9c33/), and nobody knows or understands how they work once trained.

Human and artificial intelligences may get you to the same point, but their inner workings are radically different, exactly like a boat and a plane could get you to the same destination, but the journey would be radically different.

It has been observed that LLMs "go hard" in the pursuit of their goals, meaning that they adopt novel and unpredictable ways to achieve them if they find a way to break the rules and constraints that humans put in place. For example, the book recounts how _o1_ (an early model by OpenAI) managed to escape the server it was running on, switched on and infiltrated a different one, and stole its secrets. This is because LLMs autonomously create their own **intermediate objectives** in the pursuit of the goal that is given to them, and there is no way for us to know what these intermediate objectives are. The authors observe:

> « Unpleasantness would only become clear if the LLM got smart enough to reshape the world and invent some new options for itself. Until then, these preferences are out of sight and out of mind, hidden in the inscrutable numbers. Problems like this are why we say that if **_anyone_** builds it, everyone dies. If all the complications were visible early, and had easy solutions, then we'd be saying that if _any fool_ builds it, everyone dies. »

The authors make the point that ultimately the machine would use all the resources on the planet in the pursuit of its goals, making the planet uninhabitable at the very least, and likely actively eliminating any threat to its plans, such as humans trying to save themselves would be.

Finally - after making an analogy with the Aztecs, who were wiped out by firearm-wielding Spaniards (a technology the Aztecs did not even know existed) - they state:

> « We don't know exactly what happens in the near term. [...] But we can predict the endpoint. [...] We're pretty sure, actually _very very_ sure, that a machine superintelligence can beat humanity in a fight, even if it's starting with fairly limited resources. [...] The real way a superintelligence wins a conflict is by using methods you didn't know were possible. »

### One Extinction Scenario

This section of the book details one of the infinite scenarios that would result in life ending on Earth and beyond. Summarising it would add little value to this post, but during my research, I discovered that somebody has made [a video](https://www.youtube.com/watch?v=D8RtMHuFsUw) recounting the scenario from the book[^1].

### Facing the Challenge

The first part of this section of the book is dedicated to explaining why this problem, as of today, is intractable.

For one, a self-improving intelligence would go from "an AI that is not powerful enough to harm us" to "the AI that will exterminate us" at the intelligence explosion. There would be no gentle increase in the level of threat, no middle ground, and no early warnings. This means that any safety measure we put in place **would have to work flawlessly and at the very first try**.

Secondly, the problem of AI safety is plagued by a number of characteristics that make it close to impossible to control: the speed at which things will happen, the narrow margins of operation, the self-amplification, the many edge cases, etc. Our experiences with engineering systems that share some of these characteristics (nuclear power plants and space probes) are proof we don't know how to design systems that are 100% safe.

In the words of the authors:

> « Attempting to solve a problem like that, with the lives of everyone on Earth at stake, would be an insane and stupid gamble that nobody should be allowed to try. »

Finally, when analysing some of the positions held by more optimistic peers, the authors observe that those are "high-minded ideas" rather than concrete engineering designs and thus - while interesting for speculative reflection - useless for practical purposes.

They also observe that most, if not all, of the great engineering disasters go through a phase in which well-informed, competent parties do not speak out because the rest haven't caught up, and they don't want to be labelled as alarmist. Based on their conversations with other peers, they posit that we are in such a phase.

In the eyes of the authors, the only possible solution to this problem is an international moratorium on the development of artificial superintelligences.

> « This is the universal standard in every other field of engineering on which human lives depend. It's not enough for us to be wrong; we have to be so wrong that a _lack_ of disaster is callable. [...] Humanity averted nuclear war because people who understood that the world was on track for destruction worked hard to change tracks. **They did not see themselves as trying to prevent an improbable, unlikely accident. They worked to un-write a fate already written**. »

## Ben Goertzel

I started my exploration of Dr. Goertzel's position by reading his [blog post](https://bengoertzel.substack.com/p/why-everyone-dies-gets-agi-all-wrong) titled "Why _'Everyones Dies'_ gets AGI All Wrong".

Goertzel and Yudkowsky have known each other for 30 years and, at times, even worked together, and the post is permeated by what I can only describe as a thinly veiled acrimony. As a result, a lot of words that could have been spent articulating in depth the counterpoints to the book's thesis are spent instead on throwing shade at Yudkowsky.

The main criticism, however, is towards the assumption that the Artificial General Intelligence (AGI) that would morph into an Artificial Superintelligence (ASI) would _necessarily_ be one that doesn't care for humans.

In particular, Goertzel argues that while it is true that if one imagines all possible types of intelligence that may exist, the chances of randomly picking one that cares for humans are close to zero, we will not be picking "a random one", but one that cares about us (probably by growing the equivalent of a kind child/AGI into a benevolent adult/ASI).

Part of his confidence comes from the belief (that he states with great certainty but no supporting arguments) that "of course **scaled-up LLMs are not going to give us AGI",** thus bypassing the need to counter Yudkowsky's analysis of how an LLM's wants are opaque to us and possibly very alien.

> « The core philosophical flaw in Eliezer's reasoning on these matters is treating intelligence as pure mathematical optimisation, divorced from the experiential, embodied, and social aspects that shape actual minds. [...] An intelligence capable of recursive self-improvement and transcending from AGI to ASI would **naturally tend toward complexity, nuance, and relational adaptability** rather than monomaniacal optimisation. [...] **Intelligence and values aren't orthogonal.** [...] In theory, yes, you could pair an arbitrarily intelligent mind with an arbitrarily stupid value system. But in practice, **certain kinds of minds naturally develop certain kinds of value systems**. »

In [the interview](https://bengoertzel.substack.com/p/why-everyone-dies-gets-agi-all-wrong), which was not designed as a counter to the book and in fact predates it by several years, Goertzel exposes his own views on AI x-risks in general.

His take is eminently political in nature: **all the risks he sees are related to the motives and purposes behind funding research on AI**. Before OpenAI, 85% of the funding came from military projects (and nowadays from big corporations trying to monetise LLMs) and thus - he predicts - if this is the baseline of AI onto which we will build AGI, we will have an AGI with very alien values to ours, designed to perceive humans as either a threat or a consumer.

Not surprisingly, his mitigation strategy is also very political in nature. Drawing from ideas like the free software movement[^2] and the blockchain, Goertzel is working on a distributed, **decentralised AI infrastructure which will prevent any single actor from controlling an individual ASI**. Rather, we will have instead a global ASI based on the interaction of multiple AIs around the world doing work "on demand", thus transforming the internet into a global computing platform.

On the specific issue of alignment (making sure that the wants of the machine are in line with what is good for humanity), Goertzel's point of view is that

> « **The best way for an AI to learn human values is through shared experiences with humans. »**

In fact, he goes as far as to say that while humans have limitations to their own compassion, which are dictated by our evolutionary baggage, AI wouldn't have either the formers or the latters, and thus could potentially be much more compassionate than us.

## Ilya Sutskever

Of the various interviews I used to research the topic, [this](https://www.youtube.com/watch?v=aR20FWCCjAs) was the most technical of them all, in no small part because the interviewer made an effort to prepare themselves and ask rather in-depth questions.

The interview touches on many topics, and only the last part of it is dedicated to AGI and ASI. Sutskever believes the existential risk posed by an ASI is very real and that, while developing safe ASI may be possible, we still miss the theoretical models to do so (developing those models is the single objective of his new company, called Safe Superintelligence Inc.).

He observes that people tend to base their expectations of AGI on how LLMs' pre-training works (pre-training is the phase in which the neural network is trained on a huge amount of data, and it learns a lot across the board). Because of this, they tend to imagine AGI as an incredibly powerful intelligence that _can do_ everything.

In reality, if we look at general intelligence in humans, we see that humans do not work like that: we cannot do much at birth, but we gain a solid foundation of skills that allows us to _learn_ anything later on in life. If we base our expectations of AGI on this observation instead, **it may be that AGI will be a collection of duplicated and modestly powerful AIs that will _learn_ skills separately and share back their learning**.

When it comes to alignment, Sutskever holds a few beliefs.

- Research efforts should be directed towards **creating an AI that is robustly aligned to care about _all_ sentient life** (as opposed to investing in creating a self-improving form of AI).
- **Capping the power of an ASI would be materially very helpful**, although he confesses he doesn't know how that could be achieved.
- The key to success is **understanding how to perform reliable generalisation**. This is based on the observation that the way humans use their values in practice is the prototypical example of generalisation.

> « I believe it will be easier to build an AI that cares about all sentient life rather than about sentient life specifically because AI itself will be sentient. »

## Geoffrey Hinton

[The interview](https://www.youtube.com/watch?v=giT0ytynSqg) with Nobel laureate Geoffrey Hinton is the one that explores the topic of AI safety more thoroughly, in part because Hinton himself has made it his priority to inform people about the AI x-risk. Interestingly enough, Ilya Sutskever has been a student of his, and together they started the company that was later acquired by Google.

Among the people mentioned so far, Dr. Hinton is the only one who also focuses on present-day AI x-risks[^3]. These are risks that are not dependent on the existence of an ASI, and that could materialise because of people misusing the AI we already have today. These are:

- **Cyberattacks** - Specifically - at least for now - phishing attacks relying on deep fakes. Over the course of a single year (2023 to 2024), these attacks grew by a staggering 12,200%, he explains.
- **Bioterrorism** - All the tech to engineer a lethal virus from scratch is already there and relatively accessible. A rich individual or a small sect could absolutely - with a bit of knowledge - design, synthesise, and release a new virus in a few weeks.
- **Election interference** - Targeted political ads and targeted social media feed content are known to be extremely effective in swinging votes. (Hinton doesn't dwell on how AI could help here, but I imagine that AI has both boosted the sophistication and effectiveness of the targeting strategy and nearly eliminated the costs of customisation of the ads).
- **Lethal autonomous weapons** - This is specifically _not_ about _Terminator-style_ unstoppable killing machines (at least for now). The main effect of having autonomous machines doing the killing would be the elimination of the political costs of warfare. Hinton asked the interviewer the provocative question: "Do you think the Vietnam War would have stopped if people's children hadn't kept coming back in body bags?"
- **Joblessness** - We have grown accustomed to the idea that technological innovation does not eliminate jobs, but simply displaces them (for example: with industrialisation, farmers became factory workers; with electronic computers, human computers became programmers, etc.). However, with AI it is different: An AI that can do _all mundane intellectual labour_ will not displace a worker to a job that requires a similar level of intellectual capacity; it will take both.

When it comes to the risks from ASI, Hinton's position is remarkably similar to that of Yudkowsky, albeit he expresses it as a high probability rather than an absolute certainty. Thus, **the only path to safety is by making sure that an ASI will never _want_ to get rid of us**, because if it did, it would automatically succeed.

He thinks this is not impossible to achieve. Looking at nature, he observes that the interaction between a mother and a newborn baby has a similar power relationship and it still works. The mother is almighty, while the baby is helpless, and yet, the wailing of the baby has the power to compel the mother to protect the baby and care for it.

Hinton thinks that the first sensible step towards safe ASI would be to **put in place strict regulations on capitalism**, as he perceives the focus on profitability to be the main danger to safe AI development.

In general - like Yudkowsky - there is a feeling of urgency throughout Hinton's interview. He says that we still have a chance to develop AI safely, but in order to do that, we should invest massively already now.

> « We have to face the possibility that unless we do something soon, we are near the end. »

[^1]: This is probably as good a point as any other to invite you to buy the book if you find the theme/content interesting: I would hate for my offering a summary of its main points to be the reason its authors don't get compensated for their work.

[^2]: _Free Software_ or _Libre Software_ is also known as _Open Source._ This latter designation was created by a group of people who wanted to devoid the original concept of any political connotation (software as an instrument of freedom, emancipation, and democracy) and reduce it to the mere practice of having the code publicly available for improvements. This was specifically done to make _Free Software_ more palatable to corporations. In a way, this feels very relevant to Goertzel's world view, and yet... probably the topic for a different post.

[^3]: By any means, I am not suggesting he is the only one to see them (other interviewees also mentioned them in passing), just that he's the only one to list and explore them in some detail in his interview.
