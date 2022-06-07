# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

from random import choice

lottery_list = [0,1,2,3,4,5,6,7,8,9, 'a', 'b', 'c', 'd']

lottery_string = ''

for item in range(0,4):
    lottery_string += str(choice(lottery_list))

    num_of_tries = 0

while True:
    my_ticket_string = ''

    for item in range(0,4):
        my_ticket_string += str(choice(lottery_list))
        
    num_of_tries += 1

    if my_ticket_string == lottery_string:
        print(f'You had {num_of_tries} tries')
        break
