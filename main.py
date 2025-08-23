# Write a Python program capable of playing this game with the user.
import random
'''
1 for snake
-1 for water 
0 for gun
'''
# Game rules mapping
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Game loop
while True:
    print("\n Welcome to Snake-Water-Gun Game")
    print(" Enter your choice: 's' for Snake, 'w' for Water, 'g' for Gun")
    
    # Get computer's choice
    computer = random.choice([-1, 0, 1])
    
    # Get user input
    youstr = input("Your choice (s/w/g): ").lower()

    # Validate input
    if youstr not in youDict:
        print(" Invalid input! Please choose 's', 'w', or 'g'.")
        continue  # back to start of the loop

    # Map input to number
    you = youDict[youstr]

    # Display choices
    print(f"\n You chose {reverseDict[you]}")
    print(f" Computer chose {reverseDict[computer]}")

    # Determine result
    if computer == you:
        print(" It's a draw!")
    else:
        if computer == -1 and you == 1:
            print(" You win!")
        elif computer == -1 and you == 0:
            print(" You lose!")
        elif computer == 1 and you == -1:
            print(" You lose!")
        elif computer == 1 and you == 0:
            print(" You win!")
        elif computer == 0 and you == -1:
            print("You win!")
        elif computer == 0 and you == 1:
            print(" You lose!")
        else:
            print(" Something went wrong!")

    # Ask to play again
    again = input("\n🔁 Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing! Goodbye.")
        break