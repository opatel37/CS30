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