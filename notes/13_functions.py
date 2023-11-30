#If the file is in the same directory as the working file you can simplify this to simply import test_module

#Imports whole file, need to specify tm.some_function when calling the funciton
import test_module as tm 

#Imports specific functions, can use them without specifying source location
from test_module_2 import quick_function_one, quick_function_two

#Imports specific function and gives it an alias (use if your program already has a function with the same name as the one being imported)
from test_module_2 import quick_function_three as qft

#Import all functions from a module using *
from test_module_3 import *

# The keyword for a function declaration in python is 'def' 
def count_to_x(x):
    count = 1
    while count <= x:
        print(count)
        count += 1

count_to_x(15)

#You can use keyword arguments when calling a function to ensure they don't get passed in the wrong order:
def describe_pet(species, name):
    return f"I have a {species} named {name}"

print(describe_pet("Harry", "Lizard")) #This returns a string saying I have a Harry named Lizard
print(describe_pet(name="Harry", species="Lizard")) #This ignores the input order and returns the correct string

#You can also use default values in the same way as JS:

def pet_dog(name, species="dog"):
    return f"I have a {species} named {name}"

print(pet_dog("Harry")) #I have a dog named Harry

# If you don't know how many parameters are going to be passed to a function, you can use an * to
# place a placeholder argument in the function. This is called an arbitrary argument and can be used
# with positional ones, but must go LAST in the list of arguments.

def top_pizza(size, *toppings):
    print(f"Making a {size} inch pizza topped with:")
    for topping in toppings:
        print(f"\t- {topping}")

top_pizza("pep", "mozz", "rocket")

# You can also force an arbitrary argument to produce a dictionary using ** !
# Python will build a dictionary with the variable name passed as an argument after the **

def build_profile(first, last, **user_info):
    #Builds a dictionary containing all info about the user:
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")

print(user_profile)

### Page 149 Python Crash Course
#Q1
def sandwich_items(*fillings):
    print("You sandwich is filled with:")
    for filling in fillings:
        print(f"\t-{filling}")

sandwich_items("tuna", "mayo")
sandwich_items("meatballs", "marinara", "cheese")
sandwich_items("chicken", "hot sauce", "lettuce", "tomato")

#Q2
my_profile = build_profile("joe", "caswall", age=26, job="software engineering apprentice", location="london")
print(my_profile)

#Q3
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# Import modules as shown at the top of the file 
number = tm.multiply(2, 4)

print(number)

quick_function_one()
quick_function_two("Joe")
qft("London")

func()
func2()
func3()

