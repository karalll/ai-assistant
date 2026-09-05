import asyncio
import os

from models import Chat, Message, add_message
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY")
)


async def ask_llm():
    
    while True:
        textFromUser = input()
        if textFromUser.lower() != 'stop' and textFromUser.lower() !='стоп': 
            response = await client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "user",
                            "content": textFromUser
                        }
                    ]
                )
            print(response.choices[0].message.content)
        else: break
    


asyncio.run(ask_llm())