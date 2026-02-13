import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


response=client.chat.completions.create(
    model="gpt-5.2-chat-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ])

print(response.choices[0].message.content)












