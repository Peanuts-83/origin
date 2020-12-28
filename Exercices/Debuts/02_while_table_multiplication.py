# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

while 1:
    nb = input("choisissez un nombre : ")
    nb = int(nb)
    i = 1
    while i <= 10: # tant que <condition>
        print(f"{i} x {nb} = {i * nb}")
        i += 1 # incrémentation de i par pas de 1

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
