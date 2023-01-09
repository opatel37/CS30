# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)
counter_3 = 0
counter_4 = 0
counter_5 = 0

# Q1
for i in range(0, len(color_data)):
    print(color_data[i]["name"])
    print(color_data[i]["family"])
    print("")

# Q2
for i in range(0, len(color_data)):
    if color_data[i]["brightness"] >= 200:
        print(color_data[i]["name"])
        print(color_data[i]["family"])
        print("")

# Q3
for i in range(0, len(color_data)):
    if color_data[i]["family"] == "Red" or color_data[i]["family"] == "Pink":
        counter_3 += 1

# Q4
input_4 = input("Enter family of color: ")
for i in range(0, len(color_data)):
    if color_data[i]["family"] == input_4.capitalize():
        print(color_data[i]["name"])
        print(color_data[i]["family"])
        print("")
        counter_4 += 1

# Q5
input_5 = input("First letter of the desired color: ")
for i in range(0, len(color_data)):
    if color_data[i]["name"][0] == input_5.capitalize():
        print(color_data[i]["name"])
        print("")
        counter_5 += 1

print(counter_3)
print(counter_4)
print(counter_5)