# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.

messages = [
    "Hello, what is going on?",
    "I really hope you are doing fine",
    "God bless you",
    "Hail and farewell, brother"
]

def show_messages():
    for message in messages: 
        print(message)

def send_messages(message_list):
    sent_messages_list = []
    for message in message_list:
        sent_messages_list.append(message)
    return sent_messages_list

print(send_messages(messages[:]))
print(send_messages(messages))

