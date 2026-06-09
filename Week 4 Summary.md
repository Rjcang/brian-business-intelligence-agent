# Week 4 Summary — Python for AI
### AI Fluency: Framework & Foundations | Royce | May 2026

---

# PART 1 — Student Study Guide

*Your reference doc. Re-read this before interviews, before Week 5, or whenever you need a refresher.*

---

## Key Concepts

### Why Python for AI?

Python became the language of AI for three reasons: it reads like plain English (low barrier for non-engineers), it has an unbeatable ecosystem of pre-built libraries, and network effects locked it in — every major AI company (Anthropic, OpenAI, Google) publishes their API in Python first. It's not the fastest language, but it won the AI race because researchers and builders converged on it early and the switching cost became too high. This is a great PM case study in how technical standards become sticky — the best tool doesn't always win, the most networked one does.

---

### The SQL → Python Bridge

Python isn't a new way of thinking — it's a new syntax for logic you already know from SQL. Every SQL concept has a Python equivalent:

| What you're doing | In SQL | In Python |
|---|---|---|
| Store a value | `SELECT 'Shopify' AS company` | `company = "Shopify"` |
| Store a list of things | A column with multiple rows | `companies = ["Shopify", "Stripe", "Square"]` |
| Filter with logic | `WHERE is_public = TRUE` | `if is_public == True:` |
| Do something repeatedly | Subqueries, JOINs across rows | `for company in companies:` |
| Store a structured record | A single row with multiple columns | A dictionary `{"name": "Shopify", "revenue": 7100}` |

---

### Variables

A variable stores a value and gives it a name so you can use it later.

```python
company_name = "Wealthsimple"   # string (text)
revenue = 1000                   # number
is_public = False                # boolean (True or False)
```

The left side is always the name. The right side is always the value. The `=` sign means *assign*, not *equal*.

---

### Strings and F-strings

A string is any text wrapped in quotes. Use double quotes by default; switch to single only if your text contains an apostrophe.

An f-string lets you drop variables directly into text — this is what you'll use to build prompts for Claude:

```python
company = "Wealthsimple"
print(f"Generating brief for: {company}")
# Output: Generating brief for: Wealthsimple
```

The `f` before the opening quote is the signal. Any `{}` inside inserts a variable.

---

### Lists

A list stores multiple values in order — like a column in a database table.

```python
companies = ["Wealthsimple", "Freshbooks", "Shopify"]
companies[0]   # "Wealthsimple" — Python counts from zero
```

Loop through a list with `for`:

```python
for company in companies:
    print(f"Generating brief for: {company}")
```

`company` is a temporary nickname Python creates for each item as it loops. You could call it anything — the convention is to use the singular of the list name.

---

### Dictionaries

A dictionary stores multiple labeled facts about one thing — like a single row in a database table with column names.

```python
company = {
    "name": "Wealthsimple",
    "revenue": 1000,
    "is_public": False,
    "headquarters": "Toronto"
}
```

Pull a value out by its key:

```python
print(company["name"])           # "Wealthsimple"
print(company["headquarters"])   # "Toronto"
```

**Important:** Always store numbers as numbers, not strings. `"revenue": 1000` not `"revenue": "$1000M"` — format for display in the f-string, not in the data.

---

### Conditionals

A conditional runs different code depending on whether something is true or false:

```python
if company["is_public"] == True:
    status = "publicly traded"
else:
    status = "not publicly traded"
```

`==` (double equals) is a comparison — it asks a question. `=` (single equals) is an assignment — it stores a value. Remember: `=` is a statement, `==` is a question.

The `else` branch runs automatically when the `if` condition isn't met — you don't need to write a second condition.

The conditional's job is to translate raw data (`True`/`False`) into human-readable language (`"publicly traded"`). Your agent will do this constantly.

---

### Putting It All Together

This is the skeleton of your Business Intelligence Agent:

```python
companies = [
    {"name": "Wealthsimple", "revenue": 1000, "is_public": False, "headquarters": "Toronto"},
    {"name": "Shopify", "revenue": 7100, "is_public": True, "headquarters": "Ottawa"}
]

for company in companies:
    if company["is_public"] == True:
        status = "publicly traded"
    else:
        status = "not publicly traded"

    print(f"--- Brief: {company['name']} ---")
    print(f"Revenue: ${company['revenue']}M")
    print(f"Status: {status}")
    print()
```

In Weeks 7-8, the hardcoded data gets replaced with a live Claude API call. The structure stays the same.

---

### Python Does the Math — Claude Does the Language

This is a critical distinction for any fintech PM. LLMs predict tokens — they don't compute. Simple arithmetic often *looks* correct because the model has seen millions of correct examples in training, but complex multi-step calculations drift.

**The rule:** Python handles any calculation. Claude handles language and reasoning.

Applied example: a debt-to-income ratio calculator. Python calculates the ratio. Claude writes the plain-English explanation. Never ask Claude to do the arithmetic.

This applies to any financial feature: risk scores, rate calculations, balance projections. Route the math to code, route the language to the model.

---

## The Python Cheat Sheet

| Symbol | Used for | Memory hook |
|---|---|---|
| `""` or `''` | Text (strings) | Wraps words in quotes like a sentence |
| `[]` | Lists | Square = sequence of items |
| `{}` | Dictionaries | Curly = structured card with labeled fields |
| `{}` inside `f"..."` | Insert a variable | The `f` before the quote is the signal |
| `=` | Assign a value | Statement — storing something |
| `==` | Compare two values | Question — is this true? |
| `[0]` | Access item by position | Python counts from zero |
| `dict["key"]` | Access dictionary value | Use the key name in square brackets |

---

## PM Takeaways

**On Python as a PM skill:** You don't need to become an engineer. You need to be able to read code, write small scripts, and build prototypes without waiting for engineering. Python is the tool that makes that possible — and it's the language of AI, so it's the most leveraged thing you can learn right now.

**On Python being "sticky":** Python won the AI race not because it's the best language technically, but because of network effects and switching costs. This is a live PM case study — understanding *why* an ecosystem is where it is helps you predict whether it's worth disrupting, and when to work with existing standards rather than against them.

**On the math/language divide:** In any fintech feature involving calculations, the PM's job is to know which tool is doing which job. Claude writes the explanation. Python runs the numbers. Getting this wrong ships a product that confidently produces incorrect financial figures — a serious risk in a regulated industry.

**On dictionary access:** When you call the Claude API in Week 5, its response comes back as a dictionary. You'll need to pull the actual text out by key. This is exactly the `company["name"]` pattern from this week — same concept, applied to API responses.

---

## Questions Royce Asked (with answers)

**"Why is Python the language of AI and not something else?"**
Python won because of three compounding forces: it reads like plain English (accessible to researchers without CS backgrounds), it has an unbeatable library ecosystem built over decades, and network effects locked it in once enough people adopted it. R, Julia, and JavaScript exist as alternatives but never reached critical mass. C++ runs under the hood of many AI libraries for speed — Python sits on top of it as the accessible interface.

**"Is there a reason you suggested Colab over Claude Code?"**
Colab is the lowest-friction starting point for learning Python — browser-based, zero setup. Claude Code is designed for developers working on real codebases, not learning environments. Either works; the Python is identical. For this course, writing directly in the workspace folder with live execution in-session turned out to be the most integrated option.

**"Can you read my files without me pasting?"**
Yes — direct access to the workspace folder means anything saved there can be read and run directly in session.

**"What do single vs. double quotes mean, and what's the difference between `[]` and `{}`?"**
See the cheat sheet above — saved here permanently at your request.

---

## Exercise Results

**week4_practice.py — Tasks 1-3:**
All three tasks completed correctly. Variables, f-strings, lists, and loops all ran without errors. Notably: correctly used `False` with a capital F (a common first-timer mistake); went off-script with the loop output ("has offices in Canada") which demonstrated genuine understanding rather than pattern copying. Task 2 hardcoded the public/private text rather than using `is_public` — correct instinct (Python wouldn't have done it automatically) and the exact gap that motivated learning conditionals in Part 3.

**week4_agent_preview.py — Mini Business Intelligence Agent:**
Completed successfully. Three company data cards built correctly, loop and conditional logic working, structured briefs printed for all three companies. Two polish notes: minor wording inconsistency in the `else` branch (`"is not publicly traded"` vs. `"not publicly traded"`), and label text inherited from the template. Neither broke the logic. The script ran and produced clean output.

---

## Assessment Results

**Score: 5.75/8**

| Question | Score | Notes |
|---|---|---|
| Q1 — = vs == | 0.75/1 | Concept correct; `[country]` syntax error and missing colon on if statement |
| Q2 — Code reading | 1.5/2 | Mechanics explained correctly; didn't state actual printed output |
| Q3 — Code writing | 0.5/2 | `[]` instead of `{}`, revenue stored as string, wrong variable reference for dictionary access |
| Q4 — Applied scenario | 2/2 | Strong — nailed the arithmetic/LLM argument clearly and confidently |
| Q5 — Connections | 1/1 | Correctly identified hardcoded data vs. live API call as the missing piece |

**Key gap to carry into Week 5:** Dictionary access — `company["key"]` syntax. The Claude API response is a dictionary. Pulling the text out of it by key is the first thing you'll do in Week 5, and it's exactly where Q3 broke down. Review the corrected Q3 answer before next session.

---

---

# PART 2 — Session Handoff

*For the next session's Claude. Read this before beginning Week 5.*

---

## Course Status
- **Week 1:** Complete ✓ — Score: 5.5/6
- **Week 2:** Complete ✓ — Score: 6.5/8
- **Week 3:** Complete ✓ — Score: 7/8
- **Week 4:** Complete ✓ — Score: 5.75/8
- **Week 5:** The Claude API — ready to begin

## What Was Covered in Week 4
Full lesson on Python for AI, delivered in four parts:
- Part 1: What Python is and why it matters for PM roles — history, network effects, the SQL bridge
- Part 2: Variables, strings, f-strings, lists, loops — with hands-on practice in the workspace
- Part 3: Dictionaries and conditionals — the structures that power AI responses
- Part 4: Mini Business Intelligence Agent — `week4_agent_preview.py`, a working script that loops through company data cards and prints structured briefs

## What Landed Well
- The SQL → Python bridge table — immediately reduced anxiety; Royce recognized the logic as familiar
- Writing and running code directly in the workspace (vs. Colab) — the integration clicked once set up; Royce explicitly appreciated it
- The "translation layer" explanation for conditionals (raw data → human-readable language) — resolved the Q2 Task 2 confusion cleanly
- Q4 (arithmetic/LLM split) — answered perfectly and confidently; this gap has now been closed after three appearances across the course
- Q5 (connections to final project) — Royce independently identified the hardcoded vs. live API distinction without prompting

## What Was Harder
- Dictionary syntax — Q3 showed three distinct errors: `[]` vs `{}`, storing revenue as a string, and dictionary key access (`company["key"]` vs. standalone variable). This is the most important gap going into Week 5.
- Tracing code output — Q2 explained mechanics correctly but didn't produce the actual printed output. Worth reinforcing in Week 5: "what does this print?" is a standard interview question.
- Saving files before reading — small workflow friction (had to prompt Royce to save before the file could be read). Not a learning gap, just a workflow note.

## Tangents Explored
- Why Python won the AI race vs. alternatives (R, Julia, JavaScript, C++) — answered fully; became a PM case study on network effects and switching costs
- Colab vs. Claude Code vs. in-session workspace — resolved in favor of in-session workspace; worked well
- Whether Claude can read workspace files directly — yes, confirmed and used throughout the session

## Royce's Profile Note
Royce corrected an error in memory this session: fintech is his *target* industry (aspiration), not his current background. He is coming from a general business background and wants to break into PM roles in fintech. Memory has been updated. Continue using fintech examples throughout the course — they're motivating and relevant to his goal.

## Gaps to Carry Into Week 5
- **Dictionary access** — `response["key"]` syntax is the first thing Royce will use when handling a Claude API response. Open Week 5 by revisiting the corrected Q3 pattern before introducing anything new.
- **Tracing output** — reinforce the habit of stating what code actually prints, not just explaining the mechanics.

## Week 5 Setup Notes
- Week 5 is The Claude API — making real API calls from Python
- The API response is a dictionary; Royce will need `response["content"]` or similar key access immediately
- Frame the API call as: "Remember the f-string you used to build a message? Now instead of printing it, you're sending it to Claude and getting a response back." The continuity is direct.
- The Business Intelligence Agent connection is now very close — Week 5 is what turns `week4_agent_preview.py` from a hardcoded demo into a real agent
- Read Week 1–4 summaries before starting — Royce has flagged this as important and noticed when it wasn't done
