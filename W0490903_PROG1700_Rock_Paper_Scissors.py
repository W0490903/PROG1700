import random

def get_user_choice():
    while True: 
        user_choice = input("Rock, Paper, Scissors?: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Please choose a valid selection!")

def get_bot_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return "You Win!"
    else:
        return "Opponent Wins!"

while True:
    user_choice = get_user_choice()
    bot_choice = get_bot_choice()
    print(f"You chose {user_choice}.")
    print(f"Opponent chose {bot_choice}.")
    result = winner(user_choice, bot_choice)
    print(result)

    replay = input("Would you like to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break