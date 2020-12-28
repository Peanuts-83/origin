# -*-coding:latin-1 -*
"""Module multiply avec fonction table"""
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

def table(nb,max=10):
    i = 1
    while i <= max: # tant que <condition>
        print(f"{i} x {nb} = {i * nb}")
        i += 1 # incrémentation de i par pas de 1


# autotest
#if __name__ == "__main__": 
#    table(8)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
