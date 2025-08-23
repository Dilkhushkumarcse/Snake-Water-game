'''write a python program capable of playing this game with the
user.'''

import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1]) #The random.choice() function selects one value randomly from the list.
youstr = input("Enter your choice g for gun, w for water s for snake: ")#The result is stored as a string in youstr.
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}#Does the reverse — converts the number back to a readable name for printing.

you = youDict[youstr]#Converts the user’s input (s, w, or g) to its numeric value using youDict.

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")#This line prints what the user and the computer chose, by converting their numeric values back into words using reverseDict.

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")