#Heads or Tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_number = random.randint (1,2)
if str(random_number) == "1":
    print ("Tails")
else:
    print ("Heads")
