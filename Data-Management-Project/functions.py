import json

# Functions

def read_file(file_name):
    file = open(file_name, 'r')
    list = json.load(file)
    file.close()
    return list

def write_data(selected_data, save_to):
    file = open(save_to, 'w')
    json.dump(selected_data, file)
    file.close()

# Used to sort data depending on which option user wants (Inc/Dec)
def selection_sort(anArray, sort_param, compare_funct):
    for fill_slot in range(len(anArray)):
        min_pos = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if compare_funct(anArray[post_fill][sort_param], anArray[min_pos][sort_param]):
                min_pos = post_fill

        anArray[min_pos], anArray[fill_slot] = anArray[fill_slot], anArray[min_pos]

# Sort by increasing values
def sort_inc(val_1, val_2):
    if val_1 < val_2:
        return True

# Sory by decreasing values
def sort_dec(val_1, val_2):
    if val_1 > val_2:
        return True

# Search for item and return index if found
def search_data(list, key, val):
    for i in range(len(list)):
      if list[i][key] == val:
          return i

    return -1

# Verify credentials and login to correct user
def login(user_list):
    print("Please login to access data...")

    login_username = input("Username: ")
    login_password = input("Password: ")

    if find_user(user_list, login_username, login_password):
        # login_username is not a dict
        for i in range(len(user_list)):
            if user_list[i]['Username'] == login_username:
                return user_list[i]['Favorites']
    else:
        return -1

# Take in list of all users, return dict containing new user credential
def sign_up(user_list):
        print("Please create username and password...")

        sign_up_username = input("Username: ")
        sign_up_password = input("Password: ")

        if find_user(user_list, sign_up_username, sign_up_password):
            print("Username/Password already in use")
        else:
            user_list.append(create_new_acc(sign_up_username, sign_up_password))
            write_data(user_list, './text-files/users.txt')

# Used to convert given credentials into a new user in the form of a dict
def create_new_acc(username, password):
    dict = {
        "Username": username,
        "Password": password,
        "Favorites": []
    }

    return dict

# Verify inputed credentials against data base
# Return True or False
def find_user(list, username, password):
    for i in range(0, len(list)):
        if list[i]['Username'] == username and list[i]['Password'] == password:
            return True

    return False

# Check if item is in fav list or not
def check_fav_list(list, item_in):
    for i in range(len(list)):
        if list[i]['Date'] == item_in:
            return -1
    else:
        return None

# Used in selection 1 of main menu func
def print_10_lines(list, line_num):
    for i in range(line_num, line_num + 10):
        print("\n" + str(list[i]))

# Search and output any items that fit chosen filter
def filter_search(list, filter, key):
    temp_list = []
    for item in list:
        if item[key] == filter.capitalize():
            temp_list.append(item)
    
    if temp_list == []:
        print("No trades took place that day, please try again")
        return temp_list
    else:
        return temp_list

# Add item to current users favorites list according to given date
def add_to_fav(list, date, favs):
    for i in range(0, len(list)):
        if list[i]['Date'] == date:
            favs.append(list[i])
            return None

    return -1
 
# Print out items in a given list
def print_list(list):
   for i in range(len(list)):
        print("\n" + str(list[i]))

def sort_data_manager(info_3):
        # Sort data according to users input then print sorted data
        # Changes only effect current session
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
                        selection_sort(info_3, "Date", sort_inc)
                        print(info_3)

                    case "2":
                        selection_sort(info_3, "Cumulative", sort_inc)
                        print(info_3)


                    case "3":
                        selection_sort(info_3, "Cumulative", sort_dec)
                        print(info_3)

                    case "4":
                        inner_loop_3 = False
                        return None
                
                    case other:
                            print("Invalid Entry")

def add_fav_manager(list, favs_list, user_list):
    select_4 = input("Input date of trade you wish to add to favorites (YYYY-MM-DD): ")

        # Check if item is already in fav list, don't act if it does
    if check_fav_list(favs_list, select_4) == -1:
        print("Item is already in favorites")
    else:

        # Check if item exists, add if it does
        if add_to_fav(list, select_4, favs_list) == -1:
            print("Item DNE")
        else:
            print("Item has been added to favorites")
        
        # Save current sessions fav list to file
        write_data(user_list, './text-files/users.txt')

def print_data_management(list, line_tracker_archive):
    # Track lines printed
    line_num_1 = 0

    print_10_lines(list, line_num_1)
    
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

            print_10_lines(list, line_num_1) 
        
        elif select_1 == "2":
            # Set current line # to the one the user was at during last session
            line_num_1 = line_tracker_archive

            print_10_lines(list, line_num_1)

        elif select_1 == "3":
            line_tracker_archive = line_num_1
            inner_loop_1 = False
            return line_tracker_archive

        else:
            print("Invalid Entry")

def filter_manager(list):
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

            filtered_search = filter_search(list, day, "Weekday")

            print_list(filtered_search)

        elif select_2 == "2":
            date = input("Enter the date you would like to see data for (YYYY-MM-DD): ")

            filtered_search = filter_search(list, date, "Date")

            print_list(filtered_search)

        elif select_2 == "3":
            inner_loop_2 = False
        
        else: 
            print("Invalid Entry")

def remove_fav_manager(list, save_file):
    select_5 = input("Input date of trade you wish to remove from favorites (YYYY-MM-DD): ")
  
    # Search through users fav list 
    # Returns item for that date or returns -1 if no trade was found
    search_return_idx = search_data(list, "Date", select_5)
    
    if search_return_idx == -1:
        print("Data was not found in favorites")
    else:
        del list[search_return_idx]
        print("Item has been removed from favorites")
        
    write_data(save_file, './text-files/users.txt')

          
# Start main menu
def main_menu(data, fav_list, all_users, loop, line_tracker):
    # Start main menu loop
    loop = True

    # Main Menu (while loop)
    while loop:
        print(
        '''
DATE MANAGEMENT MAIN MENU

1. Display First 10 Items in Data Set
2. Search/Filter Data
3. Sort Data
4. Add to Favorites List
5. Remove Data from Favorites List
6. Display Favorites List
7. Exit
        '''
            )

        select = input("Input number of desired option (1-7): ")

        match select:
            case "1":
                # Set line tracker to manipulate the global variable
                line_tracker = print_data_management(data, line_tracker)

            case "2":
                filter_manager(data)
            
            case "3":
                sort_data_manager(data)

            case "4":
                add_fav_manager(data, fav_list, all_users)

            case "5":
                remove_fav_manager(fav_list, all_users)
      
            case "6":
                print_list(fav_list)

            case "7":
                loop = False
                print ("Signed Out")

            case other:
                print("Invalid Entry")