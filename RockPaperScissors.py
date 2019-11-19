# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
print(user_choice)

if user_choice == "r":
    if computer_choice == "p":
        print("computer wins")
    else:
        print("player wins")
elif user_choice == "p":
    if computer_choice == "s":
        print("computer wins")
    else:
        print("player wins")
elif user_choice == "s":
    if computer_choice == "r":
        print("computer wins")
    else:
        print("player wins")
