# -*-coding:latin-1 -*
import os # On importe le module os

"""
Le jeu qui appelle les variables et utilise les fonctions.
"""
# import des données et fonctions
from donnees import *
from fonctions import *

# début du jeu : nom du joueura
# nom_joueur = input('Bonjour, quel est votre nom?')
nom_joueur = 'tom'

# active la fonction joueur, fichier score vérifié/créé
tableau_joueurs(nom_joueur)

# Initialisation du jeu
print('\n','Le jeu peut commencer, vous avez 8 chances pour trouver le mot mystère.')
initialisation(LISTE_MOTS)
print(mot_choisi)
lettres_ok = ''             # lettres trouvées initialisées à None
lettre_entree(lettres_ok)   # lancement de la séquence de recherche des lettres





# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
