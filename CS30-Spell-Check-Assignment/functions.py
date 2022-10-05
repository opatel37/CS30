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
