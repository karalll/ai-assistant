from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str

class Chat(BaseModel):
    messages: list[Message]

def add_message(chat: Chat, message: str, role: Literal["system", "user", "assistant", "tool"] = "user") -> None:
    if message.strip():
        chat.messages.append(Message(role=role, content=message))
    else:
        raise ValueError("Message cannot be empty or whitespace.")