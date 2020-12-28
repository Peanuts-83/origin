class Calcul:
    FACT = 1

    def factorielle(self, num):
        for n in range(1,num+1):
            self.FACT *= n
        return self.FACT

    def somme(self, num):
        val = 0
        for n in range(num+1):
            val += n
        return val

    def prim(self, num):
        for n in range(2, num):
            if num%n == 0:
                return False
        return True 

    def testprim(self, num):
        for n in range(2, num):
            if num%n == 0:
                return f"{num} n'est pas premier."
        return f"{num} est premier."

    def testprims(self, a, b):
        for n in range(2, max(a, b)+1):
            if a%n == 0 and b%n == 0:
                return f"{a} et {b} ne sont pas premiers entre eux."
        return f"{a} et {b} sont premiers entre eux."

    def tableMulti(self, num):
        print(f"Table de {num}:")
        for n in range(1, 11):
            print(f"{num} x {n} = {num*n}")

    @staticmethod
    def listDiv(num):
        Ldiv = [n for n in range(1, num+1) if num%n == 0]
        return f"Ldiv = {Ldiv}"


    def listDivPrim(self, num):
        LdivPrim = [n for n in range(1, num+1) if num%n == 0 and self.prim(n) == True]
        return f"LdivPrim = {LdivPrim}"


###
a = Calcul()
print(a.factorielle(5))
print(a.somme(5))
print(a.testprim(7))
print(a.testprim(12))
print(a.testprims(2,5))
print(a.testprims(3,9))
print(a.tableMulti(3))
print(a.listDiv(155))
print(a.listDivPrim(155))