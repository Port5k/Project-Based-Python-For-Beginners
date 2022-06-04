# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def build_profile(first, last, **user_profile):
    user_profile['first_name'] = first
    user_profile['last_name'] = last

    return user_profile

my_profile = build_profile('adekunle','adedokun',pseudonym='Port5k',school='LAUTECH',department='medicine and surgery')
print(my_profile)