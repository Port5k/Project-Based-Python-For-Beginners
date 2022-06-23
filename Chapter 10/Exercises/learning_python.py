# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

with open("python_text.txt") as my_file:
    my_file_content = my_file.read()
    print(my_file_content)

with open("python_text.txt") as my_file:
    for line in my_file:
        print(line.strip())

file_string = ''

with open("python_text.txt") as my_file:
    file_array = my_file.readlines()

for line in file_array:
    if "Python" in line:
        line.replace("Python", "JavaScript")
        
    print(line.strip())