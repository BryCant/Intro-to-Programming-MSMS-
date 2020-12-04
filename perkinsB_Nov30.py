# Bryant Perkins
# Introduction to Computer Programming
# Date: 30 Nov 2020
from Cards import Cards

# build a class that forms a regular pentagon based on a side length.
# have a function that returns the area of the pentagon. Have another function that
# overloads the len operator to return the perimeter of the pentagon

import math


class Pentagon:
    def __init__(self, side_len):
        self.side_len = side_len

    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_len ** 2

    def __len__(self):
        return self.side_len * 5


big_pentagon = Pentagon(35489654)
print(len(big_pentagon))
