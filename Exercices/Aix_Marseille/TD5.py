"""Exercice 1. Écrivez une classe Rocket pour représenter une fusée dans un jeu. Les objets créés
par la classe sont initialisés avec deux nombres .x et .y pour la position, et un nombre .dir pour
la direction (par exemple en degrés).
. Ajoutez une méthode .move(size) qui déplace la fusée de size unités dans sa direction courante
"""
from math import asin, acos, cos, sin
class Rocket:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def move(self, size):
        self.x = cos(self.dir)*size
        self.y = sin(self.dir)*size
        return self.x, self.y

    def __repr__(self):
        return f"Rocket position is {self.x}, {self.y}, it's angle is {self.dir}"
        
    def __str__(self):
        return f"Rocket position is {self.x}, {self.y}, it's angle is {self.dir}"

r = Rocket(0, 0, 35)
print('1 x et y:', r.x, r.y)
print(r.move(2))
print(r,'\n')

""" Exercice 2. Jeu de cartes Bataille, version OO.
. Écrivez une classe Carte qui crée des objets avec deux attributs .couleur et .valeur, initialisés
avec la couleur et la valeur de la carte. Ajoutez une méthode .str_carte() qui retourne une chaîne
avec la représentation de la carte en toutes lettres.
>>> c = Carte(’Pique’, 7)
>>> c.str_carte()
’Sept de Pique’
Ajoutez les méthodes spéciales __gt__() et __lt__() pour comparer les cartes selon leur valeur.
>>> d = Carte(’Trèfle’, 10)
>>> c < d
True
"""
class Carte:
    COULEUR = ('Pique', 'Coeur', 'Carreau', 'Trefle')
    VALEUR = { 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',
    7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',
    11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As' }

    def __init__(self, coul, val):
        try:
            if coul not in self.COULEUR:
                raise ValueError
            else:
                self.coul = coul
        except ValueError:
            print('Couleur non valide.')
        try:
            if val not in self.VALEUR:
                raise ValueError
            else:
                self.val = val
        except ValueError:
            print('Valeur non valide.')

    def __repr__(self):
        return f"({self.val}, {self.coul}"

    def str_carte(self):
        return f'{self.val} de {self.coul}'

    def __gt__(self, carte2):
        if self.val > carte2.val:
            return True
        else:
            return False

    def __lt__(self, carte2):
        if self.val < carte2.val:
            return True
        else:
            return False

# print('2.')
# c = Carte('Pique', 3); d = Carte('Trefle', 10)
# print(c.str_carte(), d.str_carte(), type(c))
# print('c<d:',c<d, 'c>d:', c>d)

""" . Écrivez une classe Jeu pour modéliser un jeu traditionnel de cinquante-deux cartes. Les objets
sont initialisés avec une liste .cartes de toutes les cartes. Ajoutez une méthode .melange() qui
mélange le jeu aléatoirement et une méthode .tire() qui renvoie la première carte du jeu (et
l’enlève de la liste).
. Écrivez une classe Joueur qui crée des objets avec deux attributs .jeu (initialisé avec un jeu de
cartes mélangé) et .points (initialisé à zero)."""
from random import shuffle
class Jeu:

    def __init__(self, *jeu_entier):
        self.jeu_entier = [Carte(couleur, valeur) for couleur in Carte.COULEUR for valeur in Carte.VALEUR.keys()]

    def __repr__(self):
        return f'{[x.str_carte() for x in self.jeu_entier]}'

    def melange(self):
        shuffle(self.jeu_entier)

    def tire(self):
        return self.jeu_entier.pop(0)

# jeu = Jeu()
# print('\n3. jeu:\n', jeu)
# jeu.melange(); c = jeu.tire()
# print(type(c))

class Joueur(Jeu,Carte):

    def __init__(self, name, points=0):
        self.jeu = Jeu()
        self.jeu.melange()
        self.points = points
        self.name = name
        
    def __repr__(self):
        return f"{self.name} va jouer la carte {self.jeu.jeu_entier[0].str_carte()}, il a {self.points} points."

# j1 = Joueur()
# print('\n', j1.jeu,'\n points:', j1.points)
# c = j1.jeu.tire()
# print(c.str_carte(), type(c))
# print(j1)

""". Réécrivez le programme qui simule le jeu Bataille en utilisant les classes ainsi définies.
. Écrivez des méthodes spéciales .__repr__() adaptées pour toutes les classes précédentes.
"""
j1 = Joueur('Bob'); j2 = Joueur('Morane')
print(f"Présentation des joueurs:\n {j1.name:^55}  {j2.name:^45}")
points_temp = 0
for _ in range(51):
    main_j1, main_j2 = j1.jeu.tire(), j2.jeu.tire()
    if main_j1 > main_j2:
        gagnant = j1.name
        j1.points += 1 + points_temp
        points_temp = 0
    elif main_j2 > main_j1:
        gagnant = j2.name
        j2.points += 1 +points_temp
        points_temp = 0
    else:
        gagnant = 'BATAILLE!'
        points_temp += 1

    print(f"{f'{j1}':>55}   {f'{j2}':<20}")
    if gagnant != 'BATAILLE!':
        print(f"{f'Gagnant: {gagnant}':^115}")
    else:
        print(f"{gagnant:^115}")

if j1.points > j2.points:
    vainqueur = j1.name, j1.points, j2.points
elif j2.points > j1.points:
    vainqueur = j2.name, j2.points, j1.points
print(f"\nLe vainqueur est {vainqueur[0]} avec {vainqueur[1]} points contre {vainqueur[2]}.")
