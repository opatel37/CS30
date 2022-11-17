import csv
import functions
import json

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Data Management Project

# Global Variable(s)
data_list = functions.read_file()

# Run main function
def main():

    # Local Variable(s)
    loop = True

    # Main Menu (while loop)
    while loop:
        print(
        '''
DATE MANAGEMENT MAIN MENU

1. Display First 10 Items in Data Set
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

                # Track lines printed
                line_num_1 = 0

                # Print data
                print(data_list[line_num_1:line_num_1 + 10])
                
                # Set inner loop
                inner_loop = True

                while inner_loop:
                    print(
'''
1. Display the next 10 items
2. Exit to Main Menu                        
'''
                    )

                    # Get input for inner loop
                    selection_1 = input("Input number of desired option (1-2): ")

                    # Process input
                    if selection_1 == "1":
                        # Add to line tracker
                        line_num_1 += 10

                        print(data_list[line_num_1:line_num_1+10])
                        
                    elif selection_1 == "2":
                        inner_loop = False

                    else:
                        print("Invalid Entry")

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
            case other:
                print("Invalid Entry")

main()