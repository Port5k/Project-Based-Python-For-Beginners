people = [
    {
    "first_name" :"Olasubomi",
    "last_name": "Kazeem",
    "age": 18,
    "city": "Ibadan"
    },
    {
        "first_name" :"Oluwatomisin",
        "last_name": "Olatunde",
        "age": 18,
        "city": "Abuja"
    },
    {
        "first_name" :"Adenike",
        "last_name": "Abdulsalam",
        "age": 19,
        "city": "Ogun"
    }
]

for person in people: {
    print(f"{person['first_name']} {person['last_name']} is {person['age']} and lives in {person['city']}")
}