#Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_height = 0
totaln = 0
for heights in student_heights:
    sum_height += heights
    totaln += 1
    
average = sum_height/totaln
new_average = round(average)

print (new_average)
