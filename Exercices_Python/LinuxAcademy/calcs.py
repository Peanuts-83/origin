import math

def circle_circumference(radius):
    base = 2*math.pi*radius
    return math.ceil(base*100)/100


def circle_area(radius):
    base = math.pi*math.pow(radius, 2)
    return math.ceil(base*100)/100
