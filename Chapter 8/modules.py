from functions import make_pizza 
from functions import build_profile
from functions import print_models
from functions import show_completed_models


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

