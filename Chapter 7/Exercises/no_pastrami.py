# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches

sandwiches = ['pepperoni','pastrami', 'pastrami','tuna','pastrami', 'PB & J']
finished_sandwiches = []

while sandwiches:
    while  'pastrami'in sandwiches:
        sandwiches.remove('pastrami')
    current_sandwich = sandwiches.pop()
    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)