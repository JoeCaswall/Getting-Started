# To make a class, start by declaring 'class' followed by the name of the class.

class Dog:
    # __init__() is a built in python method which initialises classes. self must be the first argument. 
    def __init__(self, name, age):
        #Initialise name and age attributes (self is similar to this in JS):
        self.name = name
        self.age = age
    #Methods:
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

## Creating a specific instance of Dog:

my_dog = Dog("Opie", 8)

print(f"My dog is called {my_dog.name}.") #Note that dot notation works for attributes of an instance of a class
print(f"My dog is {my_dog.age} years old.") #While it doesn't work for object/dictionary keys

my_dog.sit()
my_dog.roll_over()

## Page 162 Python Crash Course

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"This restaurant is called {self.restaurant_name} and sells {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Les Halles", "French")

restaurant.describe_restaurant()
restaurant.open_restaurant()

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{self.username}:")
        print(f"\tFull Name: {full_name}")
        print(f"\tEmail: {self.email}")
    
    def greet_user(self):
        print(f"Hi, {self.username}!")

solarwhale = User("Joe", "Caswall", "solarwhale", "qwerty@hello.com")

solarwhale.describe_user()
solarwhale.greet_user()

