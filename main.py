from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

print("Welcome to the secret auction program")

#defining a variable for the while loop
bids = {}
end_bid = False

#bidding_record is the input that represents the dictionary in bids {} which represents the values
def highest_bid(bidding_record):
    highest_bidder = 0
    winner = ""
    #when looping through a dictionary it will only loop through keys not value
    for bidder in bidding_record:
        #taking bidding_record and passing in key will get the value 
        bid_amount = bidding_record[bidder]
      #bid_amount is greater than highest_bidder 0 then highest bidder becomes bid_amount
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            #the winner becomes the bidder who had the highest bid
            winner = bidder
        #printing the winner which is the name(key) and the highest bidder that was established as 0
    print(f"The winner is {winner} with the winning bid of {highest_bidder}")     
#if user answers yes to more bidders then while loop will continue until input is no
while not end_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid.: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if more_bidders == 'no':
        end_bid = True
        #calling the function 
        highest_bid(bids)
    else:
        clear()
    

        




    
    
    