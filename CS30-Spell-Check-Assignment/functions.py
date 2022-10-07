# Function(s)
def linearSearch(anArray, item):
    for i in anArray:
        if i == item:
            return anArray.index(item)
        
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

def check_and_output(select_type, search_type, time_start, time_stop):
        # Check if word is in dictionary
    if search_type == -1:
        print(str(select_type) + "was not found" )
    else:
        # Print output
        print(
            f'''
Linear Search starting...
{select_type} was found at index: {search_type}
\nTime taken to find word: {time_stop - time_start}
            '''
        )

def print_alice_out(word_counter, time_start, time_stop): 