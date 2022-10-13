# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re # Needed for splitting text with a regular expression
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
        num_select = input("Input number of desired option (1-5): ")

        # Process Input
        match num_select:
            case "1":
                functions.word_search(dictionary, functions.linearSearch)

            case "2":
                functions.word_search(dictionary, functions.binarySearch)

            case "3":
                print("Linear Search Starting...")   

                functions.alice_spell_check(aliceWords, dictionary, functions.linearSearch)

            case "4":
                print("Binary Search Starting...")

                functions.alice_spell_check(aliceWords, dictionary, functions.binarySearch)

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

