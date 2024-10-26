import random

# Prompt the user for a level
while True:
    level = input("Enter a level (positive integer): ")
    if level.isdigit() and int(level) > 0:
        level = int(level)
        break
    else:
        print("Invalid input, please enter a positive integer.")

# Randomly generate an integer between 1 and level
target = random.randint(1, level)

# Game loop for guessing the integer
while True:
    guess = input("Guess the integer (between 1 and {}): ".format(level))
    if guess.isdigit() and int(guess) > 0:
        guess = int(guess)
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break
    else:
        print("Invalid input, please enter a positive integer.")
