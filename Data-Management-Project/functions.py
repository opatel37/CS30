import json

# Functions

def read_file(file_name):
    file = open(file_name, 'r')
    info = json.load(file)
    file.close()
    return info

def save_file(selected_file):
    file = open('trade-data-set.txt', 'w')
    json.dump(selected_file, file)
    file.close()

def selectionSort(anArray):
    for fill_slot in range(0, len(anArray) -1):
        min_position = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if anArray[post_fill] < anArray[min_position]:
                min_position = post_fill

        anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]