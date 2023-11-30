from pathlib import Path

path = Path("pi_million_digits.txt")
# rstrip is used because read_text() adds an empty string at the bottom of what it reads which shows up as a blank line
contents = path.read_text().rstrip() 

pi_string = ""


for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Input your birthday in the format ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")






# Since the classes_styling.txt file is in a different directory, the absolute path is needed. If it were in a
# different directory within the 16_files directory, it would be okay to use a relative path which continues
# from/extends on the working directory path
path2 = Path("/Users/joe.caswall/Documents/bootcamp/Python/Getting-Started/notes/classes_styling.txt")

contents2 = path2.read_text().rstrip()
# print(contents2)

