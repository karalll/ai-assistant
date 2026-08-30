import json

from app.models import Chat, Message, add_message

chat = Chat(messages =[Message(
    role = 'assistant',
    content='Чем могу помочь?'
)
])
question = ''
while question!= 'stop':
    print('user:', end = '')
    b = input()
    question = b
    if(b != 'stop'):
        add_message(chat, 'user',b)
        add_message(chat,'assistant','Запрос принят')
        print(f'{chat.messages[-1].role}: {chat.messages[-1].content}')
    elif b == 'stop':
        add_message(chat, 'user', b)

chat.model_dump()
print(f'ВЕСЬ ЧАТ: \n\n{chat}')

