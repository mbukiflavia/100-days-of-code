capitals = {
    "France" : "Paris",
    "Germany" : "Berlin" # Lists can only have one value
}

#Nested lists in a dictionary
travel_log = {
    "Germany" : ["Berlin", "Stuttgart"],
    "France" : ["Paris", "Lille", "Dijon"]
}
#print Lille
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log2 = {

    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Dijon"],
    },
    "Germany" : {
        "num_times_visited" : 7,
        "cities_visited" : ["Stuttgart", "Berlin", "Hamburg"],
    },
}
print(travel_log2["Germany"]["cities_visited"][0])