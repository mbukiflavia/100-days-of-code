# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_highest_bidder(name_dictionary):
   highest_bid = 0
   winner = ""
   for bidder in name_dictionary:
        bid_amount = name_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")

from art import logo
print(logo)
print("Welcome to the secret auction program")
name_dictionary = {}
other_bidders = True
while other_bidders:

    name = input("What is your name? : \n")
    bid = int(input("What is your bid? :$ \n"))
    name_dictionary[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if cont == "no":
        other_bidders = False
        find_highest_bidder(bid)
    print("\n" * 20)
print(name_dictionary)

print("The winner is {..}")

