# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

def bubbleSort(anArray):
    for total_coms in range(len(anArray) -1, 0, -1):

        for cur_coms in range(total_coms):
            if anArray[cur_coms] > anArray[cur_coms +1]:
                anArray[cur_coms], anArray[cur_coms +1] = anArray[cur_coms +1], anArray[cur_coms]

def selectionSort(anArray):
    for fill_slot in range(0, len(anArray) -1):
        min_position = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if anArray[post_fill] < anArray[min_position]:
                min_position = post_fill

        anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]

def insertionSort(anArray):
    for i in range(1, len(anArray)):
        ins_val = anArray[i]
        test_pos = i

        while test_pos > 0 and anArray[test_pos -1] > ins_val:
            anArray[test_pos] = anArray[test_pos -1]
            test_pos -= 1
        
        anArray[test_pos] = ins_val

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def sort_function(algo_type, data_file):
    start_time = time.time()
    algo_type(data_file)
    end_time = time.time()
    return end_time - start_time

print("Bubble Sort")
print("Random Data Run: " + str(sort_function(bubbleSort, randomData.copy())))
print("Revered Data Run: " + str(sort_function(bubbleSort, reversedData.copy())))
print("Nearly Sorted Run: " + str(sort_function(bubbleSort, nearlySortedData.copy())))
print("Few Unique Run: " + str(sort_function(bubbleSort, fewUniqueData.copy())))

print("Selection Sort")
print("Random Data Run: " + str(sort_function(selectionSort, randomData.copy())))
print("Revered Data Run: " + str(sort_function(selectionSort, reversedData.copy())))
print("Nearly Sorted Run: " + str(sort_function(selectionSort, nearlySortedData.copy())))
print("Few Unique Run: " + str(sort_function(selectionSort, fewUniqueData.copy())))

print("Insertion Sort")
print("Random Data Run: " + str(sort_function(insertionSort, randomData.copy())))
print("Revered Data Run: " + str(sort_function(insertionSort, reversedData.copy())))
print("Nearly Sorted Run: " + str(sort_function(insertionSort, nearlySortedData.copy())))
print("Few Unique Run: " + str(sort_function(insertionSort, fewUniqueData.copy())))