cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# == in Python is looking for strict equality, so cAsE MaTTerS !
# if you don't want case to matter, use .lower() in the condition

# != works the same but the inverse:
for car in cars:
    if car != "bmw":
        print(car.title())
    else:
        print(car.upper())

# you can check multiple conditions by using and/or/not
age_1 = 17
age_2 = 25

if age_1 < 18 and age_2 < 18:
    print("Neither of you are old enough to enter.")
elif age_1 >= 18 and age_2 >= 18: #elif syntax
    print("You can both enter.")
else: #You do not need an else block at the end, it can be clearer to write another elif instead
    print("One of you can enter.")

# you can check if a value is in a list using 'in'
requested_toppings = ["mushrooms", "onions", "pineapple"]

print("mushrooms" in requested_toppings) #true
print("pepperoni" in requested_toppings) #false

# not works like ! for boolean expressions

banned_users = ["charlie", "maria", "denise"]
user = "jamie"

if user not in banned_users:
    print(f"{user.title()}, you can log in.")
else:
    print("Access denied.")

### Page 64 Python Crash Course ###

alien_color = "red"

if alien_color == "green":
    print("Player earned 5 points")
elif alien_color == "yellow":
    print("Player earned 10 points")
elif alien_color == "red":
    print("Player earned 20 points")
else:
    print("Invalid alien color")

age = 300

if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
elif age < 120:
    print("You are elderly.")
else:
    print("You might be gandalf...")

# comparing lists
favourite_fruits = ["apple", "strawberry", "grape"]
lots_of_fruits = ["banana", "plum", "apple", "raspberry", "mango", "grape", "apricot", "strawberry"]

for fruit in lots_of_fruits:
    if fruit in favourite_fruits:
        print(f"You really like {fruit}s!")
    else:
        print(f"Not so fond of {fruit}s.")

# empty lists evaluate to False
some_list = []

if some_list:
    print("Yay it has items in it")
else:
    print("Oh dear, no items :(")

