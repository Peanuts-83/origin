class Numbers:
    MULTIPLIER = 8

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a*cls.MULTIPLIER

    @staticmethod
    def substract(b, c):
        return (b-c)*Numbers.MULTIPLIER

    @property
    def value(self):
        try:
            return (self.x, self.y)
        except AttributeError:
            return 'No value for (x, y)'

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y

a= Numbers(5,3)
print('Values:',a.value)
print('Sum:',a.add())
print('Mult a by Multiplier:',a.multiply(2))
print('Subst b, c:',a.substract(9,4))
a.value = 8, 2
print('Values changed:',a.value)
del a.value
print('Values deleted:',a.value)