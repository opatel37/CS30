import json

# Functions

def read_file(file_name):
    file = open(file_name, 'r')
    info = json.load(file)
    file.close()
    return info

def write_data(selected_data, save_to):
    file = open(save_to, 'w')
    json.dump(selected_data, file)
    file.close()

def selection_sort(anArray, sort_param, compare_funct):
    for fill_slot in range(len(anArray)):
        min_pos = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if compare_funct(anArray[post_fill][sort_param], anArray[min_pos][sort_param]):
                min_pos = post_fill

        anArray[min_pos], anArray[fill_slot] = anArray[fill_slot], anArray[min_pos]

def sort_inc(val_1, val_2):
    if val_1 < val_2:
        return True

def sort_dec(val_1, val_2):
    if val_1 > val_2:
        return True

def search_data(list, key, val):
  for i in range(len(list)):
      if list[i][key] == val:
          return i

  return -1

def login(user_list):
    print("Please login to access data...")

    login_username = input("Username: ")
    login_password = input("Password: ")

    if check_creds(user_list, login_username, login_password):
        user_info = open_user_spec_fav_list(user_list, login_username)
        return user_info

    else:
        return -1

def sign_up(user_list):
    # Sign up function
        print("Please create username and password...")

        sign_up_username = input("Username: ")
        sign_up_password = input("Password: ")

        if check_creds(user_list, sign_up_username, sign_up_password):
            print("Username/Password already in use")
        else:
            user_list.append(create_new_acc(sign_up_username, sign_up_password))
            write_data(user_list, './text-files/users.txt')

def create_new_acc(username, password):
    dict = {
        "Username": username,
        "Password": password,
        "Favorites": []
    }

    return dict

# Take in username and password along with the list of credentials
# Return True or False
def check_creds(list, username, password):
    for i in range(0, len(list)):
        if list[i]["Username"] == username and list[i]["Password"] == password:
            return True

    return False

def check_fav_list(user, item_in):
    for i in range(len(user["Favorites"])):
        if user["Favorites"][i]["Date"] == item_in:
            return -1
        else:
            return None

def open_user_spec_fav_list(list, username):
    for i in range(0, len(list)):
        if list[i]["Username"] == username:
            return list[i]

def print_10_lines(list, line_num):
    # print(data_list[line_num_1:line_num_1 + 10])
    for i in range(line_num, line_num + 10):
        print("\n" + str(list[i]))

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
    
def add_to_fav(list, date, username):
    for i in range(0, len(list)):
        if list[i]["Date"] == date:
            username["Favorites"].append(list[i])
            return None

    return -1

def set_fav_list(list, user):
    for i in range(0, len(list)):
        if list[i]["Username"] == user["Username"]:
            list[i]["Favorites"] = user["Favorites"]
 
def print_out_list(list):
   for i in range(len(list)):
        print("\n" + str(list[i]))

def main_menu(data, user_creds, all_users, loop, line_tracker):
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
                    print("\n" + str(data[i]))
                
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
                        print_10_lines(data, line_num_1) 
                    
                    elif select_1 == "2":
                        # Set current line # to the one the user was at during last session
                        line_num_1 = line_tracker

                        # print(data_list[line_num_1:line_num_1 + 10])
                        print_10_lines(data, line_num_1)

                    elif select_1 == "3":
                        line_tracker = line_num_1
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

                        filtered_search = filter_search(data, day, "Weekday")

                        print_out_list(filtered_search)

                    elif select_2 == "2":
                        date = input("Enter the date you would like to see data for (YYYY-MM-DD): ")

                        filtered_search = filter_search(data, date, "Date")

                        print_out_list(filtered_search)

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
                            selection_sort(data, "Date", sort_inc)
                            print(data)

                        case "2":
                            selection_sort(data, "Cumulative", sort_inc)
                            print(data)


                        case "3":
                            selection_sort(data, "Cumulative", sort_dec)
                            print(data)
                
                        case "4":
                            inner_loop_3 = False
                    
                        case other:
                            print("Invalid Entry")

            case "4":
                select_4 = input("Input date of trade you wish to add to favorites (YYYY-MM-DD): ")

                # Check if item is already in fav list
                if check_fav_list(user_creds, select_4) == -1:
                    print("Item is already in favorites")
                else:

                    # Check if item exists, add if it does
                    if add_to_fav(data, select_4, user_creds) == -1:
                        print("Item DNE")
                    else:
                        print("Item has been added to favorites")
                    
                    # Add to current user's fav list
                    write_data(all_users, './text-files/users.txt')

            case "5":
                select_5 = input("Input date of trade you wish to remove from favorites (YYYY-MM-DD): ")

                fav_list = user_creds["Favorites"]
                
                search_return_idx = search_data(fav_list, "Date", select_5)
                
                if search_return_idx == -1:
                    print("Data was not found in favorites")
                else:
                    del user_creds["Favorites"][search_return_idx]
                    print("Item has been removed from favorites")
                    
                write_data(all_users, './text-files/users.txt')

            case "6":
                for i in range(0, len(user_creds["Favorites"])):
                    print("\n" + str(user_creds["Favorites"][i]))


            case "7":
                loop = False
                print ("Signed Out")

            case other:
                print("Invalid Entry")