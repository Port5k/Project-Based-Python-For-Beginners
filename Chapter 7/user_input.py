# message = input("Tell me something and I'll repeat it back to you")
# print(message)

# name = input("Please,input your name:")
# print(f"\nHello, {name}")

# prompt = "If you tell us who you are, we can personalize the messages you see"
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print(f"\nHello, {name}")

# age = int(input("How old are you"))
# print(age >= 18)

# height = input("How tall are you, in inches?")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou will be able to ride when you are older")

# number = input("Enter a number and I'll tell you if it's even or odd")
# number = int(number)

# if number % 2 ==0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"\nThe number {number} is odd")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# prompt = "\nTell me something, and I will repeat it back to you"
# prompt += "\nEnter 'quit' to end the program"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# x = 1
# while x <= 5:
#     print(x)

#Start with users that need to be verified
# and an empty list tohold confirmed user
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
#Move each user into the list of confirmed users

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed user
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n... Poll Results...")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")

