# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re
from tkinter.tix import InputOnly  # Needed for splitting text with a regular expression
import functions
# Global Variable(s)

def main():

    # Local Variable(s)
    loop = True
    
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    while loop:
        print("\nMain Menu")
        print(
            '''
            1: Spell Check a Word (Linear Search)
            2: Spell Check a Word (Binary Search)
            3: Spell Check Alice In Wonderland (Linear Search)
            4: Spell Check Alice In Wonderland (Binary Search)
            5: Exit
            '''
    )

        # Option Input
        num_select = input("Input number of desired option (1-S): ")

        # Process Input
        match num_select:
            case "1":
                word_select = input("Input a desired word: ").lower()
                
                # Start Linear Search
                print("Linear Search starting...")
                print(functions.linearSearch(dictionary, word_select))
            case "2":
                word_select = input("Input a desired word: ")
                print("2")
            case "3":
                print("3")
            case "4":
                print("4")
            case "5":
                print("Program Terminated")
                loop = False


# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

