from app.models import Chat, Message

chat = Chat(messages = [
    Message(
        role = 'user',
        content = 'Что такое AI агент?'
        ),

    Message(
        role = 'assistant',
        content = 'Чтобы то-то то-то итд'
        )
        ])
for message in chat.messages:
    print(f'{message.role} :{message.content}')

