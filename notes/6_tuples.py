# A tuple is a list that cannot be modified. They look the same as lists but use () instead of []
# Say we had a rectangle that was always one size, we could use a tuple to define it, then access them in the same
#way as we access list indexes:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# if you try to change one of the items in the dimensions tuple, it will return a TypeError

# dimensions[0] = 250 #commented out as will throw an error

# tuples can have one element, it's uncommon but if needed you can make one by using a trailing comma
my_t = (1,)

#looping through a tuple is the same as looping through a list

for dimension in dimensions:
    print(dimension) #200, 50

# while you can't change individual items in a tuple, you can still reassign the whole variable

dimensions = (400, 100)

for dimension in dimensions:
    print(dimension) #400, 100

    