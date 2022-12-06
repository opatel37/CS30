import csv
import functions
import json

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Multi Accs - make a write+ function to create a new list for a user

# Data Management Project

# Global Variable(s)
data_list = functions.read_file('./text-files/trade-data-set.txt')
fav_list = functions.read_file('./text-files/favorites.txt')
user_creds = functions.read_file('./text-file/login-credtials.txt')

# Run main function
def main():

    # Local Variable(s)
    loop = True
    line_num_1_archive = 0

    # Login or Sign-up Page
    print(
'''
Welcome to Your Data Manager!
1. Login in
2. Sign up
'''
    )

    option = input("Selection an option (1 or 2): ")

    if option == "1":
        # Login function
        # Login page
        print(
'''
Please login to access data...
'''
        )

        username = input("Username: ")
        password = input("Password: ")

        if username ==  
        
    elif option == "2":
        # Sign up function

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

        select = input("Input number of desired option (1-7): ")

        match select:
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
                    select_1 = input("Input number of desired option (1-3): ")

                    # Process input
                    if select_1 == "1":
                        # Add to line tracker
                        line_num_1 += 10

                        # print(data_list[line_num_1:line_num_1 + 10])
                        for i in range(line_num_1, line_num_1 + 10):
                            print("\n" + str(data_list[i]))

                    elif select_1 == "2":
                        line_num_1 = line_num_1_archive

                        # print(data_list[line_num_1:line_num_1 + 10])
                        for i in range(line_num_1, line_num_1 + 10):
                            print("\n" + str(data_list[i]))

                    elif select_1 == "3":
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

                    select_2 = input("Input number of desired option (1-3): ")

                    if select_2 == "1":
                        day = input("Enter the day you would like to see data for: ")

                        for item in data_list:
                            if item["Weekday"] == day.capitalize():
                                print(str(item) + "\n")

                    elif select_2 == "2":
                        date = input("Enter the date you would like to see data for (DD/MM/YYYY): ")

                        for item in data_list:
                            if item["Date"] == date:
                                print(str(item) + "\n")


                    elif select_2 == "3":
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

                    select_3 = input("Input number of desired option (1-4): ")


                    match select_3:
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
                select_4 = input("Input date of trade you wish to add to favorites (YYYY-MM-DD): ")

                # Functionize so if no trade took place that day it returns -1 and check if trade is already in fav list
                for i in range(0, len(data_list)):
                    if data_list[i]["Date"] == select_4:
                        fav_list.append(data_list[i])
                
                functions.save_data(fav_list, './text-files/favorites.txt')

            case "5":
                select_5 = input("Input date of trade you wish to remove from favorites list (YYYY-MM-DD): ")

                search_return_val = functions.search_data(fav_list, "Date", select_5)

                if search_return_val == -1:
                    print("Data was not found in list")
                else:
                    fav_list.pop(search_return_val)

                functions.save_data(fav_list, './text-files/favorites.txt')

            case "6":
                for i in range(0, len(fav_list)):
                  print("\n" + str(data_list[i]))

            case "7":
                loop = False
                print ("Program Terminated")

            case other:
                print("Invalid Entry")

main()