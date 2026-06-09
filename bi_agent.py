from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

# Input Handler

company = input("Enter the name of a company you want to learn about: ")

if company == "":
    print("No company name entered. Please try again.")
elif len(company) < 2:
    print("Please enter a valid company name.")
else:
    dimensions = ["business model", "market position", "key risks", "opportunities", "recent news and developments"]
    results = []

    #Research Loop
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

        #Synthesis Engine
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
6. News and Developments
7. Sources: List 2-3 sources or data points that would support this analysis (e.g. company reports, news articles, industry data).

End the brief with a short caveat of when the information is from (to account for the cut-off date for training models.
"""

        #Output Writer
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

