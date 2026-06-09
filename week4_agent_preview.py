# Week 4 — Mini Business Intelligence Agent
# AI Fluency Course | Royce | May 2026
#
# This script stores data on three companies and prints a
# structured brief for each one.
#
# Your job: fill in the blanks marked with ←
# Then we'll run it together and see your agent in action.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# STEP 1 — Build your company database
# A list of dictionaries — each dictionary is one company's data card.
# Fill in real or made-up values for the two companies below Wealthsimple.
# ---------------------------------------------------------------

companies = [
    {
        "name": "Wealthsimple",
        "industry": "Fintech",
        "revenue": 10000,
        "is_public": False,
        "headquarters": "Toronto"
    },
    {
        "name": "FreshBooks",              # ← company name
        "industry": "Fintech",          # ← e.g. "E-commerce" or "SaaS"
        "revenue": 5000,            # ← made-up revenue figure
        "is_public": False,       # ← True or False
        "headquarters": "Toronto"       # ← city name
    },
    {
        "name": "Shopify",              # ← company name
        "industry": "E-commerce",          # ← e.g. "Fintech" or "Healthcare"
        "revenue": 20000,            # ← made-up revenue figure
        "is_public": True,       # ← True or False
        "headquarters": "Ottawa"       # ← city name
    }
]


# ---------------------------------------------------------------
# STEP 2 — Write the brief generator
# Loop through each company and print a structured brief.
# Fill in the blanks to complete the conditional and the print statement.
# ---------------------------------------------------------------

for company in companies:

    # Translate is_public into plain English
    if company["is_public"] == True:
        status = "publicly traded"
    else:
        status = "is not publicly traded"              # ← what should this say for private companies?

    # Print the brief
    print(f"Name Brief: {company['name']}")                          # ← which key gives us the company name?
    print(f"Industry: {company['industry']}")
    print(f"Headquarters: {company['headquarters']}")
    print(f"Revenue: ${company['revenue']}M")
    print(f"Status: {status}")                                            # ← what variable holds public/private status?
    print()                                                         # prints a blank line between briefs
