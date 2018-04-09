# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program show how Python allows multiple items
#               to be returned from a function call.
#
# ===============================================================
import random as random

def getThreeInputs(prompt):
    val1 = input(prompt)
    val2 = input(prompt)
    val3 = input(prompt)
    return val1, val2, val3


def getRandomNumbers():
    val1 = random.random()          # Random float x, 0.0 <= x < 1.0
    val2 = random.uniform(1, 10)    # Random float x, 1.0 <= x < 10.0
    val3 = random.randint(1, 10)    # Integer from 1 to 10, endpoints included
    val4 = random.randrange(0, 101, 2)  # Even integer from 0 to 100
    val5 = random.choice('abcdefghijklmopqrstuvwxyz')  # Choose a random element
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(items)           # reorders list
    val6 = items
    val7 = random.sample(items, 3)  # choose 3 elements

    return val1, val2, val3, val4, val5, val6, val7


r1, r2, r3, r4, r5, r6, r7 = getRandomNumbers()
print()
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r7:", r7)


print()
v1, v2, v3 = getThreeInputs("Enter a value: ")
print("value 1:", v1, "value 2:", v2, "value 3:", v3)
