from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

def find_highest_bidder(bidding_record):
    winner = ''
    winning_bid = 0

    for name in bids:
        if winning_bid < bids[name]:
            winner = name
            winning_bid = bids[name]
            
    print(f"The winner is {winner} with a bid of ${winning_bid}.")
       
bids = {}
more_bidder = True
while more_bidder:
    clear()
    print(logo)
    print("Welcome to the secret auction program.")
    bidder = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    bids[bidder] = bid_amount

    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_bids == 'no':
        more_bidder = False
    
    # more bidder - clear screen and loop

# display winner

find_highest_bidder(bids)
        