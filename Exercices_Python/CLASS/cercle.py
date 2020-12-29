from math import pi, sqrt
class Cercle:
    def __init__(self, O, r):
        self.O = O
        self.a, self.b = O
        self.r = r

    def __repr__(self):
        return f"Cercle de centre O(x={self.a}, y={self.b}) et de rayon {self.r} cm."

    def surf(self):
        return f"Surface: {round(pi*self.r**2, 2)} cm2."

    def perim(self):
        return f"Périmètre: {round(2*pi*self.r,2)} cm."

    def appartient(self, name, x, y):
        dist_to_O = sqrt((self.a - x)**2 + (self.b - y)**2)
        if dist_to_O < self.r:
            return f"{name}{x,y} est dans le cercle de centre O{self.O} et de rayon {self.r} cm."
        else:
            return f"{name}{x,y} est en dehors du cercle."


###
a = Cercle((3,5), 2.5)
print(a)
print(a.surf())
print(a.perim())
print(a.appartient('A',2,7))
print(a.appartient('B',0.5,5))