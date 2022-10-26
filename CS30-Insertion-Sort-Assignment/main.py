nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def insertionSort(anArray):
    for i in range(1, len(anArray)):
        ins_val = anArray[i]
        test_pos = i

        while test_pos > 0 and anArray[test_pos -1] > ins_val:
            anArray[test_pos] = anArray[test_pos -1]
            test_pos -= 1
        
        anArray[test_pos] = ins_val

insertionSort(nums)
insertionSort(words)

print(nums)
print(words)



# ins_val = 40
# test_pos = 4

# 4 > 0
# 40 < 100

# anArray[test_pos] (40) = anArray[test_pos -1] (100)
# [10, 70, 30, 100, 100, 45, 90, 80, 85]

# test_pos = 3

# 3 > 0
# 30 > 40 (terminates while loop)

# anArray[test_pos -1] (100) = ins_val (what's been saved as 40)