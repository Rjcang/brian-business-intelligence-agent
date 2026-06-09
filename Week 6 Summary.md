# Week 6 Summary — Designing Your Agent
### AI Fluency: Framework & Foundations | Royce | June 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 7, or whenever you need a refresher.*

---

## Warmup Recap — Closing Week 5 Gaps

### `print(prompt)` vs. a Claude Response

This was the gap flagged from Week 5 and it was closed cleanly at the start of Week 6.

```python
company = "Wealthsimple"
prompt = f"Give me a one-paragraph overview of {company} as a fintech company."
print(prompt)
```

What gets printed: the prompt string itself — `"Give me a one-paragraph overview of Wealthsimple as a fintech company."` — not a Claude response. Claude was never called. There is no `client.messages.create()` in this script.

**The mental check:** Does the script contain `client.messages.create()`? If not, Claude was never contacted. `print(prompt)` prints the question, not the answer.

The two steps are completely separate:
```
Step 1 — Build the prompt:    prompt = f"Give me an overview of {company}..."
Step 2 — Send it to Claude:   message = client.messages.create(... "content": prompt ...)
Step 3 — Print the response:  print(message.content[0].text)
```

---

### Syntax Bugs to Know Cold

Two recurring bugs identified and drilled:

**Bug 1 — `load_dotenv` without `()`**
```python
load_dotenv    # WRONG — refers to the function, doesn't call it
load_dotenv()  # CORRECT — actually calls it
```
Without `()`, Python sees the function name but never executes it. The `.env` file never gets read, the API key never loads, and the very next line fails with an authentication error. The analogy: writing someone's name on a notepad vs. actually picking up the phone and calling them.

**Bug 2 — String values without quotes**
```python
company = Wealthsimple   # WRONG — Python looks for a variable named Wealthsimple
company = "Wealthsimple" # CORRECT — quotes tell Python this is text data
```
Without quotes, Python looks for a variable called `Wealthsimple`. No such variable exists → `NameError: name 'Wealthsimple' is not defined`. Quotes are what distinguish text data from variable names.

---

## What Makes Something an Agent?

### Chatbot vs. Agent

These terms are used loosely in the industry. Here's the precise distinction:

A **chatbot** waits for you to ask something, answers it, and stops. Every turn is independent. It has no goal of its own.

An **agent** is given a *goal* and figures out the steps to reach it on its own.

**The fintech analogy:**
- A bank's FAQ chatbot answers one question at a time — "What's my balance?" → answer. Fresh start each time. No goal.
- A financial advisor takes a goal — "I want to retire at 55 with $2M" — and acts: pulls savings, researches options, runs projections, flags risks, delivers a plan. Used the result of one step to inform the next. Produced a deliverable.

### The Four Things That Make Something an Agent

| Capability | Chatbot | Agent |
|---|---|---|
| Takes a goal, not just a command | ✗ | ✓ |
| Breaks the goal into steps | ✗ | ✓ |
| Uses one result to inform the next | ✗ | ✓ |
| Produces a final deliverable | ✗ | ✓ |

Your Business Intelligence Agent hits all four:
1. **Goal:** "Tell me everything useful about Stripe"
2. **Steps:** Analyze business model → market position → risks → opportunities
3. **Chaining:** The synthesis step reads all four analyses before writing the final brief
4. **Deliverable:** A formatted one-page brief saved as a file

---

## User Stories

### What a User Story Is

A user story is a one-sentence description of what a feature does, written from the user's perspective. It translates a raw customer requirement (messy, informal, how users actually talk) into a structured, testable format a team can build against.

**The format:**
> *As a [who], I want to [do what], so that [why / what value it creates].*

**The flow:**
> Customer requirement (raw user pain) → User story (structured PM translation)

### What Makes a User Story Good

**Strong persona** — "As a VC researcher reviewing 20 companies a week" is useful. "As a user" tells engineering nothing.

**Need, not solution** — the "I want" should describe what the user needs, not how to build it. Solutions sneak in as specific implementation details:
- ❌ "I want spaces between sections" (solution — prescribes how)
- ✓ "I want the brief to be clearly formatted with distinct sections" (need — describes what)

**Specific "so that"** — the value should be testable and name the real cost if the feature doesn't exist:
- ❌ "so that I can learn about the company" (vague, untestable)
- ✓ "so that I can assess a company before making an investment decision" (specific, testable)

### Two Ways to Mis-Translate a Requirement

**Under-translation** — too vague. "As a user, I want the tool to work, so that it gives me information." Could describe any software.

**Over-translation** — adds features the user didn't ask for. A user says "I don't want to restart the program between companies" and you write a user story about automatic sector comparison. You've invented a bigger feature. Stay faithful to what was said.

### User Story Examples (from session practice)

| Requirement | Good User Story |
|---|---|
| "I can't tell where sections begin and end" | As a user, I want the brief to be clearly formatted with distinct sections, so that I can quickly scan and read each part without losing my place. |
| "I'd be embarrassed if it crashed mid-demo" | As a presenter, I want the agent to handle invalid or empty input without crashing, so that I can demo it confidently without worrying about it breaking in front of others. |
| "Half the companies I research aren't public — it shouldn't make things up" | As a researcher in private equity, I want the agent to acknowledge when it has insufficient information, so that I don't make investment decisions based on fabricated data. |
| "I don't want to type the same 10 companies every day" | As a hedge fund analyst, I want to run the tool against the same set of companies automatically each morning, so that I save time and avoid typing errors. |

### The Key Tension: Requirements vs. Solutions

User stories describe *what* the user needs, not *how* it gets built. The moment words like "spaces," "guards," "save a list," or "search box" appear in the "I want," you've crossed from requirements into design decisions. Keeping those separate preserves optionality for the team doing the building — and is one of the most valuable PM habits you can develop.

---

## Flow Diagrams

A flow diagram maps every step your agent takes from start to finish — including decision points and failure paths. It forces you to think through the entire experience before writing code, and becomes the spec you build from.

**Decision points** are where the flow splits into two paths — usually a check that determines whether to continue or handle an error.

### Your Agent's Complete Flow

```
Start: User runs the script
    ↓
1. Agent prompts user to enter a company name [input()]
2. Agent checks: was anything entered?
   → If empty: display error message, exit cleanly
   → If valid: continue
3. Agent loads .env file, retrieves API key
4. Agent initializes Anthropic client
5. Agent builds structured prompt using company name
6. Agent sends prompt to Claude API
   → If API call fails: display error message, exit gracefully
   → If successful: continue
7. Agent receives response from Claude
8. Agent formats the output
9. Agent saves formatted brief to a .txt file automatically
10. Agent tells user: "Brief saved as [filename]"

End: User finds their brief saved in the folder
```

Two decision points (Steps 2 and 6), two graceful exits. No crashes, no red text.

---

## `input()` — Getting User Input

### What It Does

`input()` pauses the script and waits for the user to type something and hit Enter. Whatever they type gets stored in a variable.

```python
company = input("Enter a company name: ")
```

- `input()` — pauses and waits
- `"Enter a company name: "` — the message shown to the user in the terminal
- `company =` — stores whatever the user types

After this line runs, `company` works exactly like `company = "Stripe"` — you drop it straight into your f-string and nothing else changes.

**The SQL analogy:** `input()` is like a parameter query. Instead of hardcoding the value (`WHERE name = 'Stripe'`), you collect it at runtime (`WHERE name = ?`). The placeholder gets filled when the script runs.

### Important: `input()` Always Returns a String

Whatever the user types — even if they type a number — Python stores it as text. For company names this is perfect. In other contexts (e.g., a user entering an amount of money) you'd need to convert it, but for your agent it just works.

### Validating Input

What if the user hits Enter without typing anything? Guard against it:

```python
company = input("Enter a company name: ")

if company == "":
    print("No company name entered. Please try again.")
else:
    # rest of your script runs here
```

- `company == ""` — two empty quotes = an empty string = user hit Enter without typing
- The entire `else` block is skipped if company is empty — no prompt built, no API called, no credits wasted

---

## Output Formatting

Making the brief readable before saving it.

```python
print("\n" + "="*60)
print(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}")
print("="*60 + "\n")
print(message.content[0].text)
```

- `"\n"` — newline character, adds a blank line
- `"="*60` — prints 60 equals signs (Python lets you multiply strings)
- `company.upper()` — converts the company name to ALL CAPS

Terminal output looks like:
```
============================================================
BUSINESS INTELLIGENCE BRIEF — WEALTHSIMPLE
============================================================

1. Company Overview: Wealthsimple is a Canadian...
```

---

## Saving to a File

### Writing the Brief to a `.txt` File

```python
filename = f"{company}_brief.txt"

with open(filename, "w") as f:
    f.write(f"BUSINESS INTELLIGENCE BRIEF — {company.upper()}\n")
    f.write("="*60 + "\n\n")
    f.write(message.content[0].text)

print(f"Brief saved as {filename}")
```

Line by line:
- `filename = f"{company}_brief.txt"` — creates a dynamic filename like `Wealthsimple_brief.txt`
- `with open(filename, "w") as f` — opens a file for writing; creates it if it doesn't exist
- `"w"` — write mode: starts fresh every time (see File Modes below)
- `f.write(...)` — writes a string to the file, like `print()` but to a file instead of the terminal
- `"\n"` — adds a new line inside the file
- Final `print()` — tells the user where their file was saved

**The SQL analogy:** `with open(filename, "w") as f` is Python's version of a database write operation. Instead of `INSERT INTO table`, you're inserting content into a file.

### File Modes

| Mode | What it does |
|---|---|
| `"w"` | Write — creates a fresh file, overwrites if it already exists |
| `"a"` | Append — adds to the end of an existing file |
| `"r"` | Read — reads the file, cannot modify it |

**Important:** `"w"` is destructive. If you run your agent twice for the same company, the second run overwrites the first. For your current project that's fine. For a higher-volume use case (like the VC researcher from the user story exercises), you'd add a timestamp to the filename to prevent overwriting:

```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{company}_{timestamp}_brief.txt"
```

---

## Error Handling with `try` and `except`

### What It Is

`try/except` is Python's safety net. You wrap code that might fail inside `try`, and tell Python what to do if it fails inside `except`.

```python
try:
    # code that might fail
except Exception as e:
    # what to do if it fails
```

**The fintech analogy:** A Wealthsimple kiosk tries to connect to a server. Two outcomes:
- Connection works → brief loads, everything fine
- Connection fails → without error handling: black screen crash. With error handling: "Unable to connect. Please check your internet and try again."

Same failure. Completely different user experience.

### Wrapping the API Call

The API call is the most important place to add error handling — it requires internet, a valid API key, and Anthropic's servers to be running. Any of those can fail.

```python
try:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(message.content[0].text)

except Exception as e:
    print(f"Something went wrong: {e}")
    print("Please check your API key and internet connection.")
```

- `Exception as e` — catches any error and stores the error message in variable `e`
- `f"Something went wrong: {e}"` — prints the actual error using an f-string so you know what happened

### What Happens When Each Guard Triggers

**Empty input guard (Step 2):**
- `if company == "":` runs → friendly message prints → `else` block is skipped entirely
- No prompt built, no API called, no credits wasted, no crash

**API failure guard (Step 6):**
- `except` block runs → friendly error message prints → script exits cleanly
- No crash, no red text, no embarrassing moment mid-demo

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
    prompt = f"""You are a business intelligence assistant.
Produce a structured one-page brief on {company} using the following sections:

1. Company Overview: What the company does and who it serves (2-3 sentences)
2. Business Model: How it makes money
3. Key Products: Main products or features
4. Competitive Landscape: 2-3 main competitors
5. Recent News or Trends: Anything notable in the last 1-2 years

Be concise and factual. Format each section with its heading."""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
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

This is a real, working agent — not a practice script.

---

## PM Takeaways

**On user stories as a PM tool:** User stories are how you translate messy customer requirements into precise, buildable specifications. The discipline of keeping requirements separate from solutions — and making the "so that" specific enough to test — is one of the most valuable habits you can bring to a PM role. You wrote 12 of them today. That calibration is now in your muscle memory.

**On flow diagrams as specs:** Mapping the flow before writing code forces you to confront edge cases you'd otherwise discover only when something breaks in front of someone. Every decision point you add to a diagram is a crash you prevent in the product.

**On error handling as product thinking:** Adding `try/except` isn't just a coding task — it's a design decision. Anticipating failure states before writing a single line of code is exactly what distinguishes PM-led development from pure engineering. In a demo context, graceful failure handling is the difference between "this person thinks like a product person" and "this is a fragile script."

**On wasted API calls:** Empty input that reaches the API is a real cost. Every unnecessary call burns credits. As a PM thinking about unit economics on an API-powered product, protecting your API calls with input validation is both a UX decision and a cost decision. You're now doing both.

**On the agent being essentially complete:** The script above is your Business Intelligence Agent. Week 7 extends it with multiple analysis dimensions and a synthesis step. Week 8 polishes and packages it. The hard architectural work is done.

---

## Questions Royce Asked (with answers)

**"User stories are usually derived from customer requirements, right?"**
Yes — exactly right. The flow is: customer requirement (raw user pain, how users actually talk) → user story (structured PM translation). The requirement is what you hear in user research or support tickets. The user story is how you translate it into something a team can build and test against.

**"Isn't 'saving a list' a new feature — a solution sneaking in?"**
Yes — sharp catch. "Save a list" prescribes a specific implementation. The better approach is to describe the capability without specifying how it works: "run the tool against the same set of companies automatically each morning." That's specific enough to be testable, open enough that engineering decides whether it's a saved list, a config file, a scheduled task, or something else.

---

## Assessment Results

**Score: 6.5/8**

| Question | Score | Notes |
|---|---|---|
| Q1 — Agent vs. chatbot | 0.75/1 | Strong agent definition and excellent IPO tracking example — missed the chatbot example |
| Q2 — User story from requirement | 1.5/2 | Strong persona and "so that" — "I want" described the pain rather than the desired capability |
| Q3 — Code reading | 1.5/2 | Good line-by-line explanation — didn't trace the specific output when user types "affirm" → AFFIRM |
| Q4 — Code writing | 2/2 | Perfect — clean structure, correct f-string, correct empty check |
| Q5 — Applied scenario | 0.75/1 | Got the mechanics right — PM framing could have been more proactive (you *designed* for failure, not just handled it) |

**Key gaps to carry into Week 7:**
- Always trace specific execution paths when asked "what does the terminal show" — give the actual output, not just the explanation
- When no chatbot/agent example is explicitly given, provide both
- In PM framing, lead with the proactive angle: "I anticipated this failure during design" is stronger than "hopefully the script handles it"

---

## The Python + Agent Cheat Sheet

| Syntax | Used for |
|---|---|
| `input("message")` | Pause script, collect user input, store as string |
| `if company == "":` | Check if user entered nothing |
| `"="*60` | Print 60 equals signs (string multiplication) |
| `company.upper()` | Convert string to ALL CAPS |
| `"\n"` | New line character |
| `open(filename, "w")` | Open a file for writing (creates if doesn't exist) |
| `f.write("text")` | Write a string to an open file |
| `try:` | Wrap code that might fail |
| `except Exception as e:` | Catch any error, store message in `e` |
| `f"...{e}..."` | Print the error message using an f-string |

---

---

# PART 2 — Session Handoff

*For the next session's Claude. Read this before beginning Week 7.*

---

## Course Status
- **Week 1:** Complete ✓ — Score: 5.5/6
- **Week 2:** Complete ✓ — Score: 6.5/8
- **Week 3:** Complete ✓ — Score: 7/8
- **Week 4:** Complete ✓ — Score: 5.75/8
- **Week 5:** Complete ✓ — Score: 5.75/8
- **Week 6:** Complete ✓ — Score: 6.5/8
- **Week 7:** Building Your Agent — ready to begin

## What Was Covered in Week 6
Full lesson on agent design, delivered in five parts plus warmup:

- **Warmup:** `print(prompt)` vs API response — gap from Week 5 now fully closed. Syntax bugs drilled: `load_dotenv` without `()`, string without quotes.
- **Part 1:** What makes an agent — four criteria, chatbot vs. agent distinction, fintech analogy
- **Part 2:** User stories — 12 rounds of practice translating requirements to user stories, the requirement→story flow, need vs. solution discipline, over-translation vs. under-translation
- **Part 3:** `input()` — user input function, always returns string, empty input validation with `if/else`
- **Part 4:** Output formatting and file saving — `"\n"`, `"="*60`, `.upper()`, `open()`, `f.write()`, file modes (`"w"`, `"a"`, `"r"`)
- **Part 5:** Error handling — `try/except`, `Exception as e`, graceful exits for empty input and API failure
- **Complete agent script** assembled and reviewed end to end

## What Landed Well
- The chatbot vs. agent distinction — the IPO tracking example Royce gave in the assessment was genuinely impressive; showed real product thinking
- User story practice — 12 rounds. By round 10–12 personas and core needs were consistently strong; the "so that" calibration noticeably improved
- The sharp catch on "saving a list" being a solution — unprompted, demonstrated genuine internalisation of the need vs. solution principle
- `input()` — clicked immediately, answered the quick check correctly first try
- `try/except` analogy (kiosk) — resolved initial confusion cleanly
- Q4 code writing — perfect score, clean syntax, no errors

## What Was Harder
- Tracing specific execution paths — recurring pattern from Week 5. When asked "what does the terminal show when the user types X?", Royce explains the code well but doesn't always trace through to the specific output. Worth a targeted warmup in Week 7.
- User story "so that" precision — improved significantly through practice but still occasionally undersells the real cost ("find comfort" vs. "verify before acting on it")
- PM framing in applied scenarios — gets the mechanics right but frames answers reactively ("hopefully it handles it") rather than proactively ("I designed for this failure"). One coaching prompt needed in Week 7 to shift that frame.

## Tangents Explored
- Whether "saving a list" counts as a solution in a user story — yes, sharp catch by Royce, became a good teaching moment about the need/solution boundary
- Offline capability constraint — Requirement 12 raised the tension between user needs and technical constraints (API requires internet); discussed that the faithful translation is "access previously saved briefs offline" not "generate new briefs offline"

## Week 6 Files in Workspace
- `Week 6 Summary.md` — this file
- No new `.py` files this week — Week 6 was design-focused; the complete agent script was reviewed but not saved separately (it will be built properly in Week 7)

## Gaps to Carry Into Week 7
- **Execution tracing** — open Week 7 with a warmup: "what does the terminal show step by step?" on a short script. Royce needs to give the actual output, not just explain the code.
- **Proactive PM framing** — when Royce answers applied scenarios, prompt him to lead with "I designed for this" rather than "hopefully it handles it"
- **The complete agent is the foundation** — Week 7 extends it with multiple Claude calls (one per analysis dimension), a loop, and a synthesis step. The Week 6 script is the starting point.

## Week 7 Setup Notes
- Week 7 is Building Your Agent — four components: input handler, research orchestrator (loop through 4 analysis dimensions), synthesis engine, output writer
- The Week 5 `week5_practice.py` and the Week 6 complete agent script are both in the workspace; Week 7 builds on these
- Royce's code writing is now strong enough to write significant portions from scratch — give him build challenges, don't just show him finished code
- Continue fintech examples throughout
- Read all Week 1–6 summaries before beginning — Royce flagged this as important
