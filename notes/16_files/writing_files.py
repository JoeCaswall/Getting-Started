from pathlib import Path

path = Path("programming.txt")
# Python can only write strings to a text file, if you need to write numbers convert
# them first using str()
# If the file already exists then it will overwrrite it!!
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I dont love working with data.\n"

path.write_text(contents) 

### Page 192 Python Crash Course
#Q1
name = input("What is your name? ")

user_path = Path("guest.txt")
user_path.write_text(name)

#Q2
names = ""
asking = True

while asking:
    guest = input("What are your names? To finish, enter done ")
    if guest == "done":
        asking = False
    else:
        names += f"{guest}\n"

guest_book_path = Path("guest_book.txt")

guest_book_path.write_text(names)

