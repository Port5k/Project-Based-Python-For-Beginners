# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

messages = [
    "Hello, what is going on?",
    "I really hope you are doing fine",
    "God bless you",
    "Hail and farewell, brother"
]

def show_messages():
    for message in messages: 
        print(message)

show_messages()