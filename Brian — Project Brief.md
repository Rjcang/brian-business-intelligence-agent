# Brian — Business Intelligence Agent
### Project Brief | Royce Cang | June 2026

---

## Problem

Decision makers and researchers spend 15–20 minutes manually researching and organizing findings on a single company. When tracking multiple companies, that time adds up quickly which steals focus from deeper analysis of the ones that matter most.

---

## Solution

Brian, the Business Intelligence Agent, takes a company name as input and delivers a structured one-page brief in under 2 minutes. Brian covers business model, market position, key risks, opportunities, and recent developments. What would take a researcher 20 minutes to compile manually, Brian produces instantly, letting decision makers move faster and focus their time on companies worth digging into.

---

## How I Built It

Brian is built on four components:

1. The **Input Handler** prompts the user for a company name and validates the entry before proceeding.
2. The **Research Loop** goes through five analytical dimensions: business model, market position, key risks, opportunities, and recent developments — making a separate Claude API call for each and storing the responses.
3. The **Synthesis Engine** consolidates all five analyses into a single structured prompt, which Claude uses to produce the final brief.
4. The **Output Writer** formats the result and saves it as a text file.

---

## What I Learned

**1. AI can be molded around your needs to a degree most people don't expect.**
I used an AI workspace to build a custom curriculum fit to my learning style and pace — which itself became a demonstration of what's possible when you stop using AI as a search engine and start using it as a collaborator.

**2. APIs are the connective tissue of modern software.**
I now understand APIs and the unit economics behind them. Knowing how token pricing, model selection, and call structure affect cost gives me a framework for evaluating AI features as a PM — not just using them as a consumer.

**3. System prompts are a real product design surface.**
System prompts are how organizations encode their values, tone, and guardrails into an AI product. Understanding this changed how I think about AI product design — the prompt layer is where product decisions live, not just technical ones.

---

## What's Next

The most significant limitation of v1 is Claude's training data cutoff. The recent news and developments section carries inherent risk of being outdated, and the absence of live data means the brief cannot include current share prices, recent earnings, or breaking news. A v2 would integrate a live financial data API to ground the brief in real-time information. This would require a second API integration alongside the existing Claude API calls, turning Brian into a true multi-source orchestration layer.

On the presentation side, v2 would move beyond a plain text file to a formatted PDF or HTML brief — cleaner typography, structured layout, and ideally the company's logo pulled automatically. Content does not matter if people don't find it appealing enough to read through.

---

*Built by Royce Cang | Python · Claude API | June 2026*
