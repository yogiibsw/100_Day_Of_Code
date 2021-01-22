print("Welcome to the secret auction program.")

bids = {}
bidding_over = False

while not bidding_over:
    print("What's your name?")
    while True:
        name = input("> ")
        # reject an empty input
        if name == "":
            print("Please enter a name.")
        elif bids.get(name):
            print(f"There is already a bid by {name}. Please enter a different name.")
        else:
            break

    print("What is your bid?")
    while True:
        bid_str = input("> $")
        if bid_str == "0":
            print("$0 is not a proper bid. Please try again.")
        elif not bid_str.isdigit():
            print("Please enter a valid amount.")
        else:
            bid = int(bid_str)
            break

    bids[name] = bid

    print("Are there any other bidders? Type \"yes\" or \"no\".")
    choice = input("> ").lower()

    if choice == "no":
        bidding_over = True
        print("\n" * 100)

winner_name = ""
top_bid = 0
for key in bids:
    if bids[key] > top_bid:
        top_bid = bids[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${top_bid}.")