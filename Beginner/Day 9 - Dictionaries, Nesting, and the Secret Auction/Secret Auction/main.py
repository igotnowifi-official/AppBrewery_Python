from replit import clear
from art import logo
print(logo)

#Setting up
bids = {}
end_bidding = False

#function to find highest bidder
def highest_bidder(bidding_list):
  highest_bid = 0
  winner = ""

  for bidder in bidding_list:
    bid_amount = bidding_list[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of US ${highest_bid}.\n")

#start program:
while not end_bidding:
  name = input("What is your name?: \n")
  price = int(input("What is your bid?: $\n"))
  bids[name] = price
  to_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower().strip()
  if to_continue == "no":
    end_bidding = True
    highest_bidder(bids)
  elif to_continue == "yes":
    clear()
