# -*-coding:latin-1 -*
#import os # On importe le module os


def supprime(l,i):          # f° suppression lettre l en index i
    return l[:i]+l[i+1:]    # return pour info f° print()


def renverse(l):            # f° renverse tuple basée sur la longueur du tuple
    print('tuple l =',l)
    t_renv = tuple()
    for i in range(len(l)):     
        t_renv = t_renv + (l[abs((i+1)-len(l))],)
    return t_renv

l = tuple(input())
for i in range(len(l)):
   print(supprime (l,i))

print(renverse(l))


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
