
import os
bids ={}
bidding_finished = False

def clear_console():
    # Clear console based on the platform
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")        
        
    
while not bidding_finished: 
    name = input("What is the name of the bidder?")
    price = input("Enter the amount of bid : ")
    bids[name] =price
    cont = input("Are there anymore bidders? Type 'yes' or 'no'.")
    if cont == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif cont == "yes":
        clear_console()
        