import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_llm():
    response = await client.responses.create(model="gpt-5.6",input="Объясни простыми словами, что такое API")
    print(response.output_text)

asyncio.run(ask_llm())