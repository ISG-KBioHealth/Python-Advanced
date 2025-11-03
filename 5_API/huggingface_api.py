# https://huggingface.co/docs/inference-providers/guides/responses-api

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

response = client.responses.create(
    model="openai/gpt-oss-120b:groq",
    instructions="You are a helpful assistant.",
    input="Tell me a three-sentence bedtime story about a unicorn.",
)

print(response.output_text)
