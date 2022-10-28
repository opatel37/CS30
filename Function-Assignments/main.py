# Python Functions Assignment

# Global Variables
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# CONTAINS 

def contains(list, item):
    # Loop through list and search for item
    if item in list:
        return True
    else: 
        return False

# TEST FUNCTION
if contains(test, 5):
    print("5 is in the list")
else:
    print("5 is not in the list")
    
if contains(test, "a"):
    print("a is in the list")
else:
    print("a is not in the list")



# INDEXOF

def indexOf(list, item):
    # Loop through list and search for the first occurrence of the item
    for index, x in enumerate(list):
        if x == item:
            # Return index of desired item
            return index

    # Return if item not found
    return -1
                
# TEST FUNCTION
indexT = indexOf(test, 3)

if indexT != -1:
    print(f"3 is in the list at {indexT}")
else: 
    print('3 is not in the list')

indexF = indexOf(test, "b")

if indexF != -1:
    print(f"b is in the list at {indexF}")
else: 
    print("b is not in the list")



# REVERSE
def reverse(list):
    # Creat reversed list
    new_list = []

    # Loop through list with reverse index
    for i in range(len(list) - 1, -1, -1):
        new_list.append(list[i])

    # Return reversed list
    return new_list

# TEST FUNCTION
revered_list = reverse(test)
print(revered_list)



# SWAP
def swap(list, idx1, idx2):

    list[idx1], list[idx2] = list[idx2], list[idx1]

    # Return list with swapped items
    return list

# TEST FUNCTION
swapped_list = swap(test, 3, 7)
print(swapped_list)



# INDEXOFMIN
def indexOfMin(list):
    # Set first item to smallest
    min_num = list[0]
    min_num_idx = 0

    # Loop through and check for min value
    for index, x in enumerate(list):
        if x < min_num:
            min_num = x
            min_num_idx = index
    
    # Return minimum value
    return min_num_idx

# TEST FUNCTION
min_value = indexOfMin(test)
print(min_value)
