# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello! {username}")

# greet_user("dawg")

# def describe_pet( pet_name,animal_type):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()

# def get_formatted_name(first_name, last_name): 
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name("jimi","hendrix")
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=""):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def build_person(first_name,last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi','hendrix',27)
# print(musician)

# def get_formatted_name(first_name,last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

#This is an infinite loop

# while True:
#     print("\nPlease, tell me your name")
#     print("\n(Enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f'\nHello, {formatted_name}!')

# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)

# usernames = ['hannah','ty','margot']
# greet_users(usernames)

#Start with some designs that need to be printed

# unprinted_designs = ['phone case','robot pendant', 'dodecahedron']
# completed_models = []

#Simulate printing each design until none are left
#Move each design to completed_models after printing

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing {current_design} ...")
#     print(f"{current_design} printed!")
#     completed_models.append(current_design)

#Display all completed models
# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)



# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pepper', 'extra cheese')

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMake a pizza with the following toppings:")
#     for topping in toppings:
#         print(f" - {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms','green pepper', 'extra cheese')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12,'mushrooms','green pepper', 'extra cheese')

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert','einstein',location='princeton',field='physics')
# print(user_profile)