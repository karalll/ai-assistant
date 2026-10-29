import asyncio

from groq import (
    APIConnectionError,
    APITimeoutError,
    AsyncGroq,
    AuthenticationError,
    RateLimitError,
)

from ai_assistant.config import GROQ_API_KEY
from ai_assistant.models import Chat, Message, add_message


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
    except Exception:  # noqa: BLE001
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