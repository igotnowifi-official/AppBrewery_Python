#Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Enter bill amount
bill = int(input("Enter your bill amount: \n"))
#Enter number of people paying
person = int(input("How many people will be splitting? \n"))
#Enter tip
tip = int(input("Enter tip amount WITHOUT percentage sign in numeral form (ie. 12): \n"))
#Result generator and rounding to 2 decimal places
result = round((bill / person) * (1+(tip/100)),2)
#Printing
print(f"Your final bill per person is: {result} USD after tips.")
