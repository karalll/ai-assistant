from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    role: Literal['user','assistant','system','tool']
    content: str

class Chat(BaseModel):
    messages: list[Message]

chat = Chat(messages = [Message(
    role = 'user',
    content='Привет! Чем могу помочь?'),
    Message(role = 'user', content = 'WSP')
])

