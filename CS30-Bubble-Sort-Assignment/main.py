
nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]

def swap(list, idx1, idx2):

    list[idx1], list[idx2] = list[idx2], list[idx1]



def bubbleSort(anArray):

    for total_coms in range(len(anArray)-1, -1, -1):

        print(anArray[total_coms])

        # idx1 = 0
        # idx2 = idx1 + 1

        # for cur_coms in range(total_coms):
        #     if anArray[idx1] > anArray[idx2]:
        #         swap(anArray, idx1, idx2)

        #     idx1 += 1
        #     cur_coms -= 1


test1 = bubbleSort(nums)
test2 = bubbleSort(words)

print(test1)
print(test2)