"""Exercice 1. Module cartes.py.
Les couleur sont énumérées dans un tuple de chaînes. Pour les valeurs on se donne un dictionnaire
qui associe un nom à chaque valeur numérique :"""
COULEUR = ('Pique', 'Coeur', 'Carreau', 'Trèfle')
VALEUR = { 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',
7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',
11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As' }
"""
Chaque carte sera modélisée par un tuple (couleur, valeur) où couleur est un des élément de
COULEUR et valeur une des clés de VALEUR. Un jeu de cartes sera modélisé par une liste de cartes.
. Écrivez une fonction str_carte(carte) qui renvoie une chaîne contenant la représentation en
toutes lettres de la carte passé en argument."""
def str_carte(carte):
    coul, val = carte
    return f"{VALEUR[val]} de {COULEUR[COULEUR.index(coul)]}"

# c = str_carte(('Pique', 8))
# print(c)

""". Écrivez une fonction jeu_de_carte() qui crée un jeu de cartes traditionnel et renvoie l’objet
créé."""
def jeu_de_cartes():
    jeu_entier = []
    for coul in COULEUR:
        for val in VALEUR:
            jeu_entier.append(str_carte((coul, val)))
    return jeu_entier

# print(jeu_de_cartes())

