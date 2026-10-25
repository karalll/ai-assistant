import asyncio

from groq import AsyncGroq, RateLimitError, AuthenticationError, APIConnectionError, APITimeoutError

from ai_assistant.config import GROQ_API_KEY


async def ask_llm(message:str,client: AsyncGroq) -> str | None:
    try:
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
    except RateLimitError:
        print("Лимиты закончились, подождите немного")
        return None
    except AuthenticationError:
            print("Ошибка авторизации")
            return None
    except APITimeoutError:
            print("Превышено время ожидания")
            return None
    except APIConnectionError:
            print("Ошибка соединения")
            return None
    except Exception:
            print("Непредвиденная ошибка")
            return None
    
    
    


async def main():
     async with AsyncGroq(api_key=GROQ_API_KEY) as client:
          
        while True:
            userInput = input()
            if (userInput.lower()!="stop" and userInput.lower()!="стоп"):
                if userInput.strip():
                    assistantAnswer = await ask_llm(userInput, client)
                    if assistantAnswer is None:
                        print("Запрос выполнен с ошибкой!")
                    else:
                        print(assistantAnswer)
                    continue
                else:
                    print("строка пуста") 
                    continue
            else:

                print("программа завершилась")
            
                break

if __name__ == "__main__":
    asyncio.run(main())