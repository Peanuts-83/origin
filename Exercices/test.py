class Numbers:
    MULTIPLIER = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return a * self.MULTIPLIER

    def  substract(self, b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, x,y):
        self.x, self.y = x,y

    @value.deleter
    def value(self):
        del self.x
        del self.y

