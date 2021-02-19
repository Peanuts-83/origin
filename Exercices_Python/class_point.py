import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x1 = x
        self.y1 = y

    def getx(self):
        print(self.x1)

    def gety(self):
        print(self.y1)

    def distance_from_xy(self, x, y):
        self.x2 = x; self.y2 = y
        d1 = self.x1 - self.x2
        d2 = self.y1 - self.y2
        distance = math.sqrt(d1**2 + d2**2)
        return distance

    def distance_from_point(self, point):
        self.x2, self.y2 = point.x1, point.y1
        d1 = self.x1 - self.x2
        d2 = self.y1 - self.y2
        distance = math.sqrt(d1**2 + d2**2)
        return distance


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
