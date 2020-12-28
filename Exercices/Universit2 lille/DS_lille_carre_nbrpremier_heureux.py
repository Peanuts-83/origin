#-*-coding:latin-1 -*-
#import os # On importe le module os

def reduit(caisse,pourc):
    print(caisse - (caisse * pourc / 100))

def raymond(s):
    mois=0
    while s>1:
        s = s -(s*10/100)
        mois += 1
    print(mois)

def m(a):
    s=0
    b=a
    while b>0:
        s = s +b%10
        b = b//10
        print(type(s),' - ',b)
    print(s)

def somme_carres(n):
    res=0
    while n>0:
        res = res + (n%10)**2
        n = n//10
    return res
        
def est_heureux(n):
    if n>0:
        while somme_carres(n) != (1,4):
            n = somme_carres(n)
            if somme_carres(n) == 1:
                return True
            elif somme_carres(n) == 4:
                return False

def est_premier(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
            
def est_premier_heureux(n):
    for i in range(1,n+1):
        if est_heureux(i) == True:
            if est_premier(i) == True:
                print(i)

est_premier_heureux(97)









# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
