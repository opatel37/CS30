import json

# Functions

def read_info():
    file = open("./local.txt", "r")
    info = json.load(file)
    file.close()
    return info

def save_contacts(selected_file):
    file = open('./local.txt', 'w')
    json.dump(selected_file, file)
    file.close()