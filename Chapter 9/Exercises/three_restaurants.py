# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name} and we specialize in {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

afrika_kitchen = Restaurant('Afrika Kitchen', "African Cuisine")
afrika_kitchen.describe_restaurant()
continental = Restaurant('Kontinental', "Continental Cuisine")
continental.describe_restaurant()
local = Restaurant('Local Kitchen', "Local Cuisine")
local.describe_restaurant()