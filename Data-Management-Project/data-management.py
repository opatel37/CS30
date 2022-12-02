import csv
import functions
import json

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Multi Accs - make a write+ function to create a new list for a user

# Data Management Project

# Global Variable(s)
data_list = functions.read_file('./trade-data-set.txt')

# Run main function
def main():

    # Local Variable(s)
    loop = True
    line_num_1_archive = 0

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

                # print(data_list[line_num_1:line_num_1 + 10])
                for i in range(line_num_1, line_num_1 + 10):
                    print("\n" + str(data_list[i]))
                
                # Set inner loop
                inner_loop_1 = True

                while inner_loop_1:
                    print(
'''
1. Display the next 10 items
2. Track back to last set of items displayed on previous visit
3. Return to Main Menu
'''
                    )

                    # Get input for inner loop
                    selection_1 = input("Input number of desired option (1-3): ")

                    # Process input
                    if selection_1 == "1":
                        # Add to line tracker
                        line_num_1 += 10

                        # print(data_list[line_num_1:line_num_1 + 10])
                        for i in range(line_num_1, line_num_1 + 10):
                            print("\n" + str(data_list[i]))

                    elif selection_1 == "2":
                        line_num_1 = line_num_1_archive

                        # print(data_list[line_num_1:line_num_1 + 10])
                        for i in range(line_num_1, line_num_1 + 10):
                            print("\n" + str(data_list[i]))

                    elif selection_1 == "3":
                        line_num_1_archive = line_num_1
                        inner_loop_1 = False

                    else:
                        print("Invalid Entry")

            case "2":
                # Set inner loop 
                inner_loop_2 = True

                while inner_loop_2:
                    print(
'''
Filter By: 
1. Day of the Week
2. Date
3. Return to Main Menu
'''
                    )

                    selection_2 = input("Input number of desired option (1-3): ")

                    if selection_2 == "1":
                        day = input("Enter the day you would like to see data for: ")

                        for item in data_list:
                            if item["Weekday"] == day.capitalize():
                                print(str(item) + "\n")

                    elif selection_2 == "2":
                        date = input("Enter the date you would like to see data for (DD/MM/YYYY): ")

                        for item in data_list:
                            if item["Date"] == date:
                                print(str(item) + "\n")


                    elif selection_2 == "3":
                        inner_loop_2 = False
                    
                    else: 
                        print("Invalid Entry")
            
            case "3":
                # Set inner loop 
                inner_loop_3 = True

                while inner_loop_3:
                    print(
'''
Sort By:
1. Date
2. Cumulative Value (Increasing)
3. Cumulative Value (Decreasing)
4. Return to Main Menu
'''
                    )

                    selection_3 = input("Input number of desired option (1-4): ")


                    match selection_3:
                        case "1":
                            functions.selection_sort(data_list, "Date", functions.sort_inc)
                            print(data_list)

                        case "2":
                            functions.selection_sort(data_list, "Cumulative", functions.sort_inc)
                            print(data_list)


                        case "3":
                            functions.selection_sort(data_list, "Cumulative", functions.sort_dec)
                            print(data_list)
                
                        case "4":
                            inner_loop_3 = False
                    
                        case other:
                            print("Invalid Entry")

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