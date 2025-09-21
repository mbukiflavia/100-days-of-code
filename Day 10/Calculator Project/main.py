from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#2 Add the functions to a dictionary as the values. Keys = "+", "-", "*", "/"
operations_dictionary = {
   "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

#result = operations_dictionary["*"](4,8)
#print(result)

#3 Use the dictionary operations to poerfom the calculation - 4*8
def calculator():
    print(logo)
    should_accumulate = True
    n1 = float(input("Type the first number"))
    while should_accumulate:

        for symbol in operations_dictionary:
            print(symbol)
        operator = input("Type a mathematical operator")
        n2 = float(input("Type the second number"))

        result = operations_dictionary[operator](n1, n2)
        print(result)

        cont = input(f"Would you like to continue working with {result} ? type 'y' or 'n' \n").lower()
        if cont == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() #recurssion

calculator()

