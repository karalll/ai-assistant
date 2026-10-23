import asyncio

from groq import AsyncGroq

from ai_assistant.config import GROQ_API_KEY


async def ask_llm(message:str,client: AsyncGroq) -> str:
    
    

    response = await client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages =[
            {
                "role":"user",
                "content":message
            }
        ]
    )
    
    
    return response.choices[0].message.content


async def main():
    client = AsyncGroq(api_key=GROQ_API_KEY)
    while True:
        userInput = input()
        assistantAnswer = ""
        if (userInput.lower()!="stop" and userInput.lower()!="стоп"):
            if userInput.strip():
                assistantAnswer = await ask_llm(userInput, client)
                print(assistantAnswer)
                continue
            else:
                print("строка пуста") 
                continue
        else:

            print("программа завершилась")
            break

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())