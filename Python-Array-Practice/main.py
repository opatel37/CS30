import random

# 1
num_1 = ["January", "June", "July"]

# 2
num_2 = []
for n in range(700):
    num_2.append("joy")

# 3
num_3 = []
for n in range(500):
    num_3.append(7)

# 4
num_4 = []
for n in range(5000):
    num_4.append(random.randrange(0, 100))

# 5
num_5 = []
for n in range(300):
    num_5.append(random.randrange(0, 100))

# 6
num_6 = []
for n in range(20, 801, 4):
    num_6.append(n)

# 7
num_7 = []
for n in range(100, 9, -2):
    num_7.append(n)

# 8
num_8 = []
str_8 = "red,orange,yellow,green,blue,indigo,violet"
num_8 = str_8.split(",")

# 9
num_9 = []
str_9 = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
num_9 = str_9.split(";")

# 10
num_10 = []
loop = True
while loop:
    in_10 = input("Please enter a name to add or input 'done' to terminate: ")
    if in_10.capitalize() == "Done":
        loop = False
        print(num_10)
    else:
        num_10.append(in_10.capitalize())
    