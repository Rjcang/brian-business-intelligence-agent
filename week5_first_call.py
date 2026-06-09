from dotenv import load_dotenv
import anthropic

# Step 1: Load the API key from the .env file
load_dotenv()

# Step 2: Create the connection to Claude
client = anthropic.Anthropic()

# Step 3: Send a message and store the response
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Give me a one-paragraph overview of Stripe as a fintech company."}
    ]
)

# Step 4: Pull the text out of the response and print it
print(message.content[0].text)
