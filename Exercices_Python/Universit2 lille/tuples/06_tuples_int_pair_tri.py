# -*-coding:latin-1 -*
#import os # On importe le module os


from random import randint

def liste_d_entiers_au_hasard(n):   # tuple de n entiers au hasard
    i=0
    t=tuple()
    while i<=n:
        t = t + (randint(0,100),)   # (n,) pour ajouter � un tuple!!!
        i+=1
    print(n,' entiers de 0 � 100 : ',t)
    print('entiers pairs dans cette liste : ',filtre_pair(t))

def filtre_pair(t):                 # tuple des nbres pairs du tuple pr�c�dent
    t2=tuple()
    for i in t :
        if i%2 == 0:
            t2=t2+(i,)
    return t2

def filtre_indice_pair(n):      # tuple entiers pairs qd n = tuple(range(n)))
    tuple3 = tuple()
    for i in n:
        if i%2 == 0:
            tuple3 = tuple3 + (i,)
    print('valeurs paires de 0 � la valeur max :',tuple3)




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
