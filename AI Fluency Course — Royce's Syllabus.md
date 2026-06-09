# AI Fluency: Framework & Foundations
### Your Personal Course Syllabus — Designed for Royce

**Duration:** 8 Weeks  
**Pace:** 5–10 hours/week  
**Background:** Business + Basic SQL  
**End Goal:** Build a business automation AI agent to showcase in PM job applications

---

## 🎯 What You'll Walk Away With

By the end of this course, you will be able to:
- Explain how AI and large language models work — in plain English and in a PM interview
- Write high-quality prompts that get consistently excellent results from AI tools
- Navigate the AI tools landscape and make smart product decisions about AI
- Read and write basic Python well enough to build real AI-powered applications
- Call the Claude API to connect your own logic to a powerful AI model
- Design, build, and document a business automation AI agent from scratch
- Tell a compelling story about your AI project to a hiring manager

---

## Course Overview

| Week | Module | Theme |
|------|--------|-------|
| 1 | How AI Actually Works | Build the mental model |
| 2 | Prompt Engineering | Your #1 PM superpower |
| 3 | The AI Tools Landscape | Think like a PM, not a user |
| 4 | Python for AI | SQL thinking → code thinking |
| 5 | The Claude API | Talk to AI programmatically |
| 6 | Designing Your Agent | Product thinking meets AI |
| 7 | Building Your Agent | Hands-on construction |
| 8 | Polish, Document & Present | PM-ready portfolio piece |

---

## Week 1: How AI Actually Works

**Theme:** Build the right mental model — no fluff, no magic

### Why This Matters for PM Roles
Product managers who understand *how* AI works make better prioritization decisions, write better specs, and earn the trust of engineering teams. You don't need to be an engineer — but you need to know what's actually happening under the hood.

### Topics
- What is a Large Language Model (LLM)? The core idea explained through analogy
- How AI "thinks": tokens, context windows, and probability — not rules
- What AI is genuinely good at vs. where it fails (and why this matters for product decisions)
- The difference between AI models: Claude, GPT, Gemini — how to compare them as a PM
- Key vocabulary every PM must know: inference, fine-tuning, RAG, hallucination, temperature

### Exercises
1. **The Misconception Audit:** List 5 things you believed about AI before this week. Revise each one with what you now know.
2. **Capability Map:** Create a simple 2x2 grid — "AI is great at / AI struggles with" — using 3 real business examples in each quadrant.
3. **Vocabulary Flash Cards:** Define each key term in one sentence as if explaining to a non-technical stakeholder.

### Milestone Check
> *Can you explain to someone in a 2-minute conversation what an LLM is, how it generates text, and name two things it's bad at?*

---

## Week 2: Prompt Engineering — Your #1 PM Superpower

**Theme:** Most people use AI like a search engine. You'll use it like a colleague.

### Why This Matters for PM Roles
Prompt engineering is the most immediately transferable AI skill for PMs. It's how you write better specs, run better research, synthesize faster — and it directly signals AI fluency in interviews.

### Topics
- The anatomy of a great prompt: Role + Context + Task + Format + Constraints
- Zero-shot vs. few-shot prompting: when to show examples
- Chain-of-thought prompting: getting AI to reason step by step
- Iterative prompting: treating AI like a conversation, not a command
- System prompts: setting the stage before the conversation starts
- Common failure modes and how to diagnose them

### Exercises
1. **The Rewrite Challenge:** Take a vague prompt ("summarize this"), rewrite it 3 times using progressively better structure. Compare outputs side-by-side.
2. **PM Scenario Sprint:** Write prompts for 5 real PM tasks: user story writing, competitive analysis, meeting notes synthesis, PRD first draft, stakeholder update.
3. **Failure Autopsy:** Deliberately write a bad prompt, get a bad result, diagnose *why* it failed, fix it.

### The Golden Template
```
You are [role/persona].

Context: [background information the AI needs]

Task: [exactly what you want it to do]

Format: [how you want the output structured]

Constraints: [what to avoid, tone, length, etc.]
```

### Milestone Check
> *Can you take a business problem and write a prompt that produces a genuinely useful, structured output on the first try?*

---

## Week 3: The AI Tools Landscape

**Theme:** Stop being a user — start thinking like a product person

### Why This Matters for PM Roles
PMs are expected to evaluate AI tools, make build-vs-buy decisions, and understand how AI features integrate into products. This week trains that exact muscle.

### Topics
- The AI stack: frontier models, APIs, wrappers, and end-user products
- Categories of AI tools: writing, research, coding, automation, data analysis, agents
- How to evaluate an AI tool like a PM: capability, reliability, cost, API access, data privacy
- No-code AI tools vs. API-first tools — what's the difference and when to use each
- How companies are actually building with AI: real product case studies
- Introduction to AI agents: what makes something an "agent" vs. a chatbot

### Exercises
1. **Tool Teardown:** Pick one AI product (e.g., Notion AI, Perplexity, Cursor). Write a 1-page PM brief: What problem does it solve? Who is the user? What AI capability does it use? What would you change?
2. **Build vs. Buy Analysis:** You're a PM at a mid-size company. Your team wants AI-powered meeting summaries. Map out 3 options: use an existing tool, build on an API, fine-tune a model. Pros and cons of each.
3. **Agent vs. Chatbot:** Find one example of each in the wild. Write 3 sentences explaining the difference to a non-technical stakeholder.

### Milestone Check
> *Can you evaluate an AI tool and explain — in PM terms — how it works, who it's for, and where it could fail?*

---

## Week 4: Python for AI — SQL Thinking → Code Thinking

**Theme:** You already think like a programmer. Now you'll write like one.

### Why This Matters for PM Roles
You don't need to be a senior engineer. But writing basic Python to call an API, process some data, and output a result is now a real expectation in many PM roles — especially at AI-first companies. Your SQL background is a genuine advantage here.

### The SQL → Python Bridge

| SQL Concept | Python Equivalent |
|-------------|-------------------|
| `SELECT column FROM table WHERE condition` | `for item in list: if condition:` |
| Variable | Variable |
| String | String |
| `CONCAT()` | `f"string {variable}"` |
| `COUNT()` | `len(list)` |
| Function | Function `def name():` |
| Query result | Dictionary or list |

### Topics
- Python setup: installing Python, using VS Code or a notebook (no intimidation)
- Variables, strings, lists, dictionaries — the 4 things you'll use constantly
- Functions: writing reusable blocks of logic
- Reading and writing files
- Calling an API with the `requests` library
- Handling JSON responses (this is where your SQL instinct kicks in)

### Exercises
1. **Hello, Business:** Write a Python script that takes a company name as input and prints a formatted string about it.
2. **Data Wrangler:** Given a list of 10 customer feedback strings, write a Python script that counts how many contain the word "slow" or "fast."
3. **File Reader:** Write a script that reads a `.txt` file, counts the number of words, and prints a summary.

### Milestone Check
> *Can you write a Python function that takes a string input, does something with it, and returns a formatted output?*

---

## Week 5: The Claude API — Talking to AI Programmatically

**Theme:** Connect your own logic to a powerful AI brain

### Why This Matters for PM Roles
Understanding APIs — especially AI APIs — is the bridge between "I use AI" and "I build with AI." This is the week that transforms your project from a demo into a product.

### Topics
- What is an API? The restaurant analogy (you're the customer, the API is the waiter)
- Getting your Anthropic API key and setting up authentication
- Your first API call: sending a message to Claude from Python
- Understanding the request structure: model, messages, max_tokens
- System prompts in the API: setting Claude's role and behavior
- Handling the response: extracting Claude's text from JSON
- Cost and token management: thinking like a PM about unit economics

### Code Walkthrough — Your First API Call
```python
import anthropic

client = anthropic.Anthropic(api_key="your-key-here")

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Summarize the key risks of launching a new product."}
    ]
)

print(message.content[0].text)
```

### Exercises
1. **First Contact:** Get your API key, run the example above, and see Claude respond in your terminal. (This will feel like magic — it is.)
2. **The Business Brief Generator:** Write a Python script that takes a company name as input and asks Claude to generate a 3-bullet competitive summary.
3. **System Prompt Experiment:** Add a system prompt that tells Claude to always respond as a senior McKinsey consultant. Compare the output to a response without it.

### Milestone Check
> *Can you write a Python script that sends a custom prompt to Claude and prints the response? Can you explain what each line does?*

---

## Week 6: Designing Your Agent — Product Thinking Meets AI

**Theme:** Before you build, you design. This is pure PM work.

### Why This Matters for PM Roles
This week is your PM showcase. Designing an AI agent requires the same skills as designing any product: understanding the user, defining the problem, mapping flows, and thinking through edge cases. This week's output goes directly into your portfolio.

### What Makes Something an "Agent"?
A chatbot answers one question at a time. An **agent** can:
- Take a goal, not just a command
- Break that goal into steps
- Take actions (call APIs, read files, do research)
- Use the results of one step to inform the next
- Produce a final deliverable

### Your Final Project: The Business Intelligence Agent

**What it does:** You give it a company name (or a business question). It:
1. Generates a research plan for what to investigate
2. Analyzes the company across 4 dimensions: business model, market position, key risks, opportunities
3. Synthesizes findings into a structured one-page brief
4. Formats and saves the output as a file you can share

**Why it's PM-perfect:**
- Shows you understand AI capabilities and limitations
- Demonstrates product thinking (you defined the problem, designed the flow)
- Produces a real artifact (the brief) that has business value
- Is explainable to non-technical interviewers

### Design Exercises
1. **User Story:** Write the user story for your agent. ("As a [user], I want to [do X] so that [Y].")
2. **Flow Diagram:** Map the step-by-step flow of your agent on paper or in a tool like Miro/FigJam.
3. **Edge Cases:** List 5 things that could go wrong. How should the agent handle each?
4. **Success Metrics:** How would you measure whether this agent is working well? Define 3 metrics.

### Milestone Check
> *Can you describe your agent's purpose, flow, and failure modes to someone who has never seen it?*

---

## Week 7: Building Your Agent

**Theme:** Ship it.

### What You're Building (Full Code Walkthrough)
Your agent will have 4 components:

**Component 1 — Input Handler**
Accepts a company name from the user and validates it.

**Component 2 — Research Orchestrator**
Sends structured prompts to Claude to analyze the company across 4 dimensions.

**Component 3 — Synthesis Engine**
Sends all 4 analyses to Claude with a final prompt to produce a clean, one-page brief.

**Component 4 — Output Writer**
Formats the brief and saves it as a `.txt` or `.md` file.

### Build Steps
1. Start with Component 1 alone — get input working
2. Add Component 2 — test Claude's analysis on one dimension
3. Extend to all 4 dimensions — loop through them
4. Build Component 3 — pass all 4 outputs into a synthesis prompt
5. Add Component 4 — write the final output to a file
6. Test on 3 different companies and review the results

### Debugging Mindset
When something breaks:
- Read the error message out loud
- Ask Claude to explain the error and suggest a fix
- Fix one thing at a time
- Test after every change

### Milestone Check
> *Does your agent run end-to-end and produce a readable, useful brief for at least 3 different companies?*

---

## Week 8: Polish, Document & Present

**Theme:** Great work doesn't speak for itself — you do.

### Why This Matters for PM Roles
The best portfolio projects are ones you can *explain clearly* to a non-technical interviewer in 5 minutes. This week, you'll package everything you've built into a story.

### Polish Your Agent
- Add clear print statements so the user can follow along as it runs
- Handle common errors gracefully (what if the company name is blank?)
- Make the output formatting clean and professional
- Test on at least 5 companies and fix any rough edges

### Document Your Project
Write a one-page project brief (a real PM deliverable) that covers:
- **Problem:** What problem does this agent solve?
- **Solution:** What does it do, and how?
- **How I Built It:** A plain-English summary of the architecture
- **What I Learned:** 3 things this project taught you about AI
- **What's Next:** If you had another month, what would you add?

### Interview Prep
Be ready to answer these questions naturally:
- *"Tell me about an AI project you've worked on."*
- *"How does your agent work under the hood?"*
- *"What was the hardest part? How did you solve it?"*
- *"What would you do differently if you built it again?"*
- *"How would you turn this into a real product?"*

### Final Deliverables
- [ ] Working AI agent (Python script)
- [ ] Project brief (1-page document)
- [ ] 5-minute verbal walkthrough you can deliver in an interview
- [ ] Code saved to a GitHub repository (we'll set this up together)

---

## Your Learning Principles

**1. Build early, build often.** Don't wait until you "understand everything" to start coding. Build something broken, fix it, repeat.

**2. Confusion is progress.** When something confuses you, that's the exact spot where learning is happening. Sit with it.

**3. Explain it back.** After each week, try to explain the key concept to someone else (or out loud to yourself). If you can't, re-read.

**4. Use AI to learn AI.** Stuck on a Python error? Ask Claude. Don't understand a concept? Ask Claude to explain it 5 different ways. This is the meta-skill.

**5. Think like a PM, not a coder.** Your job isn't to write perfect code. It's to build something that solves a real problem. Keep that lens on.

---

## A Note on Your SQL Background

This is a genuine advantage that most beginners don't have. Here's why:

- You already understand **structured thinking** — breaking a question into a query
- You already know what **inputs and outputs** are in a programmatic context
- You've already seen how **data types** (strings, numbers) work
- You're comfortable with the idea that **syntax matters** (one typo breaks everything)

When Python feels unfamiliar, map it back to SQL. The logic is the same — the syntax is just different.

---

*Course designed for Royce | AI Fluency: Framework & Foundations | May 2026*
