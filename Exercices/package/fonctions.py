# -*-coding:latin-1 -*
import os # windows only

# table de multiplication avec choix du nbre multipli� et de l'�tendue de la table

from multiply import * # import des var et fonctions du module multiply.py
# alternative : import multiply

# entr�e des 2 nbre par user
a = input("nombre multipli� : ")
b = input("�tendue de la table : ")

# variable a en nombre entier "int"
a = int(a)
b = int(b)

table(a, b) # test fonction table
# alternative : multiply.table(a, b)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
