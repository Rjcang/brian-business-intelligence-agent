# Week 4 Practice — Variables, Strings, and Lists
# AI Fluency Course | Royce | May 2026
#
# Instructions: Fill in each task below where you see the blanks.
# Lines starting with # are comments — Python ignores them.
# They're just notes for you.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# TASK 1 — Variables
# Create three variables:
#   - company_name: a company name of your choice (string)
#   - revenue: a made-up revenue figure (number)
#   - is_public: whether the company is publicly traded (True or False)
# Then print all three variables.
# ---------------------------------------------------------------

company_name = "Wealthsimple"       # ← replace the empty quotes with a company name
revenue = 1000             # ← replace 0 with a revenue figure
is_public = False         # ← type True or False (no quotes)

print(company_name)
print(revenue)
print(is_public)


# ---------------------------------------------------------------
# TASK 2 — F-strings
# Using your three variables above, print ONE sentence that
# combines all three naturally.
# Example output: "Shopify has revenue of $7100000000 and is a public company."
#
# Hint: use an f-string → f"some text {variable} more text"
# ---------------------------------------------------------------

print(f"{company_name} has a revenue of {revenue} and  is not publicly held.")  # ← build your sentence inside the quotes


# ---------------------------------------------------------------
# TASK 3 — Lists and Loops
# Create a list of three companies you'd want your Business
# Intelligence Agent to research.
# Then write a loop that prints a "Generating brief for: X"
# message for each company.
# ---------------------------------------------------------------

companies = ["Wealthsimple", "Freshbooks", "TurboTax"]  # ← add three company names inside the brackets

for company in companies:
    print(f"{company} has offices in Canada.")         # ← build your f-string print statement here
