# -*-coding:latin-1 -*
import os # windows only

# table de multiplication avec choix du nbre multiplié et de l'étendue de la table

from multiply import * # import des var et fonctions du module multiply.py
# alternative : import multiply

# entrée des 2 nbre par user
a = input("nombre multiplié : ")
b = input("étendue de la table : ")

# variable a en nombre entier "int"
a = int(a)
b = int(b)

table(a, b) # test fonction table
# alternative : multiply.table(a, b)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
