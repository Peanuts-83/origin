class Rect:
    def __init__(self, lon, lar):
        self.lon = lon
        self.lar = lar
        if lar > lon:
            self.lon, self.lar = self.lar, self.lon

    def __repr__(self):
        return f"La largeur du rectangle est de {self.lar} cm  et sa longueur de {self.lon} cm."

    def perim(self):
        return f"Périmètre: {self.lon*2 + self.lar*2} cm."

    @property
    def surf(self):
        return self.lon*self.lar

    @surf.getter
    def surf(self):
        return f"La surface du rectangle est de {self.lon*self.lar} cm."

    @surf.setter
    def surf(self, lon_lar):
        self.lon, self.lar = lon_lar
        if self.lar > self.lon:
            self.lon, self.lar = self.lar, self.lon

class Parall(Rect):
    def __init__(self, lon, lar, hau):
        super().__init__(lon, lar)
        self.hau = hau

    def __repr__(self):
        print(f"La hauteur du parallélépipède est de {self.hau} cm.")
        return f"La largeur du parallélépipède est de {self.lar} cm  et sa longueur de {self.lon} cm."

    def vol(self):
        return f"Volume: {self.lon*self.lar*self.hau} cm3."

###
# test class Rect:
a = Rect(3,8)
print(a)
print(a.perim())
print(a.surf)
a.surf = 2,5
print(a.surf)
print(a)

# test class Parall:
b = Parall(3,5,8)
print(b.vol())
print(b)