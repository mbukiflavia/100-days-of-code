import random

from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_card_1= random.choice(cards)
    return random_card_1

def add_scores(cards):
    sum_random_card_1 = 0
    for card in cards:
        sum_random_card_1 += card
    return sum_random_card_1


def play_round():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    print(user_cards)
    print(computer_cards)

    sum_user = add_scores(user_cards)
    sum_computer = add_scores(computer_cards)
    winner = ""
    if sum_user == 21:
        winner = "User"
    elif sum_computer == 21:
        winner = "Computer"
    else:
        if sum_user > 21:
            temp_list = []
            for card in user_cards:
                if card == 11:
                    temp_list.append(1)
                else:
                    temp_list.append(card)
            sum_user = add_scores(temp_list)
            if sum_user > 21:
                winner = "Computer"
        else:
            another_card = input("Do you want to get another card? (y/n)\n").lower()
            if another_card == "y":
                user_cards.append(deal_card())
                return play_round()
            else:
                sum_comp = 0
                while sum_comp < 17:
                    computer_cards.append(deal_card())
                    sum_comp = add_scores(computer_cards)
                    if sum_comp > 21:
                        winner = "Computer"
                    else:
                        if add_scores(computer_cards) > add_scores(user_cards):
                            winner = "Computer"
                        else:
                            winner = "User"


    print(f"{winner} Wins!")


play_round()


