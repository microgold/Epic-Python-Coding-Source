print("Welcome to the Looping Treasure Hunt Adventure!")
print("You are in a dense forest, searching for the hidden treasure.")

treasure_found = False
while not treasure_found:
    choice = input("Do you want to go left or right? (left/right) ")

    if choice == "left":
        print("You've stumbled upon a hidden cave!")
        choice = input("Do you dare to enter the cave? (yes/no) ")
        if choice == "yes":
            print("Inside the cave, you found the treasure! Congratulations!")
            treasure_found = True
        else:
            print("You chose to stay outside. The forest awaits your next move.")
    elif choice == "right":
        print("You come across a swiftly flowing river.")
        choice = input("Do you wish to swim across or follow the river? (swim/follow) ")
        if choice == "swim":
            print("Bravely swimming across, you reach a deserted beach, but no treasure here.")
        else:
            print("Following the river, you find a bridge leading to a mysterious temple.")
            choice = input("Do you cross the bridge? (yes/no) ")
            if choice == "yes":
                print("In the temple, you find the hidden treasure! Your quest is complete!")
                treasure_found = True
            else:
                print("You decide not to cross. The river path stretches endlessly before you.")
    else:
        print("Lost in the forest, you decide to stop and rest. Maybe try another path next time.")
