# Leap Year Calculator

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
mod_1 = year % 4
mod_2 = year % 100
mod_3 = year % 400

if mod_1 ==0:
    if mod_2 ==0:
        if mod_3 ==0:
            print ("Leap year.")
        else:
            print ("Not leap year.")
    else:
        print ("Leap year.")
else:
    print ("Not leap year.")
