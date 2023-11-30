### Here we make a list of 30 aliens:
aliens = []

for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

#we can loop through a slice to upgrade only the first three aliens
for alien in aliens[:3]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
#this would obviously be better written as a function, will learn about function syntax shortly
for alien in aliens[:5]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"
print("\n")
for alien in aliens[:5]:
    print(alien)

#display total number of aliens
print(f"Total number of aliens: {len(aliens)}")

### It can also be useful to use a list within a dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

print(f"You ordered a {pizza["crust"]}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

### You can even have a dictionary of dictionaries:

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton" 
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris" 
    },
    "roppenheimer": {
        "first": "robert",
        "last": "oppenheimer",
        "location": "los alamos"
    }
}

print(users.items()) #[('aeinstein', {'first': 'albert', 'last': 'einstein', 'location': 'princeton'}) ...other users]
# so when you loop through the users.items() array it assigns param1 to the username and param2 to an object containing the
#rest of the user info
for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}\n")
    
### Page 111 Python Crash Course

cities = {
    "london": {
        "country": "england",
        "population": 9_648_000,
        "river": "thames"
    },
    "glasgow": {
        "country": "scotland",
        "population": 1_698_000,
        "river": "clyde"
    },
    "bonn": {
        "country": "germany",
        "population": 327_000,
        "river": "rhine"
    }
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    print(f"\tCountry: {city_info["country"].title()}")
    print(f"\tPopulation: {city_info["population"]}")
    print(f"\tRiver: {city_info["river"].title()}")

