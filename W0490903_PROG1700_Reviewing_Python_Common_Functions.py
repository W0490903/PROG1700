"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-11-29
Project: Reviewing Python Common Functions
Repository: https://github.com/W0490903/PROG1700/
Programming Language: Python 3
"""

### Strings:

# Concatenation
def Concatenation():
    str1 = 'Apple'
    str2 = 'Pie'
    result_str = str1 + ' ' + str2
    print(result_str)

# Substrings
def Substring():
    string = 'Extravagant'
    print(string[0:5])

# Formatting
def Formatting():
    year = 20
    print(f'You are {year} years old!')

### Loops:

# Print Numbers
def Print_Numbers():
    result_str = ''  
    for x in range(1,11):
        result_str += str(x) + ' '
    print(result_str)
    

# Factorial
def Factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result
# print(Factorial(5))

### Sets:

# Intersection
def Intersection():
    set1 = {1,2,3,4,5}
    set2 = {3,8,5,10,1}
    intersect = set1.intersection(set2)
    print(intersect)

### Lists:

# List Operations
def List_Operations():
    list1 = [1,2,3,4,5]
    # Sum of all elements.
    print(f"The sum of the list is: {sum(list1)}")
    # Average of all elements.
    print(f"The average of the list is: {sum(list1)/len(list1)}")
    # Maximum of all elements.
    print(f"The maximum of the list is: {max(list1)}")
    # Minimum of all elements.
    print(f"The minimum of the list is: {min(list1)}")

# List Comprehension
def List_Comprehension():    
    list1 = [1,2,3,4,5,6,7,8,9,10]
    for n in list1:
        n *= n
        print(n)

### Tuples:

# Tuple Unpacking
def Tuple_Unpacking():
    tuple = (1,2,3)
    (a,b,c) = tuple
    print(a,b,c)

### Dictionaries:

# Dictionary Operations
def Dictionary_Operations():
    dict1 = {'Name:':'Alice', 'Age:':'20', 'City:':'Halifax'}
    for key,value in dict1.items():
        print(key,value)

# Nested Dictionary
def Nested_Dictionary():
    dict1 = {
        1:{'name':'Alice','grades':{'History':85, 'Math':91, 'English':79, 'Science':82}},
        2:{'name':'Bob','grades':{'History':77, 'Math':81, 'English':68, 'Science':92}}
    }

    for student_info in dict1.values():
        grades = student_info['grades']
        average_grade = sum(grades.values()) / len(grades)
        print(f"{student_info['name']}'s average grade is: {round(average_grade)}")

### Functions:

# Function Basics
def Function_Basics(a,b):
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")

# Default Values
def Default_Values(a=1,b=1):
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")

### Reading/Writing External Files:

# File Reading
def File_Reading():
    file = open("File_Writing_and_Reading.txt")
    print(file.read())
    file.close()

# File Writing
def File_Writing():
    file = open("File_Writing_and_Reading.txt", "a")
    file.write("\nI have added this extra line!")
    file.close()
    file = open("File_Writing_and_Reading.txt", "r")
    print(file.read())