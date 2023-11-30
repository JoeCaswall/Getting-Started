# For loops repeat code for a set number of iterations. While loops repeat code until
# a set condition no longer holds true. Use while loops if you are unsure how long the loop needs to run for.

# To count to 5:
num = 1
while num <= 5:
    print(num)
    num += 1


#You can use a while loop to allow a user to quit input whenever they like

# prompt = "Tell me something and I can say it back to you:"
# prompt += "\nEnter quit at any time to exit the program. "

# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

#A better way is to use a flag to set some variable 'active' to False 
#this way multiple actions can cause the program to end

# prompt2 = "Tell me something and I can say it back to you:"
# prompt2 += "\nEnter quit at any time to exit the program. "

# active = True
# while active:
#     message2 = input(prompt)

#     if message2 == "quit":
#         active = False
#     else:
#         print(message)


# Another way to end a while loop is to use a 'break'.
# In this case, instead of continuing all the way to 0, the loop stops at 5.
x = 10

while x > 0:
    if x == 5:
        break
    print(x)
    x -= 1

# To only miss out 5, we would use a 'continue' statement:

y = 11

while y > 0:
    y -= 1
    if y == 5:
        continue
    print(y)
    

