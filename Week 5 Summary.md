# Week 5 Summary — The Claude API
### AI Fluency: Framework & Foundations | Royce | May 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 6, or whenever you need a refresher.*

---

## Key Concepts

### What Is an API?

API stands for Application Programming Interface. The definition isn't useful — the analogy is.

**An API is a waiter.** You don't walk into the kitchen and cook your own meal. You tell the waiter what you want, the waiter goes to the kitchen, and the kitchen sends back a plate of food. You never need to know how the kitchen works — you just need to know how to order correctly.

In software terms:
- The kitchen = the powerful system (Claude, Stripe, Google Maps)
- You = the app or script that needs something
- The waiter = the API, the standardised way those two parties communicate

---

### The Claude API vs. The Chat Interface

| | Chat Interface | Claude API |
|---|---|---|
| Who sends the message | A human typing | A Python script |
| Who reads the response | A human reading | A Python script |
| Can it be automated | No | Yes |
| Control over output | Limited | Full |
| Use case | Conversation | Building products |

The fundamental difference: the chat interface requires a human in the loop. The API removes that human and lets code do the sending and reading. That's what makes your Business Intelligence Agent possible — no human has to type "tell me about Stripe" every time. The script does it automatically.

---

### Is the Claude API Python-Only?

No. The Claude API is built on **HTTP** — the same protocol your browser uses to load web pages. Any programming language that can make an HTTP request can use it (Python, JavaScript, Ruby, Go, and many others).

What Anthropic *has* done is publish an official **SDK** (Software Development Kit) for Python and JavaScript. An SDK is a pre-built library of helper code that makes the API easier to use in a specific language — it handles the technical plumbing so you don't have to.

The hierarchy:
```
HTTP API (universal, any language)
    └── Python SDK (convenient wrapper for Python)
```

You use the Python SDK because that's the language you've been building in. The underlying API speaks to the whole world.

---

### API vs. MCP

Two different things that are easy to confuse.

**API** — a communication channel between two systems. You call the Claude API to send a message to Claude and get a response back. It's a direct line: your script → Claude.

**MCP (Model Context Protocol)** — a standard that lets Claude reach out and use external tools. File systems, calendars, databases, browsers. Instead of every tool needing custom wiring to connect to Claude, MCP defines one standard connector so any tool can plug in.

| | API | MCP |
|---|---|---|
| Direction | You → Claude | Claude → tools/world |
| What it is | Communication channel | Standard for tool connections |
| Your project | You call the API from Python | Claude uses MCP to read your files in Cowork |

In short: **you call the API to talk *to* Claude. MCP is how Claude talks *to the world*.**

---

### What Is an API Key?

An API key is your **identity credential**. It's how Anthropic knows who is making calls so they can track usage and bill your account. Every call you make is tied to your key.

Important things to know:

- **One key can be used across many projects** — it's not project-specific. It's account-specific.
- **Leaking a key exposes your billing account**, not your data or conversation history. Someone with your key can make API calls charged to you.
- **Companies use multiple keys for control**, not data separation. If one key leaks, you delete just that key without breaking every other project. Think of it like having separate corporate credit cards per department — not because each card stores different data, but so you can cancel one without affecting everyone else.
- **Keys don't store historical data** — your prompts and responses are governed by your account agreement with Anthropic, not by which key you used.

---

### The .env File

The `.env` file is a plain text file that lives in your project folder and stores secrets — API keys, passwords, configuration values — separately from your code.

**Why it exists:** You never want to paste your API key directly into a Python file. If you share that file, post it to GitHub, or send it to anyone, the key goes with it. The `.env` file keeps secrets out of your code entirely.

**Naming:** `.env` is a widely adopted industry convention — short for "environment." Almost every developer tool knows to look for a file with exactly this name. It's not a placeholder.

**What it looks like:**
```
ANTHROPIC_API_KEY=sk-ant-api03-xxx...
```

**Multiple keys in one file:** You can store as many keys as your project needs in the same `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxx...
POLYGON_API_KEY=your_polygon_key_here
STRIPE_API_KEY=your_stripe_key_here
```

**One `.env` per project folder** — if you have multiple projects, each gets its own `.env` in its own folder. Same filename, different locations, no conflict.

---

### The dotenv Library

`dotenv` is the name of the Python library that reads your `.env` file and loads what's inside it into your system's memory so Python can access it.

There are two slightly different ways to import things in Python:

```python
import anthropic
```
This imports the *entire* anthropic library. You access everything through it with `anthropic.Anthropic()`.

```python
from dotenv import load_dotenv
```
This imports *just one specific function* — `load_dotenv` — from the `dotenv` library. You don't need the whole library, just that one tool.

**The analogy:** `import anthropic` is like hiring a whole team. `from dotenv import load_dotenv` is like calling one specific person to do one specific job.

**How it works in practice:**
```python
from dotenv import load_dotenv    # import the function
load_dotenv()                     # call it — finds .env, loads it into memory
```

After `load_dotenv()` runs, your `ANTHROPIC_API_KEY` is available in memory and the `anthropic` library finds it automatically. Your key never appears anywhere in your code.

The `.env` file and the `dotenv` library are two separate things that work together:
```
.env file → load_dotenv() reads it → ANTHROPIC_API_KEY in memory → anthropic library finds it
```

---

### Anatomy of a Claude API Call

Every API call has the same structure. Here it is with every line explained:

```python
from dotenv import load_dotenv    # import just the load_dotenv function
import anthropic                  # import the full anthropic library

load_dotenv()                     # find .env, load the API key into memory

client = anthropic.Anthropic()    # open a connection to Claude (like picking up the phone)

message = client.messages.create( # place your order — this sends the request
    model="claude-haiku-4-5-20251001",  # which version of Claude to use
    max_tokens=1024,              # maximum length of Claude's response (~750 words)
    messages=[                    # the conversation — a list of dictionaries
        {"role": "user", "content": "Your prompt here."}
    ]
)

print(message.content[0].text)   # pull the text out of the response and print it
```

**The `messages` list in detail:**
- It's a list `[]` containing one or more dictionaries `{}`
- Each dictionary has two keys: `"role"` and `"content"`
- `"role": "user"` means you are speaking
- `"role": "assistant"` means Claude is speaking (used when passing conversation history)
- `"content"` is the actual text of the message

**Why `"role"` exists:** The API supports multi-turn conversations. You can pass an entire conversation history and Claude responds in context. For your Business Intelligence Agent you'll only ever have one `"user"` message per call, but the role labelling is part of the structure regardless.

---

### The Response Object

The API doesn't return a plain string. It returns a **response object** — a structured package containing metadata (which model responded, how many tokens were used) and the actual text.

The text lives here:
```python
message.content[0].text
```

Breaking down the chain:
- `message` — the whole response package
- `.content` — a list of content blocks (Claude can return multiple blocks)
- `[0]` — the first block (almost always the only one)
- `.text` — the actual string of words Claude wrote

**How developers discover this structure:** You peel back the layers one at a time:
```python
print(message)                # the whole object
print(message.content)        # the content list
print(message.content[0])     # the first block
print(message.content[0].text)  # just the text
```

This is how any developer reads a new API response — you inspect it layer by layer until you find what you need. Nobody memorises this; they look it up in the documentation or explore it directly.

---

### Dynamic Prompts with Variables and F-strings

A hardcoded prompt always asks about the same thing:
```python
"Give me a one-paragraph overview of Stripe as a fintech company."
```

A dynamic prompt uses a variable and an f-string so it works for any company:
```python
company = "Stripe"
prompt = f"Give me a one-paragraph overview of {company} as a fintech company."
```

Change `company = "Stripe"` to `company = "Wealthsimple"` and the whole prompt updates automatically. You only ever touch one line.

**Storing the prompt in a variable** keeps your code readable. Instead of a long string directly inside `"content"`, you pass the variable:
```python
{"role": "user", "content": prompt}
```

---

### Single Quotes, Double Quotes, and Triple Quotes

| Syntax | What it does |
|---|---|
| `"..."` | Single-line string |
| `'...'` | Single-line string (identical to double quotes) |
| `"""..."""` | Multi-line string — can span many lines |
| `f"..."` | Single-line string with variables |
| `f"""..."""` | Multi-line string with variables |

Triple quotes `"""..."""` are used when a string is too long to fit on one line — like a structured prompt with multiple sections. The `f` prefix and the `"""` are completely independent: the `f` enables variables, the `"""` enables multiple lines. They can be used together.

---

### Writing a Structured Prompt

The quality of Claude's output is determined entirely by the quality of your prompt. A vague prompt returns a vague response. A structured prompt returns structured, consistent output.

**A well-structured prompt:**
- Gives Claude a role (`"You are a business intelligence assistant"`)
- Specifies exactly what sections to return
- Tells Claude how to format the output
- Uses an f-string so it works for any company

```python
company = "Affirm"

prompt = f"""You are a business intelligence assistant.
Produce a structured one-page brief on {company} using the following sections:

1. Company Overview: What the company does and who it serves (2-3 sentences)
2. Business Model: How it makes money
3. Key Products: Main products or features
4. Competitive Landscape: 2-3 main competitors
5. Recent News or Trends: Anything notable in the last 1-2 years

Be concise and factual. Format each section with its heading."""
```

This is the prompt your Business Intelligence Agent uses. The structure is what makes the output consistent every time — regardless of which company you ask about.

---

### The Standard Boilerplate

These lines appear at the top of every API script you write. Think of them as your starting template:

```python
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()
```

Like `SELECT` at the start of every SQL query — you write these automatically, then build your specific logic below.

---

## The Python + API Cheat Sheet

| Syntax | Used for |
|---|---|
| `import X` | Import an entire library |
| `from X import Y` | Import one specific function from a library |
| `load_dotenv()` | Read the .env file and load keys into memory |
| `anthropic.Anthropic()` | Open a connection to Claude |
| `client.messages.create(...)` | Send a request to Claude |
| `model=` | Which Claude version to use |
| `max_tokens=` | Maximum response length |
| `messages=[{"role": "user", "content": ...}]` | The prompt, as a list of dictionaries |
| `message.content[0].text` | The text of Claude's response |
| `f"""..."""` | Multi-line string with variables |
| `{"role": "user", "content": prompt}` | Passing a prompt variable into the messages list |

---

## PM Takeaways

**On APIs as a PM skill:** Most powerful features in modern fintech products are built on APIs. When Robinhood shows you a stock quote — API call. When Wise converts currencies — API call. When your bank sends a fraud alert — API call. As a PM, you'll spec features that depend on APIs constantly. Most PMs can describe APIs in a meeting. You've now *written one* — that's a different level of credibility.

**On API key security:** Never hardcode secrets in code files. The `.env` pattern is industry standard — it keeps credentials out of your codebase and out of version control. This applies to every API key you'll ever use, not just Anthropic's.

**On prompt engineering and output quality:** The structure of Claude's response is entirely controlled by how you write the prompt. Giving Claude a role, specifying sections, and telling it how to format output are the PM's tools for controlling AI behaviour in a product. This is spec writing applied to AI.

**On the arithmetic/LLM divide (reinforced):** LLMs predict tokens based on pattern recognition. They don't compute. In any fintech feature involving calculations — credit scores, rate calculations, balance projections, risk scores — Python handles the arithmetic, Claude handles the language. Getting this wrong in a regulated industry isn't just a bug, it's a liability. A wrong credit score means wrong lending decisions, potential regulatory violations, and real financial harm to users.

**On the API powering your final project:** Your Business Intelligence Agent is now mostly built. The `week5_practice.py` script you wrote this week already does the core job: take a company name, call Claude, return a structured brief. Weeks 7 and 8 add user input and polish. The hard part is done.

---

## Questions Royce Asked (with answers)

**"Does the Claude API only work with Python?"**
No — it's built on HTTP, which any language can use. Anthropic publishes official SDKs for Python and JavaScript to make it easier, but the API itself is language-agnostic.

**"What's the difference between MCP and an API?"**
API = communication channel (you → Claude). MCP = standard for connecting Claude to external tools (Claude → world). You call the API from your scripts. Claude uses MCP to access file systems, browsers, and other services.

**"Does an API key store my historical data?"**
No. The key is purely an authentication credential. Your conversation data is governed by your account agreement with Anthropic, not by the key. Leaking a key exposes your billing account, not your data.

**"Why do companies use multiple API keys?"**
For control and damage limitation, not data separation. One key per project or team means if one leaks, you delete just that key without breaking everything else. Like separate corporate credit cards per department.

**"Am I charged separately for the API if I already pay for Pro?"**
Yes — they are separate products with separate billing. Claude Pro covers the chat interface at claude.ai. The API is billed by token usage at console.anthropic.com. Free credits are sometimes available for new API accounts; otherwise $20 covers far more usage than this entire course requires.

**"Is the name `.env` a placeholder?"**
No — it's a widely adopted industry convention. Almost every developer tool knows to look for a file called exactly `.env`. The name is standard, not customisable.

**"Can I store multiple API keys in the same `.env` file?"**
Yes — one `.env` per project, all secrets for that project inside it. Each key gets its own line with a clear name.

**"What does `from dotenv import load_dotenv` mean?"**
`from dotenv` specifies the library. `import load_dotenv` imports just one specific function from it — not the whole library. The analogy: hiring one specific person for one specific job vs. hiring a whole team.

**"Is `.env` automatically referred to as `dotenv` when calling the API?"**
They're two separate things that work together. `dotenv` is the library name. `.env` is the file name. `load_dotenv()` is the function that connects them — it finds the `.env` file and loads its contents into memory.

**"What is the purpose of `role: user`?"**
The API supports multi-turn conversations, so it needs to know who said what. `"role": "user"` means you're speaking. `"role": "assistant"` means Claude is speaking. When passing conversation history, you include both. For single-turn calls like your agent, you'll always just have one `"user"` message.

**"Why are there `"""` instead of just `f"`?"**
`f` enables variables inside a string. `"""` enables multi-line strings. They're independent features that can be combined: `f"""..."""` gives you a multi-line string with variables. Single `"` limits you to one line.

---

## Exercise Results

**Dictionary access warmup:**
Correctly identified `print(response["text"])` as the syntax for accessing a key. Used `{}` instead of `[]` initially — fixed immediately once explained. Confirmed understanding of "key" as the correct terminology.

**Syntax drill (Tasks 1–3):**
All three correct. List creation and index access right. Dictionary creation right — number stored as number, `False` capitalised correctly. Chained access `companies[0]["valuation"]` correct with strong verbal explanation of the logic.

**week5_first_call.py:**
First live API call — ran successfully in Terminal after resolving library installation and permissions issues. Response received for Stripe.

**week5_practice.py (written from scratch):**
Wrote the full script independently from memory. One syntax error: `)print(...)` with no line break between closing bracket and print statement. Fixed and ran successfully — live response received for Wealthsimple.

**Dynamic prompt exercise:**
One syntax error: `[company]` instead of `{company}` in the f-string (square vs curly brackets). Fixed and ran — live responses received for Koho and Affirm with full structured output.

**Prompt improvement:**
Independently improved the prompt sections — added "Include main source and supplementary sources" to Business Model and "how they differentiate, and where they overlap" to Competitive Landscape without being asked. Demonstrated genuine product thinking.

---

## Assessment Results

**Score: 5.75/8**

| Question | Score | Notes |
|---|---|---|
| Q1 — API vs chat interface | 0.75/1 | Got automation and control right; didn't clearly state the core distinction (programmatic vs human interaction) |
| Q2 — .env, load_dotenv, API key | 0.75/1 | Minor inaccuracies: .env is a file not a folder; load_dotenv loads into memory not directly into the script |
| Q3 — Code reading | 1.5/2 | Traced variables correctly; missed that `print(prompt)` prints the prompt string itself, not a Claude response — there's no API call in that code |
| Q4 — Code writing | 1/2 | Structure correct; three syntax errors: missing `()` on `load_dotenv`, missing quotes on `"Visa"`, imports not all at the top |
| Q5 — Applied scenario | 1.75/2 | Strong — correctly applied the arithmetic/LLM divide; could name specific consequences (wrong lending decisions, regulatory risk, financial harm to users) |

**Key gaps to carry into Week 6:**
- `print(prompt)` prints the prompt string, not a Claude response — reading what code *actually outputs* vs what it *conceptually does* is a recurring gap worth practising
- Syntax precision: `load_dotenv()` not `load_dotenv`, string values always in quotes, imports at the top

---

---

# PART 2 — Session Handoff

*For the next session's Claude. Read this before beginning Week 6.*

---

## Course Status
- **Week 1:** Complete ✓ — Score: 5.5/6
- **Week 2:** Complete ✓ — Score: 6.5/8
- **Week 3:** Complete ✓ — Score: 7/8
- **Week 4:** Complete ✓ — Score: 5.75/8
- **Week 5:** Complete ✓ — Score: 5.75/8
- **Week 6:** Designing Your Agent (PM-focused) — ready to begin

## What Was Covered in Week 5
Full lesson on the Claude API, delivered in five parts:
- Part 1: What an API is — waiter analogy, Claude API vs chat interface, why it matters for PMs
- Part 2: How an API call is structured — anatomy line by line, the response object, `message.content[0].text`
- Part 3: First live API call — setup (.env, API key, libraries), `week5_first_call.py` run successfully in Terminal
- Part 4: Dynamic prompts — f-strings with variables, `week5_practice.py` written from scratch by Royce, runs successfully for multiple companies
- Part 5: Structured prompts — multi-section prompt with role assignment, `f"""..."""` syntax, prompt stored as variable

## Setup Completed This Session
- Anthropic API account created, credits purchased ($20)
- API key generated and stored in `.env` file in workspace folder
- `anthropic` and `python-dotenv` libraries installed on Royce's Mac
- VS Code set up as code editor
- Terminal permissions granted for Desktop folder access
- Workflow established: write in VS Code → run in Terminal

## What Landed Well
- The waiter analogy for APIs — clicked immediately
- API vs MCP distinction — Royce asked about this unprompted, suggesting genuine curiosity
- Line-by-line breakdown of the API call anatomy — Royce explicitly asked for this when the first pass moved too fast; good instinct to slow down
- `f"""..."""` explanation — the table showing all four string type combinations resolved confusion cleanly
- Prompt improvement exercise — Royce independently added richer section descriptions without being asked; genuine PM instinct
- Q5 on the arithmetic/LLM divide — answered confidently and correctly; this concept has now fully landed across three weeks of reinforcement

## What Was Harder
- `print(prompt)` vs receiving a Claude response — Royce described the f-string mechanics correctly but assumed `print(prompt)` would produce Claude's output. The distinction between building a prompt and sending it needs reinforcement in Week 6.
- Syntax precision — recurring pattern: `load_dotenv` without `()`, `company = Visa` without quotes. Small errors but consistent. Worth a warmup exercise at the start of Week 6.
- `{company}` vs `[company]` in f-strings — square bracket habit from dictionary access bleeding into f-strings. Corrected quickly but appeared twice.

## Tangents Explored
- Pro vs API billing — fully resolved; Royce purchased $20 in API credits
- API key security — what leaking exposes (billing, not data), why companies use multiple keys
- Whether one key can serve multiple projects — yes, account-level not project-level
- Terminal navigation — covered `~` vs `/`, `cd`, `pwd`, backslash escaping, quotes for paths with spaces. Royce wants to learn Terminal separately — keep coverage minimal in Week 6 summary per his request.
- VS Code setup — Royce now uses VS Code as his code editor

## Royce's Workflow Note
Royce asked that Terminal navigation not be covered in depth in weekly summaries — he plans to learn it separately. All other concepts should remain exhaustive in the summary. This preference is now saved in memory.

## Week 5 Files in Workspace
- `week5_first_call.py` — first API call, hardcoded Stripe prompt
- `week5_practice.py` — dynamic prompt with f-string, structured multi-section brief, runs for any company

## Gaps to Carry Into Week 6
- **`print(prompt)` vs API response** — open Week 6 with a quick check: "what does this code print?" on a script that has a prompt variable but no API call. Reinforce that building a string and sending it to Claude are two separate steps.
- **Syntax precision** — small warmup on `()` on function calls, quotes around string values.
- **The agent is nearly complete** — `week5_practice.py` already does the core job. Week 6 is about designing the full agent experience: user input, output formatting, error handling, and the product thinking behind it. Frame it as: "the engine works — now we design the car around it."

## Week 6 Setup Notes
- Week 6 is Designing Your Agent (PM-focused) — product thinking, user input (`input()`), output formatting, edge cases, error handling
- The Business Intelligence Agent is the throughline — every concept connects directly to the final project
- Royce's PM instincts are strong (see prompt improvement exercise, Q5) — lean into product framing throughout
- Continue using fintech examples (Royce's target industry)
- Read all Week 1–5 summaries before beginning — Royce flagged this as important
