# Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name3 = name1 + name2. lower()
t = name3.count('t')
r = name3.count('r')
u = name3.count('u')
e = name3.count('e')
first_digit = t + r + u + e
l = name3.count('l')
o = name3.count('o')
v = name3.count('v')
e = name3.count('e')
second_digit = l + o + v + e
love_score = str(first_digit) + str(second_digit)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print (f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")