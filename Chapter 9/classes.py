# class Dog:
#     """A simple attempt to model a dog"""

#     def __init__(self, name, age):
#         """Initailize name and age attributes"""
#         self.name = name
#         self.age  = age
    
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over")

# my_dog = Dog('Willie', 6)

# print(f"My dog's name is {my_dog.name}")
# print(f"My dog's age is {my_dog.age}")
# my_dog.sit()
# my_dog.roll_over()

# your_dog = Dog('Lucy',3)

# print(your_dog.name.capitalize())
# print(your_dog.age * 34)

class Car: 
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading  = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Print a message showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if tit attempts to roll the odometer back.
        """
        if  mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """FIll gas tank"""
        print("The gas tank is filled ")




# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # my_new_car.odometer_reading = 34
# my_new_car.read_odometer()
# my_new_car.update_odometer(-22)
# my_new_car.read_odometer()

# my_used_car = Car('Subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

class Battery:
    """A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size=75):
        """"Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100: 
            range = 315

        print(f"This car can go about {range} miles on a full charge")
        


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__( make, model, year)
        self.battery = Battery()
        
    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")



# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# print(my_tesla.read_odometer())
# my_tesla.update_odometer(34)
# print(my_tesla.read_odometer())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


from random import randint, choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print(choice(players))

# print(randint(1,6))