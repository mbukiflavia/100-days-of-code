weight = 84
height = 1.65

bmi = (weight / (height**2))
print(bmi)
print(int(bmi)) #flooring
print(round(bmi, 2)) #rounding

#Assignment Operators
score = 0
score += 1
print(score)

#f-Strings
#print("Your score is : " + str(score))
is_winning = True
#print("Your score is " + str(score) + str(is_winning)) instead, use an fstring

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")