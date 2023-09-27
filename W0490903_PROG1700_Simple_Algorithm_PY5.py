"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-09-25
Project: Create a simple Algorithm using the program Flowchart and pseudocode
Repository: https://github.com/W0490903/Coding/blob/main/W0490903_PROG1700_Simple_Algorithm_PY5.py
Programming Language: Python 3
License: Creative Commons
Version: 1.0
"""

# Import the current date using the datetime module.
import datetime

# Defines current year and month variables.
# The datetime module is used to import the current year and month.
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

# Validate user input. This function will check an input to ascertain if the input is an integer.
# If the input is not an integer, it will return an error and reprompt the user for an input again.
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number!")

#Loops this snippet of code.
while True:
    # Ask user to input current age.
    age_input = get_integer_input("Enter your age as a number: ")
    # Ask user to input their birth month.
    month_input = get_integer_input("Enter the month you were born (1-12): ")

    # If the user's inputted month is not equal to 
    if month_input <= current_month:
        yob = current_year - age_input
    else:
        yob = current_year - age_input - 1

    # Calculate and display user's year of birth.
    print(f"Your year of birth is {yob}")

    # Ask user if they would like to reset.
    reset = input("Reset? (y/n)")
    if reset != "y":
        break