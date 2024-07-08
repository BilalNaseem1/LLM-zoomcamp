from anthropic import Anthropic
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
client = Anthropic(api_key=ANTHROPIC_API_KEY)

prompt = "What's the formula for energy?"
# Send the request to the API
response = client.messages.create(
    model='claude-3-5-sonnet-20240620',
    max_tokens=1000,
    temperature=0.0,
    messages=[
        {"role": "user", "content": prompt}
    ]
)
# Print the response
print("Response:")
print(response.content[0].text)

# Print the number of output tokens
print(f"\nNumber of output tokens: {response.usage.output_tokens}")


# Extract the response text
# response_text = response['choices'][0]['text']
# print(f"Response from OpenAI: {response_text}")

# # Count the number of completion tokens
# completion_tokens = len(response_text.split())
# print(f"Number of completion tokens: {completion_tokens}")




