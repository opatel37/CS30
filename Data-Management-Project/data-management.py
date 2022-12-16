import csv
import functions
import json

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Multi Accs - make a write+ function to create a new list for a user

# Data Management Project

# Global Variable(s)
# Data files
data_list = functions.read_file('./text-files/trade-data-set.txt')
users = functions.read_file('./text-files/users.txt')
# Other(s)
cur_user = None

# Run main function
def main():

    # Local Variable(s)
    line_num_1_archive = 0 #used in selection 1
    main_loop = False
    login_loop = True

    while login_loop:
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
            user_login = functions.login(users)
            # Login function
            if user_login == -1:
                print("Inccorect Username or Password")
            else:
                cur_user = user_login
                main_loop = True
                login_loop = False
        
        elif option == "2":
            functions.sign_up(users)

        else: 
            print("Invalid Entry")

main()