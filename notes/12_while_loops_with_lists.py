# If modifying a list or dictionary, we should be using a while loop as python will have trouble
# keeping track of the items in the list if modifying them with a for loop

# Moving items from one list to another

# Consider a list of users who have registered but haven't verified their account yet
# How do we move them from the list of registered users to the list of verified users? 

unverified_users = ["emma", "joec", "joeg", "jamie", "nigel", "karen"]
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()

    print(f"Verifying user: {current_user}")
    verified_users.append(current_user)

print("The following users have been verified:")
for user in verified_users:
    print(user)


#To remove all instances of a specific value from a list:

pets = ["dog", "cat", "goldfish", "cat", "rock", "cat"]

while "cat" in pets:
    pets.remove("cat")

print(pets)

# Storing user responses in a dictionary:
responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you most like to climb? ")

    responses[name] = response

    repeat = input("Is anyone else taking the poll? y/n ")
    if repeat.lower() == "n":
        polling_active = False

print("----Poll Results----")

for name, response in responses.items():
    print(f"{name} would like to climb {response}")


### Page 127 Python Crash Course

#Q1 and Q2
sandwich_orders = ["meatball sub", "pastrami", "turkey and stuffing", "club", "pastrami", "blt", "salmon and cream cheese", "pastrami", "tuna"]
finished_sandwiches = []
print("Sorry guys, no more pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I've made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    if sandwich == "blt":
        print(sandwich.upper())
    else:
        print(sandwich.title())


#Q3
user_responses = {}
poll_open = True

while poll_open:
    name = input("What is your name? ")
    vacation = input("What is your dream vacation location? ")
    user_responses[name] = vacation
    stop = input("Is there another user to be polled? y/n ")
    if stop == "n":
        poll_open = False

print("---- Poll Results ----")
for name, vacation in user_responses.items():
    print(f"{name.title()} wants to visit {vacation.title()}")
