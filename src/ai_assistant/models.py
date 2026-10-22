from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str 

message1 = Message(role = "system", content = "Привет, чем могу помочь")
message2 = Message(role = "user", content = "Привет, как дела?")

class Chat(BaseModel):
    messages: list[Message]

chat = Chat(messages = [message1, message2])
print("Первый тест: " + len(chat.messages))

def add_message(chat: Chat, message: str):
    if message.isspace() or message == "":
        raise ValueError("Message content cannot be empty or whitespace.")
    else: 
        chat.messages.append(message)

message3 ="все норм"
add_message(chat, message3)
print("Второй тест" + len(chat.messages))






#1 task
# message = Message(role = "user", content = "Привет")
# print(f"{message.role}: {message.content}")