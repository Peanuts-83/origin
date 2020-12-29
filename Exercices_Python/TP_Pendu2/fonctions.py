
import os # On importe le module os
from pathlib import Path
import pickle
from random import choice

from donnees import *

"""
fonctions nécessaires au fonctionnement du jeu de pendu.
"""

# # récupération scores de la partie
def recuperer_scores():
    chemin_scores = Path(NOM_FICHIER_SCORES)
    if chemin_scores.exists():
        with open(chemin_scores,'rb') as fichier_scores:
            mon_depickler = pickle.Unpickler(fichier_scores)
            scores = mon_depickler.load()
    else:
        scores = {}
    return scores

def enregistrer_scores(scores):
    chemin_scores = Path(NOM_FICHIER_SCORES)
    with open(chemin_scores,'wb') as fichier_scores:
        mon_pickler = pickle.Pickler(fichier_scores)
        mon_pickler.dump(scores)

# # récupération nom utilisateur
def recuperer_nom():
    print(''.center(50,'*'))
    nom = input("Bonjour, merci d'indiquer votre nom :")
    if len(nom) > 2 or not nom.isalnum():
        return nom
    else:
        return recuperer_nom()

def recuperer_lettre():
    lettre = input('Entrer une lettre :')   # demande une lettre à user
    if len(lettre) > 1 or not lettre.isalpha():
        print('lettre non valide.')
        return recuperer_lettre()
    else:
        return lettre

def choix_mot():
    mot = choice(LISTE_MOTS)
    return mot

def eval_lettre(lettres_trouves,mot):
    mot_trouve = ''
    for i in mot:
        if i in lettres_trouves:
            mot_trouve += i
        else:
            mot_trouve += '*'
    print(mot_trouve)
    return mot_trouve





# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
# os.system("pause")
