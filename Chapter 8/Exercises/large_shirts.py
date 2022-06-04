# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size, text):
    print(f"This is a {size}-sized shirt and it has '{text}' printed on it ")

make_shirt("large","I love Python")
make_shirt("medium","Monty Python")