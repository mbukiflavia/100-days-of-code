import random
choices = ["rock", "paper", "scissors"]
user_choice = input("You Go first. Do you choose rock, paper or scissors?").lower()
computer_choice = random.choice(choices)
print(f"User chose: {user_choice}, Computer chose: {computer_choice}")

def rock_paper_scissors(user_choice):

    user_wins = True
    if user_choice == computer_choice:
        print("Draw")

    elif user_choice == "rock" and computer_choice == "paper":
        user_wins = False
        print("Computer Wins")

    elif user_choice == "paper" and computer_choice == "scissors":
        user_wins = False
        print("Computer Wins")

    elif user_choice == "scissors" and computer_choice == "rock":
        user_wins = False
        print("Computer Wins")

    else:
        user_wins = True
        print("User Wins")

rock_paper_scissors(user_choice)



