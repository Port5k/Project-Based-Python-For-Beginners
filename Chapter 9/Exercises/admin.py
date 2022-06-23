# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:
    """Defines a new user"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old")

    def greet_user(self):
        print(f"Hello, {self.first_name}")


class Privileges:

    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()



my_admin = Admin('Pablo', 'Estivia', 34)
my_admin.describe_user()
my_admin.privileges.show_privileges()