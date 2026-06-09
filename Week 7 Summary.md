# Week 7 Summary — Building Your Agent
### AI Fluency: Framework & Foundations | Royce | June 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 8, or whenever you need a refresher.*

---

## Warmup — Execution Tracing

A gap carried from Week 6 was closed at the start of this session: when asked "what does the terminal show?", always give the *exact* characters that appear — including punctuation, capitalization, and spacing.

Example script:
```python
company = input("Enter company: ")

if company == "":
    print("No input.")
else:
    result = f"Researching {company.upper()}..."
    print(result)
    print("Done.")
```

If the user types `stripe`, the terminal shows:
```
Enter company: stripe
Researching STRIPE...
Done.
```

Two easy misses:
- `.upper()` converts to ALL CAPS — `STRIPE` not `Stripe`
- The `...` in the f-string is part of the string and prints literally

**The habit:** When tracing code, copy what the screen would show character by character. Don't explain — output.

---

## What You Built

Your Business Intelligence Agent — upgraded from Week 6's single-call script to a 5-call prompt chain:

```
User types company
    → Claude call 1: Analyze business model
    → Claude call 2: Analyze market position
    → Claude call 3: Analyze key risks
    → Claude call 4: Analyze opportunities
    → Claude call 5: Synthesize all 4 into a final brief
    → Save to file
```

This is a real, working AI agent. You ran it on Wealthsimple and produced a structured business intelligence brief.

---

## Prompt Chaining

**What it is:** Using the output of one Claude call as the input for the next. Each step produces a result that feeds into the following step.

**Why it produces better output than a single prompt:** Each call gets focused attention on one dimension. A single prompt asking Claude to cover everything produces shallower work. Chaining is like having four specialists each write one section, then a senior analyst synthesize it — versus asking one person to do everything at once.

**The PM angle:** "Does this use a single prompt or a chain?" is a meaningful architectural question when evaluating AI features. Chains are slower and more expensive, but produce meaningfully better results for complex tasks. That's a real product tradeoff.

---

## For Loops

The key new Python concept this week. A for loop runs the same block of code once for each item in a list.

```python
dimensions = ["business model", "market position", "key risks", "opportunities"]

for dimension in dimensions:
    print(f"Analyzing {dimension}...")
```

- `dimensions` — a list of 4 strings
- `for dimension in dimensions` — "for each item in this list, call it `dimension` and run the indented code below"
- Each pass through the loop, `dimension` takes the next value: `"business model"`, then `"market position"`, then `"key risks"`, then `"opportunities"`

Terminal output:
```
Analyzing business model...
Analyzing market position...
Analyzing key risks...
Analyzing opportunities...
```

One block of code, ran 4 times automatically.

**The SQL analogy:** Instead of writing 4 separate queries for 4 rows, you write one query and let the database loop through matching rows. A for loop is the same idea — write the logic once, run it for every item in a list.

---

## Storing Loop Results with `.append()`

A loop that just prints isn't useful — you need to *save* each Claude response so you can pass them all to the synthesis step.

```python
results = []

for dimension in dimensions:
    response = message.content[0].text
    results.append(response)
```

- `results = []` — an empty list, like an empty container
- `results.append(response)` — adds the response to the end of the list after each loop pass
- After 4 loops, `results` contains all 4 Claude responses in order

**`append` means:** "add to the end of." Each loop adds one item to the list.

---

## The Research Orchestrator (Component 2)

```python
dimensions = ["business model", "market position", "key risks", "opportunities"]
results = []

for dimension in dimensions:
    print(f"Analyzing {dimension}...")
    prompt = f"Give me a one-paragraph analysis of the {dimension} of {company}."
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    response = message.content[0].text
    results.append(response)
    print("Done.")
```

Terminal output while running:
```
Analyzing business model...
Done.
Analyzing market position...
Done.
Analyzing key risks...
Done.
Analyzing opportunities...
Done.
```

---

## Joining a List into a String with `.join()`

After the loop, `results` is a list of 4 strings. You need to combine them into one block of text to pass to the synthesis prompt.

```python
combined = "\n\n".join(results)
```

- `"\n\n".join(results)` — takes every item in `results` and joins them together, with two blank lines between each one
- `combined` ends up as one long string with all 4 analyses separated by blank lines
- Think of it like SQL's `CONCAT()` but for a whole list at once

---

## The Synthesis Engine (Component 3)

```python
combined = "\n\n".join(results)

synthesis_prompt = f"""You are a business intelligence assistant.
Here are four analyses of {company}:

{combined}

Using the above, write a clean, structured one-page brief in this format:

Executive Summary: A 3-4 sentence overview of the company and its most important characteristic.

Then the following sections:
1. Company Overview
2. Business Model
3. Market Position
4. Key Risks
5. Opportunities
"""

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2048,
    messages=[
        {"role": "user", "content": synthesis_prompt}
    ]
)

brief = message.content[0].text
print(brief)
```

This is the final Claude call — it receives all 4 analyses and synthesizes them into the formatted brief.

---

## The Output Writer (Component 4)

```python
print("\n" + "="*60)
print(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}")
print("="*60 + "\n")
print(brief)

filename = f"{company}_brief.txt"
with open(filename, "w") as f:
    f.write(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}\n")
    f.write("="*60 + "\n\n")
    f.write(brief)

print(f"\nBrief saved as {filename}")
```

Same as Week 6 — formats the terminal output and saves the brief to a file.

---

## The Complete Business Intelligence Agent

```python
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

company = input("Enter a company name: ")

if company == "":
    print("No company name entered. Please try again.")
else:
    dimensions = ["business model", "market position", "key risks", "opportunities"]
    results = []

    try:
        for dimension in dimensions:
            print(f"Analyzing {dimension}...")
            prompt = f"Give me a one-paragraph analysis of the {dimension} of {company}."
            
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            response = message.content[0].text
            results.append(response)
            print("Done.")

        combined = "\n\n".join(results)

        synthesis_prompt = f"""You are a business intelligence assistant.
Here are four analyses of {company}:

{combined}

Using the above, write a clean, structured one-page brief in this format:

Executive Summary: A 3-4 sentence overview of the company and its most important characteristic.

Then the following sections:
1. Company Overview
2. Business Model
3. Market Position
4. Key Risks
5. Opportunities
"""

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2048,
            messages=[
                {"role": "user", "content": synthesis_prompt}
            ]
        )

        brief = message.content[0].text

        print("\n" + "="*60)
        print(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}")
        print("="*60 + "\n")
        print(brief)

        filename = f"{company}_brief.txt"
        with open(filename, "w") as f:
            f.write(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}\n")
            f.write("="*60 + "\n\n")
            f.write(brief)

        print(f"\nBrief saved as {filename}")

    except Exception as e:
        print(f"Something went wrong: {e}")
        print("Please check your API key and internet connection.")
```

Saved as `business_intelligence_agent.py` in your project folder. Run with:
```
python3 business_intelligence_agent.py
```

---

## Counter Variable in a For Loop

How to print a numbered list using a counter variable:

```python
companies = ["Stripe", "Wealthsimple", "Shopify"]
number = 1

for company in companies:
    print(f"{number}. {company}")
    number = number + 1
```

Output:
```
1. Stripe
2. Wealthsimple
3. Shopify
```

- `number = 1` — start the counter at 1
- `{number}.` — print the current number
- `number = number + 1` — increment after each print so the next loop shows the next number

---

## File Naming Convention

Standard Python file naming:
- All lowercase
- Underscores instead of spaces
- No special characters

✓ `business_intelligence_agent.py`
✗ `Business Intelligence Agent.py`

Reason: spaces in filenames require quotes in terminal (`python3 "Business Intelligence Agent.py"`), which is error-prone. Underscores avoid the problem entirely.

---

## PM Takeaways

**On prompt chaining as a product decision:** Whether to use a single prompt or a chain is a real architectural tradeoff. Chains produce better output but cost more and run slower. Knowing this lets you have an informed conversation with your engineering team about quality vs. cost vs. latency — three axes that always compete in AI product decisions.

**On token limits as a cost lever:** `max_tokens` directly controls how much Claude can write per call. Reducing it cuts cost. Increasing it improves output richness. As a PM thinking about unit economics on an API-powered product, this is the most direct dial you have. You identified this correctly in the assessment.

**On reducing API calls:** Consolidating prompts — combining multiple analysis dimensions into fewer calls — is the other major cost lever. Going from 10 calls to 5 cuts costs in half. This is a real optimization decision PMs make when scaling API-powered features.

**On what you built:** You can now say in an interview: "I built an agent that makes 5 chained API calls, validates user input, handles errors gracefully, and saves a formatted output file." When an engineer asks a follow-up, you can answer it. That's the PM bar — not memorizing syntax.

---

## Python Cheat Sheet — New This Week

| Syntax | Used for |
|---|---|
| `for item in list:` | Loop through every item in a list |
| `results = []` | Create an empty list |
| `results.append(x)` | Add item `x` to the end of the list |
| `"\n\n".join(list)` | Join list items into one string with blank lines between |
| `number = number + 1` | Increment a counter variable by 1 |

---

## Questions Royce Asked (with answers)

**"How would I run this py file in terminal?"**
`python3 business_intelligence_agent.py` — run from the folder where the file is saved. Use `cd` to navigate there first if needed.

**"What is the standard way of saving files?"**
All lowercase, underscores instead of spaces, no special characters. `business_intelligence_agent.py` is correct. Spaces in filenames cause terminal issues.

**"I feel overwhelmed by all the code. PMs don't have to be as technical to write this type of code, correct?"**
Correct. A PM's job is to understand what the code is doing well enough to have credible conversations with engineers, know what's possible when writing specs, and speak the language. The syntax fades — the mental model sticks. You now have the mental model.

---

## Assessment Results

**Score: 5.25/8**

| Question | Score | Notes |
|---|---|---|
| Q1 — Prompt chaining | 0.75/1 | Got the core right — missed the *why* (focused attention per call vs. shallow single prompt) |
| Q2 — Code reading | 2/2 | Perfect — loop count, second pass value, and `combined` description all correct |
| Q3 — Error handling | 1/1 | Correct — except fires, try block skipped, error message printed |
| Q4 — PM applied | 1.5/2 | Lever 1 (reduce tokens) spot on. Lever 2 had the right instinct but needed specificity: consolidate calls |
| Q5 — Code writing | 0/2 | Counter variable loop not attempted — syntax was the blocker, not the concept |

**Key gaps to carry into Week 8:**
- Counter variable syntax — `number = number + 1` inside a for loop. Revisit with a quick exercise.
- Q1 completion — when explaining prompt chaining, always include *why* it's better (focused attention per call)
- Q4 specificity — "evaluate whether each call is necessary" is the right instinct; the specific answer is "consolidate calls"

---

---

# PART 2 — Session Handoff

*For the next session's Claude. Read this before beginning Week 8.*

---

## Course Status
- **Week 1:** Complete ✓ — Score: 5.5/6
- **Week 2:** Complete ✓ — Score: 6.5/8
- **Week 3:** Complete ✓ — Score: 7/8
- **Week 4:** Complete ✓ — Score: 5.75/8
- **Week 5:** Complete ✓ — Score: 5.75/8
- **Week 6:** Complete ✓ — Score: 6.5/8
- **Week 7:** Complete ✓ — Score: 5.25/8
- **Week 8:** Polish, Document & Present — ready to begin

## What Was Covered in Week 7

Full build session — agent went from design to working code:

- **Warmup:** Execution tracing — closed the gap from Week 6. Royce explained code correctly but didn't trace to exact output. Corrected with the `.upper()` and `...` example.
- **User story practice (3 rounds):** Royce requested extra practice before moving on. Feedback: personas still descriptive rather than role-based; "so that" improving but still occasionally vague; good instinct on need vs. solution.
- **Part 1:** Architecture — single prompt vs. prompt chain, the 5-call structure, PM framing on quality/cost/latency tradeoffs
- **Part 2:** For loops and `.append()` — concept explained, quick check passed, built incrementally
- **Part 3:** Research Orchestrator — built the 4-call loop from a skeleton; Royce filled in the two key lines correctly
- **Part 4:** Synthesis Engine — built from skeleton; both lines correct first try
- **Part 5:** Output Writer — written from memory with strong recall; missed the terminal header print and placed `except` without `try`
- **Final assembly** — complete agent shown, saved to workspace as `business_intelligence_agent.py`
- **Live test** — ran on Wealthsimple, produced real brief, saved as `Wealthsimple_brief.txt`; Royce correctly identified token limit as cause of depth constraint (good product thinking)
- **Prompt update** — added Executive Summary section to synthesis prompt; Royce made the edit himself

## What Landed Well
- Loop concept clicked quickly — passed the quick check (4 loops, third pass = "key risks") correctly
- `.append()` — asked a great clarifying question ("does it mean put into?") and confirmed understanding immediately
- Synthesis engine lines — both correct first try, no prompting needed
- Live test observation — correctly identified token limit as the depth constraint; unprompted PM thinking
- Assessment Q2 and Q3 — perfect scores; code reading and error tracing are now solid
- The agent actually ran and produced a real brief — Royce saw it work

## What Was Harder
- Output Writer from memory — missed the terminal header print; `except` placed without `try`
- Q5 (counter variable) — couldn't start; syntax was the blocker. The concept was explained and understood but not internalised enough to write independently
- Motivation dipped at the end of the session — Royce flagged feeling overwhelmed by the code volume. Addressed with PM framing reassurance.
- User story personas — still defaulting to descriptive ("a user needing accurate information") rather than specific roles

## Tangents Explored
- File naming conventions — spaces vs. underscores, why underscores are standard
- Token limits as a cost lever — came up naturally from the live test; became a PM takeaways moment
- Whether PMs need to write this level of code — Royce asked directly; answered honestly (mental model matters, not syntax recall)

## Week 7 Files in Workspace
- `Week 7 Summary.md` — this file
- `business_intelligence_agent.py` — the complete working agent
- `Wealthsimple_brief.txt` — output from the live test run

## Gaps to Carry Into Week 8
- **Counter variable loop** — open Week 8 with a quick exercise: numbered list from a Python list. `number = 1` / `number = number + 1`. One minute, close it properly.
- **Proactive PM framing** — still occasionally reactive in applied scenarios. One coaching moment needed.
- **Motivation management** — Royce flagged feeling overwhelmed. Week 8 is lighter on new code (polish and documentation). Frame it that way upfront.

## Week 8 Setup Notes
- Week 8 is Polish, Document & Present — the final week
- Three deliverables: polished agent, one-page project brief (PM document), 5-minute verbal walkthrough
- GitHub setup is listed in the syllabus as a Week 8 task — worth checking if Royce has a GitHub account
- The agent is essentially complete; Week 8 is about packaging the work, not building new features
- Royce's code writing is solid enough — Week 8 is more PM writing and storytelling than Python
- Keep fintech framing throughout
- Read all Week 1–7 summaries before beginning — Royce flagged this as important
