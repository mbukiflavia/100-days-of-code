rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
random_number = random.randint(0,2)
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
if random_number == my_choice:
    print("Draw")
elif random_number == 0 and my_choice == 1:
    print("You Loose")
else:
    print("You win")