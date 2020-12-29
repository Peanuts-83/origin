# -*-coding:latin-1 -*
#import os # On importe le module os

def sumall(*args):
    t = args
    somme = 0
    print(t)
    print(type(t))
    for n in t:
        somme = somme + n
    print('somme des args =',somme)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
