print("----------------------" + "welcome to blind auction" + "-----------------")

# Initialize an empty dictionary to store bids
highest_bids = {}

# Get the first bidder's name and bid
name = input("What is your name?")
bids = input("What is your bid? $")

# Store the first bid in the dictionary
highest_bids[name] = bids

# Ask if there are more bidders
should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
continue_bidding = True
while continue_bidding :
    print("\n"* 50)
    name = input("What is your name? ")
    bids = input("What is your bid? $")
    highest_bids[name] = bids
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if should_continue == 'no':
        continue_bidding = False
        print(" \n" * 5)
        print("----------------------" + "Bidding for auction has ended" + "-----------------")
# Find the highest bidder
highest_bidder = max(highest_bids, key=highest_bids.get)
highest_bid = highest_bids[highest_bidder]
# Display the highest bid and bidder
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")