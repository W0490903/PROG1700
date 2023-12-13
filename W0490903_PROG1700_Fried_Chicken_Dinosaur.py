"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1700
Date: 2023-11-08
Project: Fried Chicken Dinosaur
Repository: https://github.com/W0490903/PROG1700/
Programming Language: Python 3
License: Creative Commons
Version: 3.0
"""

# Assign global variables.
friedchicken_remaining = 20
friedchicken_eaten = 1
days = 1

print(r""" 
 _____                                                 _____ 
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
    
    # On all other days except the seventh, the dinosaur eats 5% more than the previous amount.
    if days != 7:
        friedchicken_remaining = friedchicken_remaining - friedchicken_eaten
        print(f"It is day {days} and I'm Hungry. Let's Eat!\nChicken eaten today: {friedchicken_eaten:.2f}\nChicken remaining: {friedchicken_remaining:.2f}\n")
        friedchicken_eaten *= 1.05
        days += 1
        if friedchicken_eaten > friedchicken_remaining:
            friedchicken_eaten = friedchicken_remaining

    # On the seventh day, the dinosaur does not eat any chicken.
    else:
        days += 1
        print("It is day 7 and I have a tummy ache. I can't eat anything today.\n")
        
# If the dinosaur runs out of chicken, prints the current day, and tells user that he has run out.
if friedchicken_remaining <= 0:
    days = days - 1
    print(f"It is day {days}. and I have run out of fried chicken! Time to make some more!")
    print(r"""
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