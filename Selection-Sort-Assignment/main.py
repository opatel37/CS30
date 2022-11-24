nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]
 
def selectionSort(anArray):
    # Loop through array, stopping one before the last element
    for fill_slot in range(len(anArray)):
        # Create and set the fill slot(what might be swapped)
        min_position = fill_slot

        # Loop through values after the fill slot element
        for post_fill in range(fill_slot +1, len(anArray)):
            
            # Check if items after fill slot are smaller
            if anArray[post_fill] < anArray[min_position]:
                # If so, set min position to the new minimum value
                min_position = post_fill

        # Swap values at min position and fill slot (will only make a difference if you have set min position to new value[post_fill])
        anArray[min_position], anArray[fill_slot] = anArray[fill_slot], anArray[min_position]

# Sort array(s)
selectionSort(nums)
selectionSort(words)

# Print array(s)
print(nums)
print(words)