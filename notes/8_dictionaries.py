# Objects are called dictionaries in Python!
# Dictionary keys need to have "" around them (unlike js)
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"]) #green
print(alien_0["points"]) #5

#you can add key value pairs to a dictionary by declaring them explicitly
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# You can modify values similarly
alien_0["color"] = "yellow"

#empty dictionaries also evaluate to false (like empty lists)
alien_1 = {}

if alien_1:
    print("test passed")
else:
    print("test failed")

# Use the del statement to delete a key-value pair
alien_0["temporary_key"] = "going soon!"

print(alien_0) # {'color': 'yellow', 'points': 5, 'x_position': 0, 'y_position': 25, 'temporary_key': 'going soon!'}
del alien_0["temporary_key"]
print(alien_0) # {'color': 'yellow', 'points': 5, 'x_position': 0, 'y_position': 25}


# .get() is a useful tool when you are unsure if the key you are searching for will actually exist
# syntax: some_variable = some_object.get("key_you_are_unsure_of", "string to return if it doesn't exist")
# the second argument is optional, if you omit it and the key does not exist, python will return "None"
# If the key does exist it will return the key as normal. If you don't use .get() and try and access
# a key which doesn't exist, python will throw a KeyError. 

alien_speed = alien_0.get("speed", "No speed value assigned")
print(alien_speed) # No speed value assigned

alien_hp = alien_0.get("hp")
print(alien_hp) # None

# Above is an example of storing one distinct object with different properties, you can also use a dictionary
# to store information about related simple objects
favourite_languages = {
    "joe c": "python",
    "joe g": "C#",
    "damien": "java",
    "emma": "python"
}

# Looping through dictionaries (### Page 99 Python Crash Course):
# This works because the items() method loops through the object and returns an array
# of tuples consisting of the key-value pairs
print(favourite_languages.items()) #dict_items([('joe c', 'python'), ('joe g', 'C#'), ('damien', 'java'), ('maki', 'python')])

for key, value in favourite_languages.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.title()}")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

# You can use .keys() to loop through just the keys of an object if you don't care so much about the values
for name in favourite_languages.keys():
    print(name.title())

#This is also the default behaviour when looping through a dictionary, so line 63 could be written as:
for person in favourite_languages:
    print(f"{person.title()}'s favourite language is {favourite_languages[person].title()}") #but this is less readable

friends = ["joe g", "damien"]

for name in favourite_languages.keys():
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favourite_languages[name]
        print (f"\t{name.title()}, I see you love {language.title()}!")

# Looping through values:
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# This is okay for a small data set but since it does not take into account any repetitions it can get cumbersome
# set is a good way around this!

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

# You can build your own set as so:
language_set = {"python", "rust", "c#"}

### Page 105 Python Crash Course

people = ["joe c", "joe g", "erin", "aaron", "conor", "emma"]

for person in people:
    if person in favourite_languages.keys():
        print(f"Thanks for taking the poll, {person.title()}!")
    else:
        print(f"You should take our poll, {person.title()}!")
