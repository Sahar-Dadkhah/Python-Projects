from replit import clear
logo=r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""
print(logo)
print("Welcome to the secret auction program !")
bids={}
continue_action=True
while continue_action:
    name=input("What's your name ? : ")
    price=int(input("What's your bid?: $ "))
    bids[name]=price
    action=input("Is there anyone else? Type \'yes' or \'no' :")
    if action=="no":
        continue_action=False
    else:
        clear()
highest_bid=0
winner=""
for name in bids:
    if bids[name]>highest_bid:
        highest_bid=bids[name]
        winner=name

print(f"The winner is {winner} with a bit of ${highest_bid}")


    

print (bids)


input("")
