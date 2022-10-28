nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]
 

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




print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))
