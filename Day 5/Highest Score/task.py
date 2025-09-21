student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range(1, 10))
total_exam_score=sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum = sum + score
    #sum+=score

print(sum)

#Max number
print(max(student_scores)) #replicate this using for loops

max_number = student_scores[0]
for num in student_scores:
    if num > max_number:
        max_number = num
print(max_number)