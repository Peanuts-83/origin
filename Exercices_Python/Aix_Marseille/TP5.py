""" Exercice 1. Écrivez une classe Domino pour représenter une pièce de domino. Les objet sont
initialisés avec les valeurs des deux faces, A et B. Ajoutez une méthode .affiche_points() qui
affiche les valeurs des deux faces, et une méthode .totale() qui retourne la somme de deux
valeurs."""

class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"face A: {self.a}, face B: {self.b}"

    def affiche_points(self):
        return self

    def totale(self):
        return self.a + self.b

print("1.")
d = Domino(5, 3)
print('d = Domino(5, 3)')
print(d.affiche_points())
print('total:',d.totale())

""" Exercice 2. Écrivez une classe CompteBancaire. Les objets sont initialisés avec le nom du titulaire et le solde. 
L’argument solde doit être facultatif et avoir une valeur prédéfinie zéro. Ajoutez
deux méthodes .depot(somme) et .retrait(somme) pour changer le solde. Ajoutez une méthode
.affiche() qui montre le solde courant. """

class CompteBancaire:
    def __init__(self, name, solde = 0):
        self.name = name
        self.solde = solde

    def depot(self, somme):
        self.solde += somme
        return f"solde: {self.solde}"

    def retrait(self, somme):
        self.solde -= somme
        return f"solde: {self.solde}"

    def affiche(self):
        return f"Le solde du compte de {self.name} est de {self.solde} euros."


print('\n2.')
cpt = CompteBancaire('Tom', 1500)
print("cpt = CompteBancaire('Tom', 1500)")
print('depot(500):', cpt.depot(500))
print('retrait(800):', cpt.retrait(800))
print(cpt.affiche())
cpt2 = CompteBancaire('Isa')
cpt2.depot(200)
print(cpt2.affiche())

""" Exercice 3. Generateurs. Écrivez une classe TableMultiplication qui crée des objets initialisés
avec un nombre entier. Ajouter une méthode .prochain() qui renvoie à chaque appel un nouveau
terme de la table de multiplication correspondante."""

class TableMultiplication:
    VAL = [x for x in range(11)]

    def __init__(self, num):
        self.num = num
        self.index = 0

    def prochain(self):
        self.index += 1
        return self.VAL[self.index] * self.num
    
print('\n3.')
tab = TableMultiplication(3)
print("1 x", tab.num, '=', tab.prochain())
print("2 x", tab.num, '=', tab.prochain())
print("3 x", tab.num, '=', tab.prochain())

""" Exercice 4. Écrivez une classe Fraction qui crée des objets initialisés avec deux nombres entiers
.num et .denom pour le numérateur et le dénominateur. Ajoutez une méthode .affiche() qui
affiche une représentation de la fraction. Ajoutez des méthodes spéciales pour pouvoir utiliser les
opérateurs +, -, *, /.
Pour réduire la fraction, vous pouvez employer la fonction math.gcd(a, b) du module math, qui
calcule le plus grand commun diviseur entre deux entiers a et b."""
from math import gcd    # reduction de fraction, PlusGrandDiviseurCommun
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def affiche(self):
        return f"{self.num}/{self.denom}"

    def __repr__(self):
        if self.denom > 1:
            return f"{self.num}/{self.denom}"
        else:
            return f"{self.num}"

    def __add__(self, f2):
        f1 = Fraction(self.num, self.denom)
        f1.num = self.num
        f1.denom = self.denom
        if isinstance(f2, int):
            f2 = Fraction(f2,1)
        if f1.denom == f2.denom:
            f1.num += f2.num
            G = gcd(f1.num, f1.denom)
            if G > 1:
                f1.num //= G; f1.denom //=G
            return f1
        else:
            f1.num = f1.num*f2.denom + f2.num*f1.denom
            f1.denom = f1.denom*f2.denom
            G = gcd(f1.num, f1.denom)
            if G > 1:
                f1.num //= G; f1.denom //=G
            return f1

    def __mul__(self, f2):
        f1 = Fraction(self.num, self.denom)
        f1.num = self.num
        f1.denom = self.denom
        if isinstance(f2, int):
            f2 = Fraction(f2,1)
        f1.num *= f2.num
        f1.denom *= f2.denom
        G = gcd(f1.num, f1.denom)
        if G > 1:
            f1.num //= G; f1.denom //=G
        return f1

    def __sub__(self, f2):
        f1 = Fraction(self.num, self.denom)
        f1.num = self.num
        f1.denom = self.denom
        if isinstance(f2, int):
            f2 = Fraction(f2,1)
        if f1.denom == f2.denom:
            f1.num -= f2.num
            G = gcd(f1.num, f1.denom)
            if G > 1:
                f1.num //= G; f1.denom //=G
            return f1
        else:
            f1.num = f1.num*f2.denom - f2.num*f1.denom
            f1.denom = f1.denom*f2.denom
            G = gcd(f1.num, f1.denom)
            if G > 1:
                f1.num //= G; f1.denom //=G
            return f1

    def __truediv__(self, f2):
        f1 = Fraction(self.num, self.denom)
        f1.num = self.num
        f1.denom = self.denom
        if isinstance(f2, int):
            f2 = Fraction(f2,1)
        f1.num *= f2.denom
        f1.denom *= f2.num
        G = gcd(f1.num, f1.denom)
        if G > 1:
            f1.num //= G; f1.denom //=G
        return f1



print('\n4.')
f1 = Fraction(3, 2); f2 = Fraction(1, 5); f3 = 8
print('a.affiche()', f1.affiche(), f2.affiche(), 'f3=', f3)
print('f1+f2:', f1 + f2, end ='  ')
print('f1+f3:', f1 + f3)
print('f1*f2:', f1*f2, end='   ')
print('f1*f3:', f1*f3)
print('f1-f2:', f1-f2, end='   ')
print('f1-f3:', f1-f3)
print('f1/f2:', f1/f2, end='   ')
print('f1/f3:', f1/f3)

""" Exercice 6. On se propose de représenter les polynômes en une indéterminée avec un nombre
quelconque de termes :
c0 + c1 × x + c2 × x**2 + · · · + cn × x**n

. Écrivez une classe Poly qui crée des objets initialisés avec un nombre arbitraire d’arguments
(qui représentent les coefficients) et les stocke dans une liste .coeff. Par exemple, on représentera
le polynôme p(x) = 3 + 4x − 2x**2 avec :
>>> p = Poly(3, 4, -2)
et on récupérera ses coefficients avec :
>>> p.coeff
[3, 4, -2] 
. Ajoutez une méthode .evalue(x) qui renvoie la valeur du polynôme évalué à x. Par exemple,
pour calculer p(2) = 3 + 4 × 2 − 2 × 2
2 = 3 :
>>> p.evalue(2)
3
Essayez d’utiliser la fonction enumerate() pour itérer à la fois sur les coefficients et les exposants.
. Bonus. Ajoutez des méthodes spéciales pour les opérateur + et *, qui devront calculer respectivement la somme 
et le produit de deux polynômes. Par exemple, si p1(x) = 1 + 4x et p2(x) = 3 − 3x + 2x**2 on aura:
p3(x) = p1(x) + p2(x) = 4 + x + 2x**2
p4(x) = p1(x) ∗ p2(x) = 3 + 9x − 10x**2 + 8x**3
"""

from itertools import zip_longest, combinations
from math import prod

class Poly:

    def __init__(self, *args):
        self.args = args
        self.coeff = [ self.args[i] for i in range(0, len(self.args)) ]

    def evalue(self, x):
        # return sum([(self.args[i] * pow(x, i)) if i>0 else self.args[i] for i in range(0, len(self.args))])
        return sum([val * pow(x, i) if i>0 else val for i, val in enumerate(self.args)])

    def __add__(self, p2):
        p1 = Poly()
        p1.args = self.args
        p3 = list(zip_longest(p1.args, p2.args, fillvalue=0))
        return [sum(x) for x in p3]

    def __mul__(self, p2):
        p1 = Poly()
        p1.args = self.args
        p3 = [x*y for x in p1.args for y in p2.args]
        p4 = []; n_store = []
        for n in range(0, len(p3)):
            if 0<n<len(p3)-1:
                if n not in n_store:
                    p4.append((p3[n] + p3[n+2]))
                    n_store.append(n); n_store.append(n+2)
            else:
                p4.append(p3[n])
        return p4




print('\n6.', "p1 = Poly(3,4,-2)")
p1 = Poly(3,4,-2)
print("p1.coeff:", p1.coeff)
print("p1.evalue(2):", p1.evalue(2))
p1 = Poly(1, 4); p2 = Poly(3, -3, 2)
print("p1 = Poly(1, 4); p2 = Poly(3, -3, 2)")
p3 = p1 + p2
print('p1+p2:',p3)
p4 = p1 * p2
print('p1*p2:',p4)
