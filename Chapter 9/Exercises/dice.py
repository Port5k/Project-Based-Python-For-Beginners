# 9-13. Dice: Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """A simple simulation of a die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"{randint(1, self.sides)}")

six_die = Die()
six_die.roll_die()

ten_die = Die()
ten_die.roll_die()

twenty_die = Die()
twenty_die.roll_die()

    