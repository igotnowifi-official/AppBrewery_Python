# BMI Calculator 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi= round (weight/(height**2))
if bmi<=35:
    if bmi>=18.5:
        if bmi>=25:
            if bmi<30:
                print (f"Your BMI is {bmi}, you are slightly overweight.")
            else:
                print (f"Your BMI is {bmi}, you are obese.")
        else:
            print (f"Your BMI is {bmi}, you have a normal weight.")
    else:
           print (f"Your BMI is {bmi}, you are underweight.")
else:
    print (f"Your BMI is {bmi}, you are clinically overweight.")