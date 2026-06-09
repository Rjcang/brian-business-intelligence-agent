from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

company = "Affirm"

prompt = f"""You are a Business Intelligence Assitant.
        Produce a structured one-page brief on {company} using the following sections:
        1. Company Overview: What problem the company is solving and who it serves (2-3 sentences)
        2. Business Model: How it makes money. Include main source and supplementary sources (if applicable)
        3. Key Products: Main products or features
        4. Competitive Landscape: 2-3 main competitors, how each company differentiates, and where they overlap
        5. Recent News or Trends: Anything notable in the last 1-2 years

        Be concise and factual. Format each section with its heading."""

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(message.content[0].text)
