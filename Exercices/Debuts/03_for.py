# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

chaine = "coucou"
for lettre in chaine: # repete chq carract 
    if lettre in "AEIOUYaeiouy": # verif var est un de ces elements
        print(lettre)
    else:
        print(chaine)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
