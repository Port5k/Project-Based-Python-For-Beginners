# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

group_num = int(input("How many people are in your dinner group"))
if group_num > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready")