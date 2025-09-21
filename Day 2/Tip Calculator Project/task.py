print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip * 0.01
bill_plus_tip = bill + (bill * tip_percentage)
bill_per_person = bill_plus_tip / people
final_amount = round(bill_per_person, 2)

print((f"Each person should pay :$ {final_amount}"))

