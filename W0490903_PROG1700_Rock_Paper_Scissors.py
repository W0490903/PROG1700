"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-10-05
Project: Rock, Paper, Scissors 
Repository: https://github.com/W0490903/PROG1700/blob/main/W0490903_PROG1700_Rock_Paper_Scissors.py
Programming Language: Python 3
License: Creative Commons
Version: 2.1
"""

# Import the "random" module.
import random

# Define a global variable that limits the maximum number of invalid attempts.
max_invalid_attempts = 3

# Define a function that validates the user's input.
def get_user_choice():
    # Indicates the intial amount of invalid inputs.
    invalid_attempts = 0
    while True:
        user_choice = input("Rock, Paper, Scissors?: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            # Add one to the number of invalid attempts.
            invalid_attempts += 1
            print(f"Please choose a valid selection! Attempts Left: {max_invalid_attempts - invalid_attempts}")
            # If the invalid inputs equals 3, the program exits.
            if invalid_attempts == max_invalid_attempts:
                exit()

# Define a function that validates the bot's input.
def get_bot_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(user_choice, bot_choice):
    # If the user's choice is the same as the bot, the value returned is a tie.
    if user_choice == bot_choice:
        return "It's a tie!"
    # If not, the code uses an else/if statement to determine the outcome.
    elif (
        (user_choice == "rock" and bot_choice == "scissors")
        or (user_choice == "paper" and bot_choice == "rock")
        or (user_choice == "scissors" and bot_choice == "paper")
    ):
        return "You Win!"
    else:
        return "Opponent Wins!"

# Wraps the code in a while loop.
while True:
    # Calls the corresponding function to determine the user's input and the bot's random input.
    user_choice = get_user_choice()
    bot_choice = get_bot_choice()
    print(f"You chose {user_choice}.")
    print(f"Opponent chose {bot_choice}.")
    # The result is calculated by the "winner" function.
    result = winner(user_choice, bot_choice)
    print(result)

    # Asks the user if they would like to replay. If "yes" or "Yes", the loop replays.
    # If they respond with anything other than "yes" or "Yes", the program breaks.
    replay = input("Would you like to play again? (yes/no): ").lower().strip()
    if replay != "yes":
        print("Thanks for playing!")
        exit()