# "for ... in ..." loops
family = ["rick", "morty", "diane", "jerry", "summer"] 

#person is dev defined, useful to be related to whats in the list for readability
#any code properly indented after for 'for ... in ...' line will be looped through, so indentation is very important!
#forgetting to indent can cause unexpected behaviour or throw an IndentationError
for person in family:
    print(f"You are a valued member of the Sanchez family, {person.title()}.")
    print("I mean it!")

##range() makes working with numbers easy in python:
for x in range(0, 6): #this prints each number from 0 to 5 on a new line.
    print(x)

for x in range(6): #this works the same as above, if you are starting from 0 you can omit the first parameter
    print(x)

for x in range(2, 11, 2): #the third parameter tells python to skip every second item, so this will print even numbers
    print(x)

squares = []

for x in range(1, 11): # ** is an exponent, so x ** 2 is x squared
    square = x ** 2
    squares.append(square)

print(squares)

# some useful statistical functions built into python

print(min(squares)) # 1
print(max(squares)) # 100
print(sum(squares)) # 385 (sum of squares up to 100)

#List comprehensions allow you to generate lists in a single line using a for ... in ... loop (NB don't use a colon at the end of the loop declaration)

squares = [value ** 2 for value in range(1, 11)]

print(squares)

###Python Crash Course tasks (page 60)

one_to_twenty = [x for x in range(1, 21)] 
print(one_to_twenty) ## end q1

one_million = [x for x in range(1, 1_000_001)]
# print(one_million) ## end q2 (commented out as it fills up console)

print(min(one_million))
print(max(one_million))
print(sum(one_million)) #end q3

odd_numbers = [x for x in range(1, 21, 2)]
print(odd_numbers) #end q4

multiples_of_3 = [x for x in range (3, 31, 3)]
print(multiples_of_3) #end q5

cubes = [x ** 3 for x in range(1, 11)]
print(cubes) #end q5 and q6 

### Page 62 Python Crash Course ###

# you can loop through just a slice of a list by including the slice syntax

players = ["Joe", "Emma", "Jon", "Siobhan", "Ellie", "Luke", "Emily", "Joe"]

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)
