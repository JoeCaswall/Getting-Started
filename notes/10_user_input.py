#You can get user input from the terminal by using input(). It takes one argument - the
#message you wish to be displayed to the user. The following gives the user a greeting

name = input("Please enter your name: ")
print(f"Hello {name}!")

#Prompts can be more than one line long by assigning them to a variable first

prompt = "If you share your name, we can personalise the messages you see."
prompt += "\nWhat is your name? "

name=input(prompt)

print(f"Hello {name}!")

# When using input(), python will interpret whatever is entered as a string
# Use int() to get around this

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You can have a beer!")
else:
    print("No beer today :(")

