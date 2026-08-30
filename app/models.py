from typing import Literal

from pydantic import BaseModel

class Message(BaseModel):
    role: Literal['user','assistant','system','tool']
    content:str

class Chat(BaseModel):
    messages:list[Message]

def add_message(chat:Chat,role:Literal['user','system','assistant','tool'], content:str):
    chat.messages.append(Message(role = role, content = content))
