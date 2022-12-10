#Create a Password Generator

# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
if nr_letters >=53 or nr_letters <=0:
    print("You're entered an invalid number.") 
else:
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    if nr_symbols >=10 or nr_symbols <=0:
        print("You're entered an invalid number.") 
    else:
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        if nr_numbers >=11 or nr_numbers <=0:
            print("You're entered an invalid number.")  
        else:

            #Eazy Level - Order not randomised:
            #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

            # password = ""

            # adding characters
            # for char in range(1, nr_letters + 1):
                # password += random.choice(letters)

            # adding symbols
            # for char in range(1, nr_symbols + 1):
                # password += random.choice(symbols)

            # adding numbers
            # for char in range(1, nr_numbers + 1):
                # password += random.choice(numbers)
            
            # final password
            # print(password)



            #Hard Level - Order of characters randomised:
            #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

            password_list = []

            # for random letters
            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            # for random symbols
            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            # for random numbers
            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            #printing list to check
            # shuffling list into a random positioned password
            #print(password_list)
            random.shuffle(password_list)
            #print(password_list)      
            password = ""
            for char in password_list:
                password += char

            #printing final password
            print(f"Your final password is: {password}.")  