# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    "helsinki": {
        'country': 'finland',
        'population': 300000,
        'fun fact': 'Very Cold'
    },
    "tokyo": {
        'country': 'japan',
        'population': 14500000,
        'fun fact': 'Very hot in summer'
    },
    "Ibadan": {
        'country': 'nigeria',
        'population': 7660000,
        'fun fact': 'No light'
    }
}

for city, city_info in cities.items():
    print(f"{city} is a city in {city_info['country'].title()} with a population of about {city_info['population']}\n A fun fact about {city_info['country'].title()} is that {city_info['fun fact']}")
