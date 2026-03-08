import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

if user not in choices:
    print("Your input is incorrect")

else:
    computer = random.choice(choices)

    print(f"Your choice: {user}")
    print(f"Computer's choice: {computer}")

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You won!")

    elif user == "paper" and computer == "rock":
        print("You won!")

    elif user == "scissors" and computer == "paper":
        print("You won!")

    else:
        print("Computer won!")

'''
Here is my first basic level of pythin Project which is rock, paper, scissors game in python with a very basic
understanging of logic on how this program works.
'''