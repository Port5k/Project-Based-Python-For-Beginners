# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = {
    'john': ['zimbabwe','harare','banjul'],
    'mary':['malawi','helsinki'],
    'zoe':['finland']
}

for person,location in favorite_places.items():
    print(f"{person}'s favorite place(s) is/are :")
    for places in location:
        print(f"\t{places}")