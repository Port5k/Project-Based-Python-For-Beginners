# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not

number = int(input("Please, input a number"))

def check_number(num):
    if(num == 10):
        return True
    elif(num < 0):
        return False
    else:
        return check_number(num - 10)

print(check_number(number))