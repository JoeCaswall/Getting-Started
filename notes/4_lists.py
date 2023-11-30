#lists are just js arrays
#accessed in the same way!
#and are 0 indexed

games = ["cluedo", "runescape", "monopoly", "7-1-7"]

print(games[0]) #cluedo

#index -1 accesses the last item in a list!
print(games[-1]) #7-1-7

#change items in the list using the index:
games[0] = "scrabble"

print(games) #["scrabble", "runescape", "monopoly", "7-1-7"]


#some_list.append("new_item") works like someList.push("newItem") in js:

games.append("cluedo")

print(games) #['scrabble', 'runescape', 'monopoly', '7-1-7', 'cluedo']


#some_list.insert(index, "new_item") adds a new item to the list at the selected index:

games.insert(1, "chess") 
print(games) #['scrabble', 'chess', 'runescape', 'monopoly', '7-1-7', 'cluedo']


#Removing items from a list: 
#If you know the position of the item you want to remove:

del games[0]
print(games) #['chess', 'runescape', 'monopoly', '7-1-7', 'cluedo']

#removing the last item is the same as in js (mutates the original array):
last_game = games.pop()
print(games) #['chess', 'runescape', 'monopoly', '7-1-7']
print(last_game) #cluedo

#unlike js, you can include an index as the parameter for .pop() to choose another item to remove from the list:
second_game = games.pop(1)
print(games) #['chess', 'monopoly', '7-1-7']
print(second_game) #runescape

#you can also remove an item by its value (this only removes the first instance of it in the list, if it
#might occur more than once you will need to use a loop)
games.remove("chess")
print(games)  #['monopoly', '7-1-7']

games.append("scrabble")
games.append("chess")
games.append("cluedo")

# some_list.sort() organises list items alphabetically (numbers go first) and mutates the list
# some_list.reverse() does the opposite

games.sort()
print(games)
games.reverse()
print(games)

# sorted(some_list) does the same but does not mutate the original list!

# len(some_list) gives you the length of a list, just as it does with strings

print(len(games)) # 5

## Start page 61 in Python Crash Course ##

# slicing a list uses the syntax some_slice = some_list[start_index:end_index] and is not inclusive of the end index
# it DOES NOT mutate the original list

games_slice = games[0:3]
print(games_slice) #['scrabble', 'monopoly', 'cluedo']

# you can omit the start index or end index to automatically begin the slice at the start  or end of the list:

print(games[:3]) #['scrabble', 'monopoly', 'cluedo']
print(games[2:]) #['cluedo', 'chess', '7-1-7']

# you can also use the negative index syntax to start the slice from any distance from the end of the list
# eg if you only want the last three items in a list, you could use:

print(games[-3:]) #['cluedo', 'chess', '7-1-7']

# if you omit both the start and end index, you can make a copy of the whole array:

same_games = games[:] #if you miss the [:] then python points both variables to the same list, so if you change on the other will change as well
print(games)
print(same_games)

# much like the range() function, you can also include a third parameter in the slice to tell python how many items to skip
# between each item in the slice:

print(games[0:4:2]) #['scrabble', 'cluedo']


