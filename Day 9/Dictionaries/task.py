programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#Retrieve items from a dictionary
print(programming_dictionary["Bug"])

#add data to a key
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wipe existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)

#Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])