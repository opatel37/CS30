from xml.etree.ElementTree import TreeBuilder
import functions
import json 

# Data Management Project

# Global Variable(s)
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

'''
    )