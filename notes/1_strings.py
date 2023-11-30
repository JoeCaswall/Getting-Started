greeting = "hello python world"

print(greeting) #hello python world

print(greeting.title()) #Hello Python World

print(greeting.upper()) #HELLO PYTHON WORLD (.lower() also works as you'd expect)

#String interpolation can be done using f strings. F stands for format.

first_name = "ada"

last_name = "lovelace"

full_name = f"{first_name} {last_name}"

print(full_name.title()) #Ada Lovelace

ada_greeting = f"Hello, my name is {full_name.title()}"

print(ada_greeting) #Hello, my name is Ada Lovelace

# \n adds a new line when printing strings, \t adds a tab

print("Languages:\nPython\nJavaScript\tC++")
#Languages:
#Python
#JavaScript     C++

#use .strip() to remove whitespace from both ends of a string

whitespace = "      I hate whitespace      "
print(whitespace)

no_whitespace = whitespace.strip()
print(no_whitespace)

#len(variable) works as variable.length does in js

print(len(whitespace))
print(len(no_whitespace))

