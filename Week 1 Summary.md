# Week 1 Summary — How AI Actually Works
### AI Fluency: Framework & Foundations | Royce | May 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 2, or whenever you need a refresher.*

---

## Key Concepts

### What is an LLM?
A Large Language Model didn't memorize facts — it learned **patterns**. Trained on an enormous amount of text, it absorbed how ideas connect, how language flows, and how experts reason. When you ask it something, it doesn't look it up — it generates a response by predicting, token by token, what the most useful next word would be.

### Tokens
The unit AI reads and generates — roughly 3–4 characters each. Words get split based on how frequently they appear in training data, using an algorithm called **Byte Pair Encoding (BPE)**. Common words like "the" become a single token. Rare or compound words like "Wealthsimple" might become 3–4 tokens. Spaces are part of the token. This matters for cost (APIs charge per token) and limits (context windows are measured in tokens).

### Context Window
The model's working memory — everything it can "see" at once in a conversation. Think of it as a whiteboard. When it fills up, older content falls off. Modern models like Claude have large context windows, but in long sessions or across sessions, older context can be lost.

### How AI "Thinks" — Probability, Not Rules
AI doesn't follow a rulebook. It makes a series of probabilistic predictions — given everything in context, what's the most useful next token? This is why it can write poetry and debug code using the same mechanism. It's also why it **hallucinates** — sometimes the statistically likely next token is confidently wrong, and the model has no internal fact-checker.

### Hallucination
When AI generates something incorrect with full confidence. It's not lying — it genuinely can't distinguish between "I learned this" and "I'm predicting this sounds right." In fintech, this is a critical risk for anything touching real customer data, compliance, or financial advice.

### Temperature
A setting that controls how creative vs. predictable the AI's outputs are. High temperature = more varied, surprising responses. Low temperature = more focused, consistent, precise. Rule of thumb: low temperature for compliance docs, legal text, or structured data. Higher temperature for brainstorming or creative work.

### Inference
The act of the model generating a response — what happens computationally the moment you hit send.

### Tool vs. Agent vs. LLM — The Carpenter Analogy
- **Tool** = the hammer or saw. One capability, one purpose. Examples: web browser, calculator, file reader, API call.
- **Agent** = the carpenter. Has a goal, runs a loop, orchestrates tools, evaluates progress, keeps going until done.
- **LLM** = the brain inside the carpenter. The reasoning engine that decides which tool to use, evaluates results, and determines when the goal is complete.

You choose which LLM powers the agent's reasoning — Claude, GPT-4, Gemini, Llama, etc. Same agent framework, swappable brain.

### What AI Is Great At
- Synthesizing large amounts of text (customer feedback, support tickets, research)
- Generating drafts, rewrites, and variations
- Explaining complex concepts in plain language
- Spotting patterns in qualitative data
- Reasoning through structured problems step by step

### Where AI Struggles
- Real-time or recent information (training cutoff date)
- Precise arithmetic and multi-step calculations
- Knowing when it doesn't know something — it guesses confidently
- Consistent memory across very long interactions
- High-stakes decisions without human review

---

## PM Takeaways

> **On tokens and cost:** When building AI products, your unit economics are cost-per-token. Multilingual features cost more — French text tokenizes less efficiently than English in an English-trained model because the model has less pattern compression for it.

> **On capability mapping:** The most important question when evaluating an AI feature isn't "can AI do this?" — it's "what happens when AI gets this wrong, and how bad is that?" Your answer determines whether you need human review, confidence thresholds, fallback logic, or whether you can just ship.

> **On real-time data:** When scoping a feature that needs live information, you're not asking "can the LLM know this?" You're asking "what tool or data source does the agent need access to?" Those are different product and engineering questions.

> **On context window loss:** Context window management is a real product constraint. For multi-session features (like a financial planning tool), you need to design what gets persisted externally vs. what lives in active context. This is called memory architecture.

> **On temperature:** "Which temperature should we use?" is a legitimate product decision. It affects the consistency and predictability of your AI feature's outputs — and for high-stakes content like compliance disclosures, low temperature is non-negotiable.

> **On model selection:** "Which LLM should power this feature?" is a PM decision, not just an engineering one. Tradeoffs include cost, reasoning quality, latency, context window size, data privacy, and vendor risk.

> **On risk decomposition:** A single product risk often contains multiple distinct failure modes with different solutions. Example: "AI shows wrong account info" actually contains two separate risks — stale data (solved by real-time tool access) and arithmetic errors (solved by routing calculations to a calculator tool, not the LLM).

---

## Questions You Asked — and What They Revealed

**"What patterns can be seen from tokens?"**
Tokens get converted into vectors — lists of numbers representing meaning across hundreds of dimensions. Similar concepts live close together in this space. The model learned all of this purely from patterns of co-occurrence in training data. Your color analogy (blue for one meaning, red for another) was the right intuition.

**"How are words tokenized?"**
Using Byte Pair Encoding (BPE) — start with individual characters, repeatedly merge the most frequent pairs until you reach a target vocabulary size. Common sequences get compressed into single tokens. Rare ones stay fragmented. Nobody manually designed the vocabulary — it emerged from the data.

**"Is tokenizing characters somewhat random? Nobody designed it like that?"**
Not random — deliberately designed via BPE, but optimized by data rather than by a human linguist. The stenographer analogy: shorthand symbols aren't arbitrary, they're assigned to the most common sounds for efficiency. Same logic.

**"What is the difference between an agent and a tool?"**
A tool is a single capability (a verb — search, calculate, read). An agent is a system that orchestrates capabilities toward a goal. The decision-making layer is what makes something an agent.

**"Is the LLM the brain inside the carpenter? And we get to choose which LLM runs the agent's logic?"**
Exactly right. The LLM is the reasoning engine inside the agent. You choose which model powers it. This is a real product and engineering decision with cost, quality, and latency tradeoffs.

**"If an AI has internet access, is it real-time?"**
Only if it's agentic. The LLM itself still has a knowledge cutoff. An agent with a browser tool retrieves live information and passes it to the LLM to reason about. The intelligence and the information access are separate layers.

**"How do I know when context is being lost?"**
Warning signs: AI contradicts earlier statements, forgets constraints you set, gives generic answers that should reference prior conversation, requires you to re-explain things. For this course, weekly fresh chats + memory files + weekly summaries protect against this.

---

## Exercise 1 — Misconception Audit: Feedback

**Misconception 1 (Confidence as a builder):** Valid mindset shift, but the stronger framing is conceptual: building with AI is closer to product thinking than deep engineering — you're orchestrating tools around an LLM brain, not inventing from scratch.

**Misconception 2 (LLMs learn and understand):** Your strongest answer. Correctly identified pattern recognition over memorization, tokenization as the mechanism, and multilingual token efficiency. Note: whether LLMs truly "understand" is an active philosophical debate in AI — worth knowing it exists.

**Misconception 3 (Agents are impossible to build):** Right feeling, needs more substance. What specifically changed? You now know agents have three layers — system/goal (carpenter), reasoning (LLM brain), capabilities (tools) — and building one means connecting those layers, not inventing something from scratch.

---

## Quiz Results — 5.5 / 6

| Q | Topic | Result | Note |
|---|-------|--------|------|
| 1 | LLM generation mechanism | ✓✓ | Perfect |
| 2 | Real-time + agentic distinction | ✓✓ | Excellent synthesis |
| 3 | Tool / Agent / LLM | ✓✓ | Strong; LLM decides throughout loop, not just at end |
| 4 | Temperature for compliance | ✓✓ | PM framing was excellent |
| 5 | Wealthsimple risks | ✓ | Risk 1 bundled two separate risks — stale data vs. arithmetic errors |
| 6 | French tokenization cost | ✓✓ | Excellent; correct mental model |

**Standout quality:** You consistently connected concepts back to how they'd be solved or applied, not just what they are. That's PM thinking showing up naturally.

**One gap to carry into Week 2:** Always ask whether a single "risk" contains multiple distinct failure modes with different solutions. Precision matters in product specs.

---
---

# PART 2 — Session Handoff

*For Claude at the start of Week 2. Read this before beginning the lesson.*

---

## Course Status
- **Week 1:** Complete ✓
- **Week 2:** Prompt Engineering — The PM's Superpower (ready to begin)
- **Syllabus file:** `AI Fluency Course — Royce's Syllabus.md` in workspace folder

## What Was Covered in Week 1
Full lesson on How AI Actually Works, delivered in 4 parts (one section at a time per Royce's preference):
- Part 1: What is an LLM — pattern recognition, not memorization
- Part 2: Tokens, context windows, BPE, probability-based generation
- Part 3: AI capability map — strengths and weaknesses, Wealthsimple scenarios
- Part 4: Vocabulary table + Exercise 1 (Misconception Audit)
- End-of-week quiz: 6 questions across multiple formats

## What Landed Well
- The whiteboard analogy for context windows — Royce explicitly called it out as excellent
- The carpenter/hammer/brain analogy for tool/agent/LLM distinction — became a running framework
- PM Takeaway sections at the end of key concepts — Royce requested these be included in summaries
- Business and fintech framing throughout (Wealthsimple scenarios)
- One-section-at-a-time delivery — Royce requested this mid-lesson and it improved engagement significantly

## Royce's Learning Profile (relevant to Week 2)
- Business background, basic SQL, no Python yet
- Strong at synthesis and connecting concepts to application
- Responds best to: analogy-first explanations, PM-framed "so what?" takeaways, concrete fintech examples
- Asks genuinely sharp questions — treat him as an engaged learner, not a passive one
- Wants honest feedback, not encouragement for its own sake

## Gaps / Things to Watch
- Tendency to bundle multiple distinct risks into one when doing product analysis — worth reinforcing the habit of decomposing failure modes in Week 2 exercises
- Misconception audit answers leaned toward mindset shifts over conceptual articulation — gently push for more substance when this comes up

## Teaching Workflow (must follow)
- One section at a time — ask if Royce is ready before printing the next part
- Include a PM Takeaway callout for key concepts
- End with a test (mixed question types) before writing the summary
- Ask before making any major changes to course structure or files

## Week 2 Setup Notes
- Prompt Engineering connects directly to Royce's existing AI usage — frame it as upgrading a skill he already has, not learning from scratch
- The Golden Template from the syllabus (Role + Context + Task + Format + Constraints) should be the spine of the lesson
- Good exercise: have Royce rewrite a vague prompt 3 times with progressively better structure, then compare outputs
- Fintech angle: prompt engineering for PM tasks at a company like Wealthsimple (writing user stories, competitive analysis, stakeholder updates)
