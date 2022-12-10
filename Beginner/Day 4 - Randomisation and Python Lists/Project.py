#Rock, Paper, Scissors

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image_move = [rock, paper, scissors]

#Welcome note and instruction
print("Welcome to Rock, Paper, Scissors. Type '0' for Rock, '1' for Paper, and '2' for Scissors. According to the rules of the game, try to beat the computer. \n")

#Player move
player_move = int(input("Pick a move: \n"))
if player_move >=3 or player_move <=0:
    print("You've entered an invalid number.")
else:
    print(image_move[player_move])

    #computer move
    computer_move = random.randint(0,2)
    print(image_move[computer_move])

    #compete
    if player_move == computer_move:
        print("draw. ")
    elif player_move > computer_move:
        print("Player wins.")
    elif player_move < computer_move:
        print("Computer wins.")
    elif player_move == "0" and computer_move == "2":
        print("Player wins.")
    elif player_move == "2" and computer_move == "0":
        print("Computer wins.")
    else: 
        print("You've entered an invalid move.")