
import os # On importe le module os
from donnees import *
from fonctions import *

"""
jeu de pendu.
"""

# récupération scores de la partie
scores = recuperer_scores()

# récupération nom utilisateur
nom = recuperer_nom()
if nom in scores.keys():
    print(f'Bonjour {nom}, vous avez un score de {scores[nom]} points')

# si utilisateur n'a pas de score, on l'ajoute
if nom not in scores.keys():
    scores[nom] = 0


# variable qui indique la fin de partie
continuer_partie = 'o'

while continuer_partie != 'n':
    chances = NBR_CHANCES
    mot = choix_mot()
    lettres_trouves = set()         # lettres trouvées regroupées dans un ensemble
    lettre = recuperer_lettre()
    if lettre not in mot and lettre not in lettres_trouves:
        chances -= 1                        # -1 chance si lettre mauvaise
    print('chances-',chances)
    lettres_trouves.add(lettre)             # ajout de la lettre à l'ensemble
    mot_trouve = eval_lettre(lettres_trouves,mot)   # recherche lettre dans mot mystere
    while mot_trouve != mot and chances > 0 :
        lettre = input('Entrer une lettre :')   # continuer
        if lettre not in mot and lettre not in lettres_trouves:
            chances -= 1
        print('chances-',chances)
        lettres_trouves.add(lettre)
        mot_trouve = eval_lettre(lettres_trouves,mot)
    if mot_trouve == mot:                   # mot trouvé, gagné
        print('Gagne!')
        print(f'Vous avez gagné {chances} points.')
        scores[nom] += chances              # MAJ des scores
        enregistrer_scores(scores)
        continuer_partie = input('Voulez-vous continuer? (o/n)')    # rejouer?
        lettres_trouves = set()             # si oui, remise à 0 des variables
        mot_trouve = ''
        chances = NBR_CHANCES
    elif chances == 0:
        print('Perdu...')                   # perdu, ciao!
        continuer_partie = input('Voulez-vous recommencer? (o/n)')    # rejouer?
        lettres_trouves = set()             # si oui, remise à 0 des variables
        mot_trouve = ''
        chances = NBR_CHANCES

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
# os.system("pause")
