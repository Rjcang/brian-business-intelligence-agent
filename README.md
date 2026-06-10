# Brian — Business Intelligence Agent

Brian takes a company name as input and delivers a structured one-page business intelligence brief in under 2 minutes in other words: 90% time saved.

What would take a researcher 20 minutes to compile manually, Brian produces instantly — covering business model, market position, key risks, opportunities, and recent developments.

---

## What Brian Produces

- Executive Summary
- Company Overview
- Business Model
- Market Position
- Key Risks
- Opportunities
- Recent News & Developments
- Sources

Output is saved as a `.txt` file in the same folder where the script is run.

---

## How to Run It

**1. Clone the repo**
```
git clone https://github.com/Rjcang/brian-business-intelligence-agent.git
cd brian-business-intelligence-agent
```

**2. Install dependencies**
```
pip install anthropic python-dotenv
```

**3. Add your Anthropic API key**

Create a `.env` file in the project folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```

Get your API key at [console.anthropic.com](https://console.anthropic.com)

**4. Run the agent**
```
python3 bi_agent.py
```

Enter a company name when prompted. Brian will analyze it and save the brief as `[company]_brief.txt`.

---

## Built With

- Python
- [Claude API](https://www.anthropic.com) (claude-haiku-4-5-20251001)
- anthropic Python SDK
- python-dotenv

---

## Project Brief

For a full breakdown of the problem, solution, architecture, and what's next — see [Brian — Project Brief.md](Brian%20%E2%80%94%20Project%20Brief.md).

---

*Built by Royce Cang | June 2026*
