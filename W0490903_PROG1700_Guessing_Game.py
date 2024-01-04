"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-10-17
Project: Guessing Game
Repository: https://github.com/W0490903/PROG1700/
Programming Language: Python 3
License: Creative Commons
Version: 2.0
"""

# Import the "random" module.
import random

# Define a global variable that limits the maximum number of invalid attempts.
max_invalid_attempts = 3
invalid_attempts = 0

# Define a function that determines the bot's choice via random range.
def get_bot_choice():
    return random.randrange(1, 11)


# Define a function to determine the user's choice.
def get_user_choice():
    
    global invalid_attempts
    
    while invalid_attempts < max_invalid_attempts:
        user_choice = input("Select a number between 1 and 10: ")
        
        # Validate the user is inputting only the data type we desire.
        try:
            user_choice = int(user_choice)
            if user_choice in range(1, 11):
                return user_choice
            else:
                invalid_attempts += 1
                print(f"Please choose a valid selection! Attempts left: {max_invalid_attempts - invalid_attempts}")
        
        # Return an error if the data is incorrect.
        except ValueError:
            invalid_attempts += 1
            print(f"Please choose a valid selection! Attempts left: {max_invalid_attempts - invalid_attempts}")
            
    if invalid_attempts == max_invalid_attempts:
        print("You have no attempts left. Thanks for Playing!")
        exit()

# Define a function to determine the user's name.
def get_user_name():
    
    global invalid_attempts
    
    while invalid_attempts < max_invalid_attempts:
        
        user_name = input("What is your name?: ")
        
        # Validate the user is inputting only the data type we desire.
        if user_name.isalpha():
            invalid_attempts = 0
            return user_name
        else:
            invalid_attempts += 1
            print(f"Please choose a valid selection! Attempts left: {max_invalid_attempts - invalid_attempts}")
            if invalid_attempts == max_invalid_attempts:
                print("You have no attempts left. Thanks for Playing!")
                exit()

# Define a function to determine the outcome.
def winner(user_choice, bot_choice):
    
    global invalid_attempts
    
    if user_choice is None:
        return "You have no attempts left."
    if user_choice == bot_choice:
        return f"That's correct! You guessed the answer in {max_invalid_attempts - invalid_attempts} attempt(s)!"
    elif user_choice > bot_choice:
            invalid_attempts += 1
            return f"Nope, try lower. You have {max_invalid_attempts - invalid_attempts} attempts remaining."
    elif user_choice < bot_choice:
            invalid_attempts += 1
            return f"Nope, try higher. You have {max_invalid_attempts - invalid_attempts} attempts remaining."
    if invalid_attempts == max_invalid_attempts:
        return "You have no more attempts!"

# Declare a replay variable as "Yes".
replay = "yes"

# Main Game Loop, runs as long as 'replay' is set to "yes".
while replay == "yes":
    
    guesses = max_invalid_attempts
    invalid_attempts = 0
    user_name = get_user_name()
    bot_choice = get_bot_choice()
    
    print(f"Hello, {user_name}!")
    
    while True:
        
        user_choice = get_user_choice()
        
        if user_choice is not None:
            result = winner(user_choice, bot_choice)
            print(result)
            if result == f"That's correct! You guessed the answer in {max_invalid_attempts - invalid_attempts} attempt(s)!":
                break
            else:
                guesses -= 1
            
        if guesses <= 0:
            print(f"You have no guesses left. The correct number was {bot_choice}.")
            break

    replay = input("Play Again? (yes/no): ").lower().strip()