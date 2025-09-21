from art import logo
print(logo)
import random

print("Welcome to the number guessing game \nI'm thinking of a number between 1 and 100.")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

NUM_TO_GUESS = random.randint(1, 100)

def lives():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play():
    lives()
    lives_remaing(lives)

    play()

def lives_remaing(lives):
    print(f"You have {lives} attempts remaining to guess the number")
    loose = True
    while loose:
        user_guess = int(input("Make a guess: "))
        if user_guess == NUM_TO_GUESS:
            loose = False
            print("Correct guess. You Win")
        else:
            if user_guess > NUM_TO_GUESS:
                print("Too high")

            else:
                print("Too low")
    lives_bal = lives - 1
    print(f"You have {lives_bal} attempts remaining to guess the number")
    print("Guess again")





play()