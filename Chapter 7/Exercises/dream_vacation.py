# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

while True:
    prompt = input("Where is your dream vacation location?: ")
    if prompt == 'quit':
        break
    else:
        print(f"Your dream vac is in {prompt}")