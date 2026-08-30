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
        print(chat.messages)
    elif b == 'stop':
        add_message(chat, 'user', b)



