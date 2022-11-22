import csv

list = []

with open('./text.csv', 'r') as file:     

    for line in file:
        list.append(line.strip().split(','))


print(list)

def create_list_dict(list):
    # take list and convert into list of dict