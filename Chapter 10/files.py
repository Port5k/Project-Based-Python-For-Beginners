# with open('pi_digits.txt') as file_object:
#  contents = file_object.read()
# print(contents.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''

# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

text = ''

filename = 'random_gibberish.txt'
with open(filename) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    text += line.strip()
print(text)
print(len(text))

name = input("Enter your name: ")
if name in text:
    print("eee0")
else:
    print("fff9")