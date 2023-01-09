import functions

# Data Management Project

# Global Variable(s)
# Data files
data_list = functions.read_file('./text-files/trade-data-set.txt')
users = functions.read_file('./text-files/users.txt')
# Others
cur_user = None

# Run main function
def main():
    # Local Variable(s)
    main_loop = False
    login_loop = True
    line_num_1_archive = 0 #used in selection 1 of main menu func

    while login_loop:
        # Login or Sign-up Page
        print(
        '''
Welcome to Your Data Manager!
1. Login in
2. Sign up
3. Exit
        '''
        )

        # Get input
        option = input("Selection an option (1 or 3): ")

        if option == "1":
            cur_user = functions.login(users)
            # Login to account
            if cur_user == -1:
                print("Inccorect Username or Password")
            else:
                functions.main_menu(data_list, cur_user, users, main_loop, line_num_1_archive)
        
        elif option == "2":
            # Create account
            functions.sign_up(users)

        elif option == "3":
            login_loop = False
            print("Program Terminated")

        else: 
            print("Invalid Entry")

# Call main function to start program
main()