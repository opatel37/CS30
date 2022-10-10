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
                # Local Variable(s)
                word_select_linear = input("Input a desired word: ").lower()
                
                # Start timer
                start_linear_dict = time.time()

                # Do Search
                word_search_linear = functions.linearSearch(dictionary, word_select_linear)
                
                # Stop timer
                stop_linear_dict = time.time()

                # Check if word is in dictionary
                functions.check_and_output(word_select_linear, word_search_linear, start_linear_dict, stop_linear_dict)

            case "2":
                word_select_binary = input("Input a desired word: ")

                # Start timer
                start_binary_dict = time.time()
                
                # Do Search
                word_search_binary = functions.binarySearch(dictionary, word_select_binary)

                # Stop timer
                stop_binary_dict = time.time()

                # Check if word is in dictionary
                functions.check_and_output(word_select_binary, word_search_binary, start_binary_dict, stop_binary_dict)

            case "3":
                counter_linear = 0

                print("Linear Search Starting...")   

                # Start timer
                start_linear_alice = time.time()
                
                # Do Search
                for i in aliceWords:
                    output = functions.linearSearch(dictionary, i.lower())
                    if output == -1: 
                        counter_linear = counter_linear + 1
                
                # Stop timer
                stop_linear_alice = time.time()

                # Print out results
                functions.print_alice_out(counter_linear, start_linear_alice, stop_linear_alice)

            case "4":
                counter_binary = 0

                print("Binary Search Starting...")

                # Start timer
                start_binary_alice = time.time()
                
                # Do Search
                for i in aliceWords:
                    output = functions.binarySearch(dictionary, i.lower())
                    if output == -1:
                        counter_binary = counter_binary + 1
                
                # Stop timer
                stop_binary_alice = time.time()

                # Print out results
                functions.print_alice_out(counter_binary, start_binary_alice, stop_binary_alice)

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

