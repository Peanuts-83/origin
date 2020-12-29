# -*-coding:latin-1 -*
#import os # On importe le module os


liste=[(69, 38), (92, 75),
       (37, 89), (64, 52), (70, 72), (84, 44),
       (13, 0), (20, 67), (38, 56), (40, 98)]

liste1 = sorted(liste, key=lambda x : x[0])
print('tri par index 0 des tuples : ',liste1)
liste2 = sorted(liste, key=lambda x : x[1])
print('tri par index 1 des tuples : ',liste2)
    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
