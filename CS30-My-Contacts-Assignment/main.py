import json
import functions

# MY CONTACTS ASSIGNMENT

# Global Variable(s)
loop = True
contacts = functions.read_info()

# MAIN MENU

while loop: 
    print(
        '''
        CONTACT'S LIST

        1. Display Contact Names
        2. Search for Contact
        3. Edit Contact
        4. New Contact
        5. Remove Contact
        6. Exit

        '''
    )

    # Input
    selection = input("input number of desired option (1-6): ")

    # Input
    match selection: 
        case "1":
            print("CONTACT NAMES")
            functions.print_names(contacts)

                
        case "2":
            print("\nSearch for Contact")
            
            wanted_con = input("Input a contact name: ")
            

            search_find_con = functions.search_con(contacts, wanted_con)

            # Output depending on if contact was found
            if search_find_con == -1:
                print("\nContact DNE")   
            else: 
                # Space out output lol
                print("\n")

                # Output info on contact
                for key, value in contacts[search_find_con].items():
                    print(key, ":", value)

        case "3":
            print("\nEdit Contact")

            # Get input
            edit_con = input("Input contact name you wish to edit: ")

            # Check if contact exists
            edit_found_con = functions.search_con(contacts, edit_con)

            if edit_found_con == -1:
                print("Invalid Entry")
            else:
                edit_con_name = input("Input new contact name: ")
                edit_con_phone_num = input("Input new contact phone #: ")
                edit_con_email = input("Input new contact email: ")

                # Replace old info with new
                replace_con = contacts[edit_found_con]
                replace_con["Name"] = edit_con_name
                replace_con["Phone #"] = edit_con_phone_num
                replace_con["Email"] = edit_con_email

                functions.save_contacts(contacts)

                print("Information has been changed")
            
        case "4":
            print("\nNew Contact")

            # Get info
            add_con_name = input("Input contact name: ")
            add_con_phone_num = input("Input contact phone #: ")
            add_con_email = input("Input contact email: ")

            # Create new dict
            con_dict = {
                "Name": add_con_name, 
                "Phone #": add_con_phone_num, 
                "Email": add_con_email
            }

            # Add dict to list
            contacts.append(con_dict)

            functions.save_contacts(contacts)

            print("Contact has been added")

        case "5":
            print("\nRemove Contact")

            # Get info
            remove_con_name = input("Input contact name: ")

            # search for contact name
            remove_find_con = functions.search_con(contacts, remove_con_name)

            # if contact found remove and send confirmation message
            if remove_find_con == -1:
                print("Contact DNE")
            else: 
                contacts.pop(remove_find_con)
                print("Contact has been removed")

                functions.save_contacts(contacts)

        case "6":
            # Exit Program
            print("Program Terminated")
            loop = False
