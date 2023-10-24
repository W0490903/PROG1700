"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-10-23
Project: Fried Chicken Dinosaur
Repository: https://github.com/W0490903/PROG1700/
Programming Language: Python 3
License: Creative Commons
"""

# Assign global variables.
friedchicken_remaining = 20
friedchicken_eaten = 1
days = 1

print(""" _____                                                 _____ 
( ___ )                                               ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  _______        __           __                 |   | 
 |   | |    ___|.----.|__|.-----.--|  |                |   | 
 |   | |    ___||   _||  ||  -__|  _  |                |   | 
 |   | |___|    |__|  |__||_____|_____|                |   | 
 |   |                                                 |   | 
 |   |  ______ __     __        __                     |   | 
 |   | |      |  |--.|__|.----.|  |--.-----.-----.     |   | 
 |   | |   ---|     ||  ||  __||    <|  -__|     |     |   | 
 |   | |______|__|__||__||____||__|__|_____|__|__|     |   | 
 |   |                                                 |   | 
 |   |  _____  __                                      |   | 
 |   | |     \|__|.-----.-----.-----.---.-.--.--.----. |   | 
 |   | |  --  |  ||     |  _  |__ --|  _  |  |  |   _| |   | 
 |   | |_____/|__||__|__|_____|_____|___._|_____|__|   |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                               (_____)
""")

# Wraps code in a while loop, repeating the code execution as long as the condition is met.
while friedchicken_remaining > 0:
    # If it is the first day, the dinosaur only eats 1 pound.
    if days == 1:
        print(f"It is day {days} and I'm Hungry. Let's Eat!")
        friedchicken_remaining = friedchicken_remaining - friedchicken_eaten
        days += 1
        print(f"Chicken eaten today: {friedchicken_eaten:.2f}")
        print(f"Chicken remaining: {friedchicken_remaining:.2f}")
        # Increment the amount the dinosaur eats after each day, except the seventh.
        friedchicken_eaten += 0.05
    # On all other days except the seventh, the dinosaur eats 0.05 more than the previous day.
    elif days > 1 and days != 7 and days != 16:
        print(f"It is day {days} and I'm Hungry. Let's Eat!")
        print(f"Chicken eaten today: {friedchicken_eaten:.2f}")
        friedchicken_remaining = friedchicken_remaining - friedchicken_eaten
        print(f"Chicken remaining: {friedchicken_remaining:.2f}")
        friedchicken_eaten += 0.05
        days += 1
    # On the seventh day, the dinosaur does not eat any chicken.
    elif days == 7:
        days += 1
        print(f"It is day 7 and I have a tummy ache. I can't eat anything today.")
    # On day sixteen, he eats the last of his chicken, so this sets the amount remaining to zero.
    elif days == 16:
        print(f"It is day {days} and I'm Hungry. Let's Eat!")
        print(f"Chicken eaten today: 1.45")
        print(f"Chicken remaining: 0")
        friedchicken_remaining = 0
        
# If the dinosaur runs out of chicken, prints the current day, and tells user that he has run out.
if friedchicken_remaining <= 0:
    print(f"It is day {days}. and I have run out of fried chicken! Time to make some more!")
    print("""\
                                                     ___._
                                                   .'  <0>'-.._
                                                  /  /.--.____")
                                                 |   \   __.-'~
                                                 |  :  -'/
                                                /:.  :.-'
__________                                     | : '. |
'--.____  '--------.______       _.----.-----./      :/
        '--.__            `'----/       '-.      __ :/
              '-.___           :           \   .'  )/
                    '---._           _.-'   ] /  _/
                         '-._      _/     _/ / _/
                             \_ .-'____.-'__< |  \___
                               <_______.\    \_\_---.7
                              |   /'=r_.-'     _\\ =/
                          .--'   /            ._/'>
                        .'   _.-'
                       / .--'
                      /,/
                      |/`)
                      'c=,
          """)