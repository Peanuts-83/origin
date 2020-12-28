# -*-coding:latin-1 -*
import os # On importe le module os

var = input('liste nbres')
print(var)

liste = var.split()
print('liste : ',liste)

tuple = tuple(liste)
print('tuple : ',tuple)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
