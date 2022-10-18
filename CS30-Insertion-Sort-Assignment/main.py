nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def insertionSort(anArray):
    for i in range(1, len(anArray) -1):
        ins_value = anArray[i]
        ins_position = i

    while ins_position > 0 and ins_value > anArray[ins_position -1]:
        