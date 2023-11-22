"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-11-15
Project: Exploring Dictionaries
Repository: https://github.com/W0490903/PROG1700/
Programming Language: Python 3
License: Creative Commons
Version: 2.0
"""

import statistics

# Create dictionary with names and scores.
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 78, "David": 92, "Eve": 88}

# Print the dictionary. [1]
def printdict():
    print(student_scores)

# Print average scores. [2]
def average_score():
    print("The average score is: ", statistics.mean(list(student_scores.values())))

# Prompt user for student name, and check if student exists. [3]
def user_search():
    while True:
        student = input("Please enter student name: ").strip().title()
        if student in student_scores.keys():
            print(f"Name: {student}\nScore: {student_scores.get(student)}")
            break
        else:
            print("No record exists. Please select a valid student!")

# Prompt user for student name, check if it exists, then prompt user to input a new score. [4]
def change_student_grade():
    user_search()
    while True:
        lowest_possible_score = 0
        highest_possible_score = 100

        new_score = input("Please enter a new score: ").strip()
        if new_score.isdigit() and int(new_score) >= lowest_possible_score and int(new_score) <= highest_possible_score:
            print("Score successfully changed.")
            break
        else:
            print("Please enter a valid score (0-100)!")

# Displays the current names in the dictionary, then prompts user to input a student name to remove. [5]
def remove_student_record():
    print("Current students:")
    for keys in student_scores.keys():
        print(keys)
    while True:
        student = (input("\nWhich student record would you like to remove?: ").strip().title())
        if student in student_scores.keys():
            del student_scores[student]
            print("Record successfully removed.\n")
            print("Current students:")
            for keys in student_scores.keys():
                print(keys)
            break
        else:
            print("Record not found!")

# Displays the student with the highest score. [6]
def print_highest_score():
    highest_name = max(student_scores, key=student_scores.get)
    highest_score = student_scores[highest_name]
    print(f"The student with the highest score is {highest_name} with a score of {highest_score}.")

# Main
while True:
    selection = input(
"""\n[1] Display All Records
[2] Display Average Score
[3] Search Student Score
[4] Change Student Grade
[5] Remove Student Record
[6] Display Highest Score\n
Please make a selection (1-6): """)
    
    if not selection.isdigit():
        print("Please make a valid number! (1 - 6)")
        continue
    
    selection = int(selection)
    
    if selection < 1 or selection > 6:
        print("\nPlease make a valid selection!")
    elif selection == 1:
        printdict()
    elif selection == 2:
        average_score()
    elif selection == 3:
        user_search()
    elif selection == 4:
        change_student_grade()
    elif selection == 5:
        remove_student_record()
    elif selection == 6:
        print_highest_score()