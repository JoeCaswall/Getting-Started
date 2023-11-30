# Python includes the Python Standard Library which is a set of modules included with the python installation.

from random import randint, choice

print(randint(1, 6)) #picks a random number between 1 and 6 (not including 6)

letters = ["a", "b", "c", "d", "e"]
pick = choice(letters) # Picks a random entry from a selection
print(pick)

#there are obviously too many of these to list comprehensively - checkout the library docs
# https://docs.python.org/3/library/index.html