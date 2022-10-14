nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(anArray):

    for total_coms in range(len(anArray) -1, 0, -1):

        for cur_coms in range(total_coms):
            if anArray[cur_coms] > anArray[cur_coms +1]:
                anArray[cur_coms], anArray[cur_coms +1] = anArray[cur_coms +1], anArray[cur_coms]

bubbleSort(nums)
bubbleSort(words)

print(nums)
print(words)