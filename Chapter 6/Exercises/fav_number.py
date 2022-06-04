# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

fav_numbers = {
    "John": 33,
    "Mary": 22,
    "Tolu": 36,
    "Shege": 93,
    "Olu":92,
}

for people, fav_number in fav_numbers.items():
    print(f"{people}'s favorite number is {fav_number}")