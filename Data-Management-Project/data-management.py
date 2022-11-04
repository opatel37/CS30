# import functions
import json
import pandas
# Data Management Project

# Global Variable(s)


def main():

    # Local Variable(s)
    loop = True

    # Main Menu (while loop)
    while loop:
        print(
        '''
DATE MANAGEMENT MAIN MENU

1. Display All Data
2. Search/Filter Data
3. Sort Data
4. Add to Favourites List
5. Remove Data from Favourites List
6. Display Favourites List
7. Exit

        '''
            )

        selection = input("Input number of desired option (1-7): ")

        match selection:
            case "1":
                test = pandas.read_excel(r"F:\CS30\Data-Management-Project\trade-data-set.csv")
                print(test)
            case "2":
                print("2")
            case "3":
                print("3")
            case "4":
                print("4")
            case "5":
                print("5")
            case "6":
                print("6")
            case "7":
                loop = False
                print ("Program Terminated")


main()