# def push(list1, value): return [value] + list1


# TEST STUFFS
'''
string1 = "Lawrence"
string2 = "William"
string3 = "Jeffrey"

for i in range(len(string2)):
    if string2[i] < string3[i]:
        print("True")

string4 = string1[:3] + string2[3:5] + string3[5:]
string5 = "William"
print(string5 == string2)
print("string5 is string2")
print(string4)

import math


def square_area(side):
    return side**2


def triangle_area(side):
    return math.sqrt(3)/4*side**2


def pentagon_area(side):
    return 0.25*math.sqrt(5*(5+2*math.sqrt(5)))*side**2


shapeChoice = input("Choose a shape:")
sizeChoice = int(input("Choose a size:"))

if shapeChoice.lower() == "square":
    print("Your square has an area of", round(square_area(sizeChoice), 2))
elif shapeChoice.lower() == "tri":
    print("Your triangle has an area of", round(triangle_area(sizeChoice), 2))
elif shapeChoice.lower() == "pentagon":
    print("Your pentagon has an area of", round(pentagon_area(sizeChoice), 2))
else:
    print("You did not enter a valid shape")

'''

count = 0

while count < 20:
    if count % 2 == 0:
        print("This is an even iteration")
    else:
        print("This is an odd iteration")

