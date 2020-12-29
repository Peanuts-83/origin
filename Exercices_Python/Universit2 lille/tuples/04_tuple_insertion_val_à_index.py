# -*-coding:latin-1 -*
#import os # On importe le module os

def insere(e,i,t):      # f° inserer une val e à un index i ds un tuple
    tup1 = tuple(t)
    #e = (e,)           # la valeur insérée doit etre un tuple! (e,)
    tup2 = (tup1[:i]+(e,)+tup1[i:])
    print(tup2)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
