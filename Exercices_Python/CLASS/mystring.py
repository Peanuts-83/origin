class myString:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f'{self.string}'
    
    def append(self, second):
        self.string += " " + second.__repr__()
        return f"Methode append: {self.string}"

    def pop(self, num):
        return f"Methode pop: { self.string[:num]}{self.string[num+1:]}, index n°{num}: {self.string[num]}."

###
s1 = myString('Hello')
s2 = myString('World')
print('s1=',s1,'s2=',s2)
print(s1.append(s2))
print(s2.pop(2))

