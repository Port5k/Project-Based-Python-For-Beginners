# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pets = [
    {
        'animal':'cat',
        'owner':'john'
    },
    {
        'animal':'rat',
        'owner':'mary'
    },
    {
        'animal':'goat',
        'owner':'bambi'
    },
    {
        'animal':'sheep',
        'owner':'jane'
    },
    {
        'animal':'toad',
        'owner':'neville'
    }
]

for pet in pets: 
    print(f"The owner of the {pet['animal']} is {pet['owner'].title()}")