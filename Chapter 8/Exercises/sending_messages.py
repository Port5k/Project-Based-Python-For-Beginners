# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
 

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

print(send_messages(messages))
