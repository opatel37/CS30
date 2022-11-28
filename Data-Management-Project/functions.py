import datetime
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

def selectionSort(anArray, sort_param):
    for fill_slot in range(len(anArray)):
        min_pos = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if anArray[post_fill][sort_param] < anArray[min_pos][sort_param]:
                min_pos = post_fill

        anArray[min_pos], anArray[fill_slot] = anArray[fill_slot], anArray[min_pos]

def compare_vals(anArray, post, min, sort):
    if anArray



# def convert_str_to_datetime(data):
#     for item in data:
#         date_val = item["Date"].split("/")
#         for i in range(0, len(date_val)):
#             date_val[i] = int(date_val[i])
            
#         date_item = str(datetime.date(date_val[2], date_val[1], date_val[0]))
#         item["Date"] = date_item

#     save_file(data)

