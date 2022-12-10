#Treasure Island

import random

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#Introduction
print("You've entered a dreamlike forest, the path forks to two roads and you have to choose which path to go through.\n")
path = input("Type 'right' to go to the right, an easy road ahead; Type 'left' to go to the scary-looking path on the left.\n").lower().strip()

# To win, go right and enter green door, then if answer question right get treasure.
if path == "right":
    print("You passed through the forest with ease, suddenly you see a leprechaun in between two doors.\n")
    door = input("Leprechaun says: Type 'green' to get my pot of gold behind the green door and type 'red' for the pot of coal behind the red door\n").lower().strip()
    if door == "green":
        print("You found the pot of gold, but there is a fairy guarding it.\n")
        answer = input("Fairy asks: This is MY gold, but I'll share it with you if you get the answer right. What is 1+1? Hint: Type a number.\n").strip()
        if answer == "11":
            print("Congrats you got the gold!\n")

# Lose, get answer wrong
        else:
            print("Fairy says: Too bad, you're wrong. I'm going to take all your teeth. Game over\n")

# Lose, go red door
    else:
        print("You went in the red door and was met with a pot of coal. Guess the Leprechaun did not lie. Game Over\n")

# Lose, go left
else:
    print("You took the path less taken, there was a reason why; You feel down a cliff right to the middle of a firepit surrounded by ogres. Game Over\n")
