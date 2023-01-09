# Global Variable(s)
import random

# Generate Init Grades
def generate_grades():
    # Local Variable(s)
    temp = []
    i = 0

    # Loop 35 times
    while i < 35:
        temp.append(random.randrange(0, 101))
        i += 1

    # Display temp
    return temp


def print_grades(array):
    for item in array:
        print(str(item) + " %")