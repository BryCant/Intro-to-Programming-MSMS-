import math


class Point:
    def __init__(self, **components):
        if components is not None:
            if "x" in components.keys():
                self.x = components["x"]
            else:
                self.x = 0
            if "y" in components.keys():
                self.y = components["y"]
            else:
                self.y = 0

    def distance(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))


point1 = Point(x=6)
point2 = Point(x=3)
print(point1.distance())
