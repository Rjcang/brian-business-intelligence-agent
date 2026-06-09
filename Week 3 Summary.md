# Week 3 Summary — The AI Tools Landscape
### AI Fluency: Framework & Foundations | Royce | May 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 4, or whenever you need a refresher.*

---

## Key Concepts

### The AI Stack — Four Layers (Not "Floors")
In the real world, people say "the AI stack," "layers," or "the model layer / application layer / product layer." The four-floor framework was a teaching tool — here's how to translate it:

| Teaching Term | Industry Term | What Happens Here |
|---|---|---|
| Floor 1 | Model / Infrastructure layer | Foundation models are trained here (Claude, GPT-4, Gemini) |
| Floor 2 | Application layer | API integration, system prompts, guardrails — where products are built |
| Floor 3 | Product / Wrapper layer | Pre-built tools aimed at specific workflows (Cursor, Notion AI, Cowork) |
| Floor 4 | Consumer layer | General-purpose chat interfaces (Claude.ai, ChatGPT.com) |

**The PM insight:** When someone says "we build at the application layer on top of GPT-4," they mean Floor 2 — API integration, system prompts, and full control over behavior. No model training, just connecting and configuring.

**The key question at every layer:** Who holds the pen? On Floor 2, you write the system prompt — you are the builder. On Floor 4, Anthropic wrote it — you are the user. Control follows whoever holds the pen.

---

### The Six Categories of AI Tools

| Category | What It Does | PM Relevance |
|---|---|---|
| **Writing & Content** | Draft, edit, rewrite, summarize | Internal productivity — PRDs, stakeholder updates, help docs |
| **Research & Knowledge** | Synthesize sources, answer with citations | Competitive research, market analysis — verify facts, watch for hallucination |
| **Coding** | Write, explain, review, debug code | Helps you speak credibly with engineering; Week 4 feels less scary |
| **Automation & Workflow** | Connect AI to existing tools, trigger actions | No-code automation — route tickets, trigger workflows, no engineering needed |
| **Data Analysis** | Answer questions about data in plain English | Ask "what's driving activation drop?" without writing SQL |
| **Agent Platforms** | Multi-step autonomous workflows that take actions | The frontier — where your final project lives |

---

### The Four PM Evaluation Questions
Apply these to any AI tool, in any category:

1. **What specific problem does it solve?** Not "it uses AI" — what workflow does it replace or improve?
2. **Where does it fail?** Every tool has a failure mode. What's this one's?
3. **Who owns the data?** What happens to what you put into it? Critical in fintech and healthcare.
4. **Does it give you API access?** Can you build on top of it, or are you stuck on their Floor 4?

---

### Build vs. Buy — The Decision Framework

The real decision is almost always **Floor 3 (Buy) vs. Floor 2 (Build on API).**

| | **Buy (Floor 3)** | **Build on API (Floor 2)** |
|---|---|---|
| **Speed** | Days to weeks | Weeks to months |
| **Cost** | Subscription, predictable | Per-token, scales with usage |
| **Control** | Low — their constraints | High — you define everything |
| **Customization** | Limited | Complete |
| **Data privacy** | Their servers, their terms | You control what gets sent |
| **Differentiation** | None — competitors can buy the same | High — your system prompt is your product |

**The question that cuts through it:** *Is this AI behavior a competitive differentiator, or is it table stakes?*
- Table stakes → buy it, move on
- Differentiating → build on the API, own the behavior

**The fintech wrinkle — always ask about data privacy:**
When you use a Floor 3 vendor, customer financial data goes to their servers under their terms. In a regulated industry, that's a legal and compliance question before it's a product question. Can you even send that data to a third party under your user agreements? This must be on your checklist for every fintech build-vs-buy decision — not optional.

**The pragmatic middle path:** Buy while building internal capability. If timeline is tight, ship with a vendor solution, but invest in Floor 2 capability in parallel so you're not permanently locked into someone else's constraints.

---

### Agent vs. Chatbot — The Three Tests

A chatbot answers one question at a time. An agent takes a goal and works toward it across multiple steps.

**The three tests:**
1. **Does it take actions, or just produce text?** Agents call tools, book things, send emails. Chatbots produce words.
2. **Does it run multiple steps, or just one?** Agents plan, execute, evaluate, and decide what's next. Chatbots respond once and wait.
3. **Does it pursue a goal, or answer a question?** "What is X?" is a chatbot question. "Do X for me" is an agent instruction.

**Real example:** A tennis court booking that runs automatically every week passes all three tests — it takes action, runs multiple steps, and pursues a goal. That's an agent, even if it lives inside a Floor 3 platform like Cowork.

**The interview move:** When someone says "we built an AI agent," ask: "Does it take actions autonomously, or does it generate responses for a human to act on?" That question alone signals genuine AI fluency.

---

## PM Takeaways

**On the stack as a PM decision tool:** "Which AI should we use?" is the wrong first question. "Which layer are we building on?" is the right one. That answer drives cost structure, control, time-to-ship, and differentiation.

**On data privacy as a default lens:** In fintech (and healthcare), data privacy is never just a legal department question — it's a PM constraint that shapes your build-vs-buy decision from the start. Whose servers is this data on? Whose terms govern it? Ask this before anything else.

**On arithmetic as a distinct AI risk:** LLMs predict tokens — they don't compute. They pattern-match to what arithmetic *usually looks like*, which works for simple cases but breaks on complex multi-step calculations. Any AI feature involving important numbers (financial scores, risk figures, calculations) should route the math to a proper computation tool and use the LLM only for reasoning and language. The PM gut-check: "What calculations are involved here, and should the LLM be doing them?"

**On system prompts as your differentiator:** A competitor using the same foundation model gets the same raw capability — but they can't copy your system prompt. Your persona, guardrails, reasoning instructions, and tone live in the system prompt. That's what makes Floor 2 worth building on.

**On agents vs. chatbots in the market:** Most companies are calling chatbots agents in their marketing right now. Being able to spot the difference — and articulate it crisply — is a genuine signal of AI fluency in interviews.

---

## Questions Royce Asked (with answers)

**"Do people in the industry actually call them floors?"**
No — "floors" was a teaching framework. Real-world terms: "the AI stack," "layers," "model layer," "application layer," "product layer." When someone says "we build at the application layer on top of GPT-4" — that's Floor 2.

**"Would a system prompt be attached to Floor 4 usage too?"**
Yes — but Anthropic wrote it, not you. Every product built on an API has a system prompt. The distinction is who sits in the builder seat. On Floor 4, Anthropic is the builder. On Floor 2, you are. The three-layer model from Week 2 applies everywhere: Anthropic's training → builder's system prompt → user prompt. The builder changes by floor.

**"Isn't using Cowork to book tennis courts autonomously every week an agent?"**
Yes — it passes all three tests. Takes actions (books the court), runs multiple steps, pursues a goal. Cowork is the agent platform (Floor 3). The scheduled booking workflow is the agent running inside it. The tool and the behavior are separate things.

**"What does 'building at the application layer' mean?"**
Floor 2. Infrastructure layer = the raw model. Application layer = where you connect to it via API and build your product on top. Same concept, industry language.

**"Why is arithmetic a general LLM shortfall?"**
LLMs predict the next token — they don't compute. Simple math works because they've seen millions of correct examples in training and can pattern-match well. But complex multi-step calculations drift from the correct answer because the model is producing what arithmetic *looks like*, not actually running the calculation. Fix: route math to a computation tool, use the LLM for reasoning and language only.

---

## Assessment Results

**Score: 7/8**

| Question | Score | Notes |
|---|---|---|
| Q1 — AI Stack (3-part) | 2/2 | All three identifications correct; meta-question about real-world terminology was sharp |
| Q2 — Build vs. Buy | 1.5/2 | Strong framework (timeline, differentiator, budget, roadmap); missing data privacy lens |
| Q3 — Agent vs. Chatbot | 2/2 | Perfect application of all three tests |
| Q4 — Tool Evaluation | 1/1 | Correct primary answer; hallucination noted as close second in healthcare |
| Q5 — Week 2 Connection | 2/2 | Correctly identified system prompt as differentiator; chain-of-thought example was strong |
| Q6 — Week 1 Connection | 1.5/2 | Hallucination + human review correct; temperature callback excellent; missing arithmetic risk |

**Overall:** Best assessment yet. Reasoning quality has leveled up — constructing arguments, not just identifying answers. Two gaps to carry forward: (1) data privacy as a default lens in any fintech build-vs-buy decision, and (2) arithmetic as a distinct AI risk whenever financial calculations are involved.

---

---

# PART 2 — Session Handoff

*For the next session's Claude. Read this before beginning Week 4.*

---

## Course Status
- **Week 1:** Complete ✓ — Score: 5.5/6
- **Week 2:** Complete ✓ — Score: 6.5/8
- **Week 3:** Complete ✓ — Score: 7/8
- **Week 4:** Python for AI (SQL → Python bridge) — ready to begin

## What Was Covered in Week 3
Full lesson on The AI Tools Landscape, delivered in four parts:
- Part 1: The AI Stack — four layers (floors), who holds the pen at each layer
- Part 2: Six categories of AI tools + four PM evaluation questions
- Part 3: Build vs. Buy decision framework — table stakes vs. differentiator, data privacy lens
- Part 4: Agent vs. Chatbot — three tests, real-world examples

## What Landed Well
- The four-floor building analogy — immediately intuitive, Royce used it confidently throughout
- The Wealthsimple walkthrough — grounded every layer in a company he knows
- "Who holds the pen?" as the unifying question across layers
- Agent vs. chatbot three-test framework — Royce applied it independently and correctly to the tennis booking example
- The Floor 3 vs. Floor 4 distinction needed extra clarification (Royce asked for more on Floor 3) — the "someone else's Floor 2 work, packaged for a specific workflow" one-liner resolved it cleanly

## What Was Harder
- Floor 3 vs. Floor 4 distinction — required a follow-up explanation before it clicked
- Data privacy as a fintech lens — Royce's build-vs-buy reasoning was strong but didn't surface this instinctively; worth reinforcing in Week 4 context too
- Arithmetic as a distinct AI risk — missed again (was also a gap in Week 1); this is a pattern worth addressing directly early in Week 4

## Tangents Explored
- Whether "floors" is real industry terminology (answered: no — use "layers," "AI stack," "application layer")
- Whether Floor 4 tools also have system prompts (answered: yes, but Anthropic is the builder, not the user — three-layer model from Week 2 applies everywhere)
- Whether Cowork booking tennis courts is an agent (answered: yes — passes all three tests; platform vs. behavior are separate things)
- Why arithmetic is an LLM shortfall (answered: token prediction vs. actual computation)

## Royce's Trajectory
Scores improving week over week (5.5 → 6.5 → 7). Critical thinking is visibly developing — he's constructing arguments now, not just identifying answers. He flagged a genuine teaching error (asking about APIs without Week 1 covering them) and was direct about it — respond well to that directness, it's a strength. He also asked a meta-question about whether "floors" is real industry terminology, which shows he's thinking beyond the lesson toward actual application.

## Gaps to Carry Into Week 4
- **Arithmetic as distinct AI risk** — has appeared as a gap in both Week 1 and Week 3. Worth naming it explicitly early in Week 4 and building it into the Python context (when to use Python's math vs. asking an LLM to calculate)
- **Data privacy reflex** — instinct is developing but not yet automatic; any fintech scenario in Week 4 is an opportunity to reinforce it

## Week 4 Setup Notes
- Week 4 is Python for AI — SQL thinking → code thinking
- Royce has basic SQL knowledge; the SQL → Python bridge table in the syllabus is the spine of the lesson
- Frame Python as a new syntax for logic he already knows, not a new way of thinking
- Start with variables, strings, lists, dictionaries — avoid jumping to functions before these feel familiar
- The final project context (Business Intelligence Agent) should be referenced throughout — every Python concept should connect to "here's where you'll use this in Weeks 7-8"
- Read Week 1, 2, and 3 summaries before starting — Royce explicitly requested this and flagged it when it wasn't done
