import time

# Function(s)
def linearSearch(anArray, item):
    for i in range(0, len(anArray)):
        if anArray[i] == item:
            return i
        
    return -1

def binarySearch(anArray, item):
    # Initialize lower and upper indices
    lower_index = 0
    upper_index = len(anArray) - 1

    while lower_index <= upper_index:
        # Initialize middle index
        middle_index = (lower_index + upper_index) // 2

        # Check if item value equals middle index value
        if (anArray[middle_index] == item):
            return middle_index
        elif (item < anArray[middle_index]):
            upper_index = middle_index - 1
        elif (item > anArray[middle_index]):
            lower_index = middle_index + 1

    # If item is not found
    return -1

def word_search(search_txt, algo_type):
    # Get input
    inputed_word = input("Input a desired word: ").lower()
    
    # Start timer
    start_search = time.time()

    # Do Search
    word_search = algo_type(search_txt, inputed_word)
    
    # Stop timer
    stop_search = time.time()

    # Check if word is in dictionary
    if word_search == -1:
        print(str(inputed_word) + "was not found" )
    else:
        # Output results
        print(
            f'''
Linear Search starting...
{inputed_word} was found at index: {word_search}
\nTime taken to find word: {stop_search - start_search}
            '''
        )

def alice_spell_check(search_txt, check_txt, algo_type):
    # Init word counter
    word_counter = 0

    # Start timer
    start_alice = time.time()
    
    # Do spell check
    for i in search_txt:
        output = algo_type(check_txt, i.lower())
        if output == -1:
            word_counter += 1
    
    # Stop timer
    stop_alice = time.time()

    # Output results
    print(
    f'''
Number of words not found in dictionary: {word_counter}
\nTime taken to complete search: {stop_alice - start_alice}
    '''
    )