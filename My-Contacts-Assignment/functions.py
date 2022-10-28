import json

#  Function(s)

def read_info():
    file = open("./local.txt", "r")
    info = json.load(file)
    file.close()
    return info

def save_contacts(selected_file):
    file = open('./local.txt', 'w')
    json.dump(selected_file, file)
    file.close()

def search_con(list, name):
    # Check if contact exists 
    for item in read_info():
        if item["Name"] == name.capitalize():
            return list.index(item)

        
    # If not found 
    return -1

def print_names(file):
    for item in file:
        print('\nName: ' + item["Name"])