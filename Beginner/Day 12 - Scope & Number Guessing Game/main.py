from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Functions for game features

def check_answer(guess, answer, turns):
  """checks answer against guess."""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"Correct! The answer was {answer}. \n")
    if input("Play again? Type 'y' for yes and 'n' for no.\n").lower().strip() == "y":
      game()
    

def set_difficulty():
  level = input("Choose a difficulty. Type '0' for easy or '1' for hard: \n").strip()
  if level == "0":
    return EASY_LEVEL_TURNS
  elif level == "1":
    return HARD_LEVEL_TURNS
  else:
    print("You've entered an invalid input.")
    game()
    return 

def game():
  print(logo)
  
  print("Welcome to the Number Guessing Game!\n")
  print("Choose a number between 1 and 100.\n")
  answer = randint(1, 101)
  #to check
  #print(f"The correct answer is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.\n")

    #Let the user guess a number.
    guess = int(input("Make a guess: \n"))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.\n")
      if input("Play again? Type 'y' for yes and 'n' for no.\n").lower().strip() == "y":
        game()
      return
    elif guess != answer:
      print("Guess again.")

#start the game 
game()
