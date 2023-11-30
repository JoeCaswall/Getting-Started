from pathlib import Path

# Exceptions are written in try-except blocks (like try-catch blocks in JS)
# They work in the same way, to help with error handling and allow a program
# to continue running even if something doesb't work in it. 

# eg: python can't divide by 0 so it throws a traceback with a ZeroDivisionError

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#This can be used to prevent crashes

print("\nGive me two numbers and I'll divide them.")
print("Enter q to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("Please only enter numbers!")
    else:
        print(answer)
    
## handling FileNotFound errors

example_path = Path("pi_digits.txt") #This will throw an error as the path is wrong
# The encoding argument is needed when your system’s
# default encoding doesn’t match the encoding of the file that’s being read.
# This is most likely to happen when reading from a file that wasn’t created
# on your system.
try:
    example_contents = example_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {example_path} does not exist.")

# Here we will be working with the book copies stored as .txt files

def count_words(path):
    """Count the number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # if you want the error to fail silently (ie without letting the user know)
        # use pass to not throw anything in the case of an error
        #pass 
        print(f"Sorry, the file {path} does not exist.")
    else:
        #Count the number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path("alice.txt")
count_words(path)

# mockingbird doesn't exist in a file, so the exception is thrown
books = ["alice.txt", "moby_dick.txt", "to_kill_a_mockingbird.txt", "little_women.txt"] 

for book in books:
    count_words(Path(book))

def num_of_the(path):
    """Counts how many times a file uses the word 'the' """
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.lower().split()
        count = words.count("the")
        print(f"The word the appears {count} times in {path}")

spanish = Path("the_spanish_farm.txt")

num_of_the(spanish)