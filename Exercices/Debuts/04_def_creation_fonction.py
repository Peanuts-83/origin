# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # syst�me d'exploitation

def table(nb, max=10):
    i = 1
    while i <= max: # tant que <condition>
        print(f"{i} x {nb} = {i * nb}")
        i += 1 # incr�mentation de i par pas de 1


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")