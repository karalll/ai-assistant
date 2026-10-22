from models import Chat, add_message


chat = Chat(messages=[])

while True:
    userInput = input("Enter your message: ")
    if userInput.lower() == "exit" or userInput.lower() == "стоп":
        add_message(chat, "Выход из чата", role="system")
        print("Exiting the chat.")
        break
    else:
        if userInput.isspace() or userInput == "":
            add_message(chat, "Пустое сообщение", role="system")
            print("Empty message. Please enter a valid message.")
        else: 
            add_message(chat, userInput, role="user")
            userInput = input("Enter your message: ")
print(chat.model_dump_json())