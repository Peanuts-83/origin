# -*-coding:latin-1 -*
import os # On importe le module os

liste = []
i=700
while i<1100:
    liste.append(i)
    i += 1

liste_div7 = [n for n in liste if n%7 == 0]

liste_finale = [n for n in liste_div7 if n%5 !=0 and n%2 !=0]

print(liste_finale)




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
