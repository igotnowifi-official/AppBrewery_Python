#Banker Roulette

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_generator = random.randint (0,len(names) -1)
random_name = names [random_generator]
print (f"{random_name} is going to buy the meal today!")
print (names [1][1])