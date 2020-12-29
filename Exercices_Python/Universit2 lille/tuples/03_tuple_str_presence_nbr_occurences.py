# -*-coding:latin-1 -*
#import os # On importe le module os


def indice(x, t):       # f° présence elt dans un tuple
    if x in t:          
        print(1)
    else:
        print(0)

def nbr_occ(x, t):      # f° nbr d'occurences elt dans un tuple
    print(t.count(x))

chaine = input('? ')    # appel de f° nbr d'occurences dans une chaine
nbr_occ('a', chaine)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
