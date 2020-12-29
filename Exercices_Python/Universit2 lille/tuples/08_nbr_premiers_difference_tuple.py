# -*-coding:latin-1 -*
#import os # On importe le module os


def enumere_premiers(n):
    t = tuple()                 # tuple des nbr non premiers
    for n in range(2,n):
        for i in range(2,n):
            if i<n:
                if n%i != 0:
                    pass
                else:
                    t = t + (n,)
    t_premiers = tuple()         # tuple par différence des entiers premiers
    for i in range(2,n):
        if i not in t:
            t_premiers = t_premiers + (i,)
    print('nbres premiers :',t_premiers)
    print('qtté :',len(t_premiers))


##var = int(input('étendue de la recherche ? '))
##enumere_premiers(var)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
