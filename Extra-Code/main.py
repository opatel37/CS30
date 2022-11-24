import csv
import datetime

list = []

with open('./text.csv', 'r') as file:     

    for line in file:
        list.append(line.strip().split(','))



# def create_list_dict(list):
    # take list and convert into list of dict
present = datetime.datetime.now()
future = datetime.datetime(3000, 1, 1)

if present < future:
    print(str(future) + "!")