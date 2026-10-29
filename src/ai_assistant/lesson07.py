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


async def ask_llm(message:str, client: AsyncGroq, chatHystory:Chat) -> str|None:
    if message.strip():
         add_message(chatHystory, message, "user")
    else:
         return None
    dumpingObject = [item.model_dump() for item in chatHystory.messages]
    
    
    try:
        response = await client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages = dumpingObject
        )
        add_message(chatHystory, response.choices[0].message.content, "assistant")
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
    chat = Chat(messages=[])
    async with AsyncGroq(api_key=GROQ_API_KEY) as client:
        while True:
            userInput = input()
            if userInput.lower() != "stop" and userInput.lower() != "стоп":
                if userInput.strip():
                    assistantAnswer = await ask_llm(userInput, client, chat)
                    if assistantAnswer != None:
                        print(assistantAnswer)
                        continue
                    else:
                        print("Ответ модели выдал ошибку!")
                        continue
                else:
                    print("Вы ввели пустую строку")
                    continue
            else:
                print("Программа завершена")
                break

if __name__ == "__main__":
    asyncio.run(main())