nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]
 
def selectionSort(anArray):
    for fill_slot in range(0, len(anArray) -2, 1):
        min_position = fill_slot
        for post_fill in range(anArray[fill_slot] +1, len(anArray) -2, 1):
            if post_fill < anArray[min_position]:
                min_position = post_fill

            list[min_position], list[fill_slot] = list[fill_slot], list[min_position]