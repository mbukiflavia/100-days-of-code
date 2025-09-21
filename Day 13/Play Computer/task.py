try:
    year = int(input("What's your year of birth?"))
except ValueError:
    print("You have entered an invalid number. Please try again with a numerical value such as 18")
    year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
