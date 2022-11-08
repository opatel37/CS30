import csv

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Data Management Project

# Global Variable(s)
data_file = open("trade-data-set.csv", "r")
    
for line in data_file:
    print(line)

    # reader = csv.DictReader(data_file)
    # for row in reader:
    #     print(row['Direction'], row['Year'], row['Data'], row['Weekday'], row['Country'], row['Commodity'], row['Transport_Mode'], row['Measure'], row['Value'], row['Cumulative'])


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
                print("1")
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