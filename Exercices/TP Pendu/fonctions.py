# -*-coding:latin-1 -*
import os # On importe le module os
from pathlib import Path
import pickle
from random import randint
from donnees import *

"""
Fonctions nécessaires au bon fonctionnement du jeu de pendu
"""

mot_choisi = ''     # mot qui sera à deviner
tentatives = 0
nom = ''
sc_nom = 0

# fonction contenant les noms des joueurs et leur scores
# vérifications de l'existence du tableau et création le cas échéant
def tableau_joueurs(nom_joueur):
    global nom
    global sc_nom
    nom = nom_joueur
    chemin = Path('TP Pendu')   # vérification fichier scores
    fichier = chemin/'scores'
    if fichier.exists() == True:
        print(fichier.exists())         # scores existe, est extrait, joueur ajouté puis affiché
        with open('TP Pendu/scores','rb') as fichier:
            dict_scores = pickle.Unpickler(fichier) 
            score = dict_scores.load()
            if nom_joueur in score.keys():      # score du joueur en memoire
                print(f'Bonjour {nom_joueur}, votre score enregistré est de {score[nom_joueur]} points.')
                sc_nom = score[nom_joueur]
            else:                               # score à 0 si nveau joueur
                score[nom_joueur] = 0
                sc_nom = score[nom_joueur]
        with open('TP Pendu/scores','wb') as fichier:   # dico scores mis à jour
            dict_scores = pickle.Pickler(fichier)
            dict_scores.dump(score)
            print(score)                           # dico affiché
        
    else:
        print(fichier.exists())         # scores n'existe pas, est créé, joueur ajouté puis affiché
        with open('TP Pendu/scores','wb') as fichier:   # dico créé avec nveau joueur à 0
            dict_scores = pickle.Pickler(fichier)
            score = dict()
            score[nom_joueur] = 0
            sc_nom = score[nom_joueur]
            dict_scores.dump(score)
        with open('TP Pendu/scores','rb') as fichier:
            dict_scores = pickle.Unpickler(fichier)
            score = dict_scores.load()
            print(score)                            # dico affiché

def initialisation(LISTE_MOTS):                     # choix du mot à deviner ds la liste
    global mot_choisi
    tentatives = 0                                  # nbr de tentative mis à 0
    mot_choisi = LISTE_MOTS[randint(0,len(LISTE_MOTS)-1)]
    print(mot_choisi)
    return mot_choisi

def lettre_entree(lettres_ok):
    val = input('saisissez une lettre -')           # val : lettre choisie
    lettres_ok = lettres_ok + val                   # lettres_ok : lettres déjà jouées
    mot(val,lettres_ok)


def mot(val,lettres_ok):
    global tentatives
    lettres_mot = ''
    if val in mot_choisi:       # la lettre est dans le mot
        print(f'Il y a {mot_choisi.count(val)} "{val}" dans le mot')
        for i in mot_choisi:
            if i not in lettres_ok:     # les lettres inconnues sont rempl par '_'
                lettres_mot = lettres_mot + '_'
            else:                       # les lettres trouvées sont affichées
                lettres_mot = lettres_mot + i
        print(lettres_mot,'\n',''.center(50,'*'))
        print('tentatives restantes :', NBR_CHANCES-tentatives)
    else:                       # la lettre n'est pas dans le mot
        tentatives += 1
        print('Mauvais choix, recommencez!','\n','tentatives restantes :', 8-tentatives)
    print('lettre mot-',lettres_mot,'lettre ok-',lettres_ok)

    val_i = 0
    for i in mot_choisi:
        if i in lettres_ok:   
            val_i += 1       
            if val_i == NBR_CHANCES:                  # le mot est trouvé!
                print('GAGNE!')
                points(tentatives)          # affectations des points restants 
                lettres_ok = ''             # remise à 0 des variables
                lettres_mot = ''
                initialisation(LISTE_MOTS)  # nveau mot
                lettre_entree(lettres_ok)   # nvelle recherche
        elif tentatives < NBR_CHANCES:                
                lettre_entree(lettres_ok)   # des tentatives sont encore possibles
        else:
            print('PERDU!')         # c'est perdu...

def points(tentatives):
    global sc_nom
    nbr_points = NBR_CHANCES - tentatives             # points calculés
    sc_nom = sc_nom + nbr_points            # nveu score
    with open('TP Pendu/scores','rb') as fichier:
            dict_scores = pickle.Unpickler(fichier) 
            score = dict_scores.load()
    score[nom] = sc_nom
    print(score)
    with open('TP Pendu/scores','wb') as fichier:   # dico scores mis à jour
            dict_scores = pickle.Pickler(fichier)
            dict_scores.dump(score)
    print(f'Vous gagnez {nbr_points} points. Total : {sc_nom} points',
    '\n',''.center(50,'*'),'\n',' - NOUVEAU MOT -')
    tentatives = 0                          # tentatives remises à 0

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")