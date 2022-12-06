import json

# Functions

def read_file(file_name):
    file = open(file_name, 'r')
    info = json.load(file)
    file.close()
    return info

def save_data(selected_data, save_to):
    file = open(save_to, 'w')
    json.dump(selected_data, file)
    file.close()

def selection_sort(anArray, sort_param, compare_funct):
    for fill_slot in range(len(anArray)):
        min_pos = fill_slot

        for post_fill in range(fill_slot +1, len(anArray)):
            
            if compare_funct(anArray[post_fill][sort_param], anArray[min_pos][sort_param]):
                min_pos = post_fill

        anArray[min_pos], anArray[fill_slot] = anArray[fill_slot], anArray[min_pos]

def sort_inc(val_1, val_2):
    if val_1 < val_2:
        return True

def sort_dec(val_1, val_2):
    if val_1 > val_2:
        return True

def search_data(list, key, val):
  for item in list:
      if item[key] == val:
          return list.index(item)

  return -1

def check_two_vals(list, username, password):
    for i in range(0, len(list)):
        