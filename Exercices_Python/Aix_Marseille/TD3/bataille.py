""" Exercice 2. Programme principal bataille.py.
Le programme utilise le module cartes pour simuler une partie du jeu bataille entre deux joueurs.
. Créez deux jeux de cartes jeu1 et jeu2 et mélangez-les aléatoirement.
"""

import os; #print(os.getcwd())
from cartes import *
import random

jeu1 = jeu_de_cartes(); jeu2 = jeu_de_cartes()
random.shuffle(jeu1); random.shuffle(jeu2)
print('jeu1:', jeu1, '\n\njeu2:', jeu2)

""" 
. Ensuite, tirez la première carte de chaque jeu et comparez les deux valeurs. Le joueur avec la
carte la plus haute gagne un point. Continuez jusqu’à la fin des jeux. Pour chaque manche, affichez
en toutes lettres les cartes tirées et le gagnant.
. Affichez les points de chaque joueur et le gagnant de la partie."""
points1 = 0; points2= 0; points_temp = 0
while len(jeu1) > 0:
    main1, main2 = jeu1.pop(0), jeu2.pop(0)
    m1 = ''.join([str(k) for k, val in VALEUR.items() if val == main1.split()[0]])
    m2 = ''.join([str(k) for k, val in VALEUR.items() if val == main2.split()[0]])
    
    if VALEUR[int(m1)] > VALEUR[int(m2)]:
        gagnant = 'Joueur 1'
        points1 += 1 + points_temp
        points_temp = 0
    elif VALEUR[int(m1)] < VALEUR[int(m2)]:
        gagnant = 'Joueur 2'
        points2 += 1 + points_temp
        points_temp = 0
    else:
        gagnant = 'BATAILLE!'
        points_temp += 1
    
    print(f"{f'Main joueur 1: {main1}':<40} {f'Main joueur 2: {main2}':<40} Gagnant: {gagnant}")
    gagnant = ''
if points1 > points2:
    print(f"Le joueur 1 a gagné avec {points1} points contre {points2}.")
elif points2 > points1:
    print(f'Le joueur 2 a gagné avec {points2} points contre {points1}.')
else:
    print("Egalité!")

    