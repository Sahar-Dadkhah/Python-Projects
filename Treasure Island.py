print("Welcomme to Treasure Island .\nYou have to find the Treasure !")
road=input("You are in a cross road. Where do you want to go ?\nleft or right?\n").lower()
if road=="left":
    print("You come to a lake.\nThere is an island in the middle of the lake .\nWill you wait for a boat or swim across the lake?")
    lake=input("swim or wait?\n").lower()
    if lake=="wait":
        print("You arrive at the island .There are 3 doors .\nWhich color will you choose?")
        door=input("orange or blue or yellow?\n").lower()
        if door=="yellow":
            print("YOU FIND THE TREASURE!")
        else:
            print("You found snakes!\nGame over!")
    else:
        print("You are drowning in water!\nGame over!")
else:
    print("You are burning in fire! \nGame over!")
input("")