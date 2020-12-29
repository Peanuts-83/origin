# -*-coding:latin-1 -*
#import os # On importe le module os

def est_divisible(n,t):         # vérifie n divisible par un élt de t
    for i in range(len(t)):
        if n % int(t[i]) == 0:
            print(n,'est divisible par',t[i])

def enumere_premiers(n):        # valide nbr premier
    #t = tuple(range(n+1))
    nbr_premier = tuple()
    for i in range(2,n):        # n divisible de 2 à n?
        if n%i != 0:
            if n%n == 0:
                nbr_premier = nbr_premier + (1,)    # (1,) ajout de tuple!!!
        elif n%i == 0:
            nbr_premier = nbr_premier + (2,)
            print(n,' est divisible par ',i)    # valeurs qui divisent n
    print(nbr_premier)                          # tuple de 1 et 2, si 2, pas premier
    if nbr_premier.count(2) > 0:
        print('nbre non premier')
    else:
        print('nbre premier')

while 1:
    n = int(input('?'))
    t = tuple(input('???'))
    #print(type(n), n, type(t), t)
    est_divisible(n,t)

    enumere_premiers(n)

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
