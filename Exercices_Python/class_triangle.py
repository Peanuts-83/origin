import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    """def getx(self):
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
        return distance"""


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v1 = vertice1
        self.__v2 = vertice2
        self.__v3 = vertice3

    def perimeter(self):
        side = (self.__v1, self.__v2, self.__v3, self.__v1)
        dist = 0
        for i in range(3):
            x = side[i]._Point__x - side[i+1]._Point__x
            y = side[i]._Point__y - side[i+1]._Point__y
            distance = math.sqrt(x**2+y**2)
            dist += distance
        return dist


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
