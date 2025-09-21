# TODO Import art and game data
import random
import art
import game_data
print(art.logo)
#TODO a function to choose random data points

def guesses():
    return random.choice(game_data.data)

#TODO display 2 data points and ask the user to compare and choose A or B

for i in range(1):
    a = guesses()
    name = a["name"]
    description = a["description"]
    country = a["country"]
    print(f"Compare A: {name}, a {description} from {country}")
    print(art.vs)
for i in range(1):
    b = guesses()
    name = b["name"]
    description = b["description"]
    country = b["country"]
    print(f"Against B: {name}, a {description} from {country}")
user_answer = input("Who has more followers? Type 'A' or 'B':").upper()
print(user_answer)


# TODO a function to Compare user choice vs data point answer
def compare(user_answer, answer):

# TODO Calculate score and repeat
#TODO end game when answer is wrong