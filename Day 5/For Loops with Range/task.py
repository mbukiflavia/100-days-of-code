#Range Function with For Loop

for number in range(1, 10):
    print(number) #does not print the last number in the range

#Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

sum = 0
for num in range(1, 101):
    sum = sum + num

print(sum)