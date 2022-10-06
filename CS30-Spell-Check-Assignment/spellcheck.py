# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re
from tkinter.tix import InputOnly  # Needed for splitting text with a regular expression
import time
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
                # Local Variable(s)
                word_select_linear = input("Input a desired word: ").lower()
                
                # Start timer
                start_linear_dict = time.time()
                word_search_linear = functions.linearSearch(dictionary, word_select_linear)
                
                # Check if word is in dictionary
                if word_search_linear == -1:
                    print(str(word_select_linear) + "was not found" )
                else:
                    # Stop timer
                    stop_linear_dict = time.time()

                    # Print output
                    print("Linear Search starting...")
                    print(f"{word_select_linear} was found at index: {word_search_linear}\ntime taken to find word: {stop_linear_dict - start_linear_dict}")

            case "2":
                word_select_binary = input("Input a desired word: ")

                # Start timer
                start_binary_dict = time.time()
                word_search_binary = functions.binarySearch(dictionary, word_select_binary)

                # Check if word is in dictionary
                if word_search_binary == -1:
                    print(str(word_select_binary) + "was not found")

                else:
                    # Stop timer
                    stop_binary_dict = time.time()

                    # Print output
                    print("Binary Seach starting...")
                    print(f"{word_select_binary} was found at index: {word_search_binary}\ntime taken to find word: {stop_binary_dict - start_binary_dict}")

            case "3":
                counter = 0
                
                for i in aliceWords:
                    output = functions.linearSearch(dictionary, i)
                    if output == -1: 
                        
                    else: 
                        counter = counter + 1
                
                print(counter)
                

            case "4":
                print("4")
            case "5":
                print("Program Terminated")
                loop = False
            case other: 
                print("Invalid Entry") 

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

