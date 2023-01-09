# Student Grades Assignment

# Global Variable(s)
import functions

# Get array as a global variable
grades = functions.generate_grades()

# Main Program Loop
loop = True

while loop:
    # Print Menu Options
    print(
    '''
    Student Grades Menu
    1. Display All Grades
    2. Display Honours
    3. Stats
    4. Randomize Grades
    5. Exit    

    '''
    )

    # Input
    selection = input("Input number of desired option (1-5): ")

    # Process & Output
    match selection:
        case "1": 
            print("ALL GRADES")

            # Display Grades
            functions.print_grades(grades)
    
        case "2":
            print("HONOURS")
            
            # Display grades
            for item in grades:
                if item >= 80:
                    print(str(item) + " %")

        case "3":
            print("STATS")
            print("Highest Grade: " + str(max(grades)) + " %")
            print("Lowest Grade: " + str(min(grades)) + " %")
            print("Average Average: " + str(round(sum(grades) / len(grades), 2)) + " %")

        case "4":
            print("RANDOM SET OF GRADES")

            # Randomize grades
            grades = functions.generate_grades()

            # Display grades
            functions.print_grades(grades)

            print("\nGRADES HAVE BEEN RANDOMIZED")

        case "5":

            print("Program Terminated")
            loop = False