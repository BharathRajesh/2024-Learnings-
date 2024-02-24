import os
def highest_bidder(bidder_data):
    highest_bidding=0
    winner=""
    for bidder in bidder_data:
        bidding_amount=bidder_data[bidder]
        if bidding_amount>highest_bidding:
            highest_bidding=bidding_amount
            winner=bidder
    print(f"all the bidders are {bidder_data}")
    print(f"the winner is {winner} with {highest_bidding} bidding amount")

bidder_data={}
end_of_bidder=False
while not end_of_bidder:
    name=input("Enter the name of the bidder:")
    price=int(input("Enter the bidding price:"))
    bidder_data[name]=price
    more_bidders=input("is any bidders exist still 'yes' / 'no'?").lower()
    if more_bidders=='no':
        end_of_bidder=True
        highest_bidder(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
