#countries_in_africa = ["Kenya", "South Africa"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])
print(states_of_america[-1]) #first one from the end

#updating lists
states_of_america[0] = "Delawares"
print(states_of_america[0])

#add item to the end of a list
states_of_america.append("aAngelaland")
print(states_of_america[-1])

#add multiple items to the end of a list
states_of_america.extend(["Nigeria", "Ghana"])
print(states_of_america[-1])