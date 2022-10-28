# Nickname Generator Assignment

# Global Variables
import random
nicknames = ["The Moon Mourner", "The Star Skipper", "The Galaxy Gazer", "The All Knowing", "The Planet Destroyer", "The Blackhole Blaster", "The Universe Seer", "The Death Stalker", "The Winter Watcher", "The Underworld Wanderer"]

# Get username
first_name = str(input("\nPlease enter your first name: "))
last_name = str(input("Please enter your last name: "))

loop = True

while loop:
    print("\nMain Menu (" + first_name + " " + last_name + ")")
    print(
        '''
        1. Change Name
        2. Display a Random Nickname
        3. Display All Nicknames
        4. Add a Nickname
        5. Remove a Nickname
        6. Exit
        '''
    )

    # Input
    selection = input("Input number of desired option (1-6): ")

    # Process Input
    match selection:
        case "1":
            print("\nCHANGE NAME")
            first_name = str(input("\nPlease enter your new first name: "))
            last_name = str(input("Please enter your new last name: "))
            print("Current name is: " + first_name + " " + last_name)
        
        case "2":
            print("\nRANDOM NICKNAME")
            print("\n" + first_name + " " + random.choice(nicknames) + " " + last_name)
        
        case "3":
            print("\nALL NICKNAMES")

            # Cycle through array to print each nickname
            for item in nicknames:
                print("\n" + first_name + " " + item + " " + last_name)
        
        case "4":
            print("ADD NICKNAME")

            # Get input
            new_nickname = str(input("\n Please enter new nickname: ")).title()
            
            # Process & Output
            if new_nickname in nicknames:
                print("This nickname already exists")
            else:
                # Capitialize first letter in new nickname 
                nicknames.append(new_nickname)
                print(new_nickname + " added to the nickname list")

        case "5":
            print("REMOVE NICKNAME")

            # Get input (capitalize first letter of inputed nickname)
            selected_nickname = str(input("\nPlease enter the nickname that you wish to remove: ")).title()

            # Process & Output
            if selected_nickname in nicknames:
                nicknames.remove(selected_nickname)
                print(selected_nickname + " was removed from the nickname list")
            else:
                print(selected_nickname + " was not found")

        case "6":
            print("\nPROGRAM TERMINATED")
            loop = False


    