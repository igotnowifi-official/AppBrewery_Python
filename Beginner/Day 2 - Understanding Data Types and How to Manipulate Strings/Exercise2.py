# BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n_weight=str(float(weight))
n_height=str(float(height))
bmi=float(weight) /(float(height) * float(height))
new_bmi=str(int(bmi))
print(new_bmi)