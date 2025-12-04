# Auction Bidder

print("Welcome to the Secret auction Program!!!")

bids={}
auction=True
while auction:
    # take user input
    
    name=input("What is your name? ")
    price=float(input("What is your bid?: $"))
    #  saving data into dictionary
    
    bids[name]=price
    max_key=max(bids, key=bids.get)
    max_value=max(bids.values())
    # Checking if there are more bidders
    
    again=input("Are there any other bidders? type 'yes' or 'no'. ").lower() 
    if again=="yes":
        auction=True
        print("\n"*100)
    elif again=="no":
        auction=False
        print("\n"*100)
        print(f"The winner is {max_key} with a bid of ${max_value}")


