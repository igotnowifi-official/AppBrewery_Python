# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

###################### End of Instructions ########################

#Start of Assignment


from game_data import data
import random
from art import logo, vs
from replit import clear

# Setting up game features:
def random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # to check
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against guess 
  and returns 'true' if right.
  Or 'false' if wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  to_continue = True
  account_a = random_account()
  account_b = random_account()

  while to_continue:
    account_a = account_b
    account_b = random_account()

    while account_a == account_b:
      account_b = random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': \n").lower().strip()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if correct:
      score += 1
      print(f"You're right! Current score: {score}.\n")
    else:
      to_continue = False
      print(f"Sorry, that's wrong. Final score: {score}.\n")
      if input("Play again? Type 'y' for yes and 'n' for no.\n").lower() == 'y':
        clear()
        game()

#Start of game:
game()

