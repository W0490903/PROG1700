import random

replay = "y"

# [1] Create two separate lists
programming_language = ["Python", "C", "Go", "JavaScript", "Lua" ]
difficulty_level = [1,2,3,4,5]
quiz_data = list(zip(programming_language, difficulty_level))


while replay == "y":
    random.shuffle(quiz_data)
    score = 0
    for language, difficulty in quiz_data:
        guess = int(input(f"\nHow difficult is {language}? (1-5): "))
        if guess == difficulty:
            print("That's Correct!")
            score += 1
        else:
            print(f"That's Incorrect! The correct answer was {difficulty}.")
    
    print(f"\nThanks for playing! You scored {score} out of {len(quiz_data)}!\n")
    replay = input("Play Again? (y/n): ").strip().lower()