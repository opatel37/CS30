import json

# Functions

def read_file():
    file = open("trade-data-set.txt", "r")
    info = json.load(file)
    file.close()
    return info

def save_contacts(selected_file):
    file = open('trade-data-set.txt', 'w')
    json.dump(selected_file, file)
    file.close()