# -*-coding:latin-1 -*
#import os # On importe le module os

suite1='Pique,Trèfle,Coeur,Carreau'
liste_val=[(2,'Deux'),(3,'Trois'),(4,'Quatre'),
        (5,'Cinq'),(6,'Six'),(7,'Sept'),(8,'Huit'),
        (9,'Neuf'),(10,'Dix'),(11,'valet'),(12,'dame'),(13,'roi'),(14,'as')]

liste_coul = suite1.split(',')
jeu = []
for a in liste_coul:
    for b in liste_val:
        jeu.append((a,) +b)
print(jeu)





# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
