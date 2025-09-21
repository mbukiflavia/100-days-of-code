# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")

#Functions with more than one input and Positional argument
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"How is it like in {location}")

greet_with("Flavia", "Italy") #positional arguments
greet_with(name="Groot", location = "France")