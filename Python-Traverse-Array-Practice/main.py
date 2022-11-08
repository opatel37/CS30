# Question 1
results = ["Yes", "Maybe", "No", "Maybe", "Yes", "No", "No", "Maybe", "Yes", "No", "Maybe", "Maybe", "Yes", "No"]

yes_counter = 0
no_counter = 0
maybe_counter = 0

for i in range(0, len(results)): 
    if results[i].capitalize() == "Yes":
        yes_counter += 1
    elif results[i].capitalize() == "No":
        no_counter += 1
    elif results[i].capitalize() == "Maybe":
        maybe_counter += 1

print(
f'''
Num Yes: {yes_counter}
Num No: {no_counter}
Num Maybe: {maybe_counter}
'''
)



# Question 2
ages = [30, 2, 46, 6, 24, 19, 35, 12, 23, 56, 18, 3, 6, 7, 25] 

below_18 = 0
equal_or_above_18 = 0

for i in range(0, len(ages)):
    if ages[i] < 18:
        below_18 += 1
    else:
        equal_or_above_18 += 1

print(
f'''
<18: {below_18}
>=18: {equal_or_above_18}
'''
)



# Question 3
prices = [12, 124, 324, 56, 20, 34, 45, 76, 10, 234, 5, 123, 64, 23, 55, 33]

# Part A
under_20 = 0
from_20_to_49 = 0
equal_or_above_50 = 0

for i in range(0, len(prices)):
    if prices[i] < 20:
        under_20 += 1
    elif prices[i] >= 20 and prices[i] <= 49:
        from_20_to_49 += 1
    else:
        equal_or_above_50 += 1

print(
f'''
>20: {under_20}
20-49: {from_20_to_49}
>= 50: {equal_or_above_50}
'''
)

# Part B
prices_B = prices.copy()

for i in range(0, len(prices_B)):
    prices_B[i] += 2

print(prices_B)

# Part C
prices_C = prices.copy()

for i in range(0, len(prices_C)):
    prices_C[i] += prices_C[i] * 0.05

print(prices_C)

# Part D
prices_D = prices.copy()

for i in range(0, len(prices_D)):
    prices_D[i] -= prices_D[i] * 0.2

print(prices_D)