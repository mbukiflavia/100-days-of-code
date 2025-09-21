import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friends = random.choice(friends)
print(random_friends)

#option 2
random_index = random.randint(0,4)
print(friends[random_index])