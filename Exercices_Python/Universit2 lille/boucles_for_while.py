#-*-coding:latin-1 -*-
#import os # On importe le module os


# affichage motifs
def afficher_ligne(n):
    i = 0
    impr = ''
    while i <= n-1:
        impr = impr + '0'
        i += 1
    print(impr)

# carré de hauteur n 
def afficher_carre(n):
    i = 0
    impr = ''
    while i <= n-1:
        impr = impr + '0'
        i += 1
    for i in impr:
        print(impr)

# triangle de hauteur n
def afficher_triangle(n):
    i = 0
    impr = ''
    while i <= n-1:
        impr = impr + '0'
        i += 1
        print(impr)

# carre de hauteur n avec diagonale de x
def afficher_carre_diag(n):
    i = 0
    impr = ''
    impr2 = 0
    while impr2 < n:
        while i <= n-1:
            if i != impr2:
                impr = impr + '0'
            elif i == impr2:
                impr = impr + 'X'
            i += 1
        i = 0
        impr2 += 1
        print(impr)
        impr = ''
    
##afficher_carre_diag(5)

# triangle de hauteur n
def afficher_triangle(n):
    i = 0
    impr = ''
    while i <= n-1:
##        print('i-',i,'n-',n)
        if i > 0 and i != n-1:
            impr = ' '*(n-i-1)+'0'+' '*(i+i-1)+'0'
            print(impr)
        elif i == n-1:
            impr = '0'.center(n+n-1,'0')
            print(impr)
        else:
            impr = '0'.center(n+n-1,' ')
            print(impr)
        i += 1

##afficher_triangle(5)

# tables multiplication
def table(n):
    multi = 10
    for i in range(multi):
        print(f'{i+1} x {n} = {(i+1)*n}')
        
##table(5)

def tables(a,b):
    for i in range(b-a+1):
        table(a+i)
        i += 1

##tables(3,5)

# return dans for
def est_present(c,s):
    for car in s:
        if c==car:
            print(True)
            return True
    print(False)
    return False

##est_present('m','informatique')


# suites
## fibonacci
def fibonacci(n):
    """
    renvoie le terme de rang n de la suite définie par u0=1, u1=1, u_(n+2)=u_(n+1)+u_n (suite de Fibonacci)
    
    :param n: (int) le rang
    :return: (int) le terme de rang n
    
    CU : n>=0
    
    exemples :
    >>> fibonacci(8)==34
    True
    >>> fibonacci(8)
    34
    """
    if n==0 or n==1: # cas particuliers (on pourrait intégrer ces cas
                     # particuliers en changeant un peu le cas général)
        return 1
    a=1
    b=1
    res=2
    for k in range(3,n+1): # k variant de 3 à n inclus
        a=b
        b=res
        res=a+b
    return res

def rang_fibonacci(m):
    """
    indique le rang à partir duquel le terme de la suite
    dépasse la valeur  m  donnée.

    :param m: (int) valeur à dépasser
    :return: (int) le terme de rang m

    CU : m>=0

    exemples :
    >>> rang_fibonacci(24)
    8
    """
    if m==0 or m==1: # cas particuliers (on pourrait intégrer ces cas
                     # particuliers en changeant un peu le cas général)
        return 1
    a=1
    b=1
    res=2
    for k in range(3,m): # k variant de 3 à m
        a=b
        b=res
        res=a+b
        print('a-',a,'b-',b,'res-',res,'k-',k)
        if res > m:
            return k
## syracuse
def syracuse_suivant(t):
    """
    calcule le terme suivant de t dans la suite de Syracuse
    
    :param t: (int) le terme dont on veut le terme suivant
    :return: (int) le terme suivant
    
    CU : t>0
    
    exemples :
    >>> syracuse_suivant(11)==34
    True
    
    >>> syracuse_suivant(34)==17
    True
    """
    if t%2==0:
        res=t//2
    else:
        res=3*t+1
    return res

def rang_du_terme_1(m):
    """
    retourne le rang pour lequel la suite de Syracuse en partant de m atteint 1
    
    :param m: (int) le terme initial de la suite de Syracuse
    :return: (int) le rang pour lequel le terme est 1
    
    CU : m>0
    
    exemples :
    >>> rang_du_terme_1(9)==19
    True
    """
    terme=m
    rang=0 # résultat à déterminer
    while (terme!=1):
        print('rang-',rang,'terme-',terme)
        terme=syracuse_suivant(terme)
        rang+=1
    return rang
    
def altitude_max(m):
    terme=m
    rang=0 # résultat à déterminer
    maxi=0
    while (terme!=1):
        terme=syracuse_suivant(terme)
        rang+=1
        if  terme > maxi:
            maxi=terme
    return maxi
    
def moyenne(m,n):
    terme=m
    rang=0 # résultat à déterminer
    somme=0
    moy=0
    while (terme!=1):
        somme=somme+terme
        terme=syracuse_suivant(terme)
        rang+=1
        if  rang == n:
            moy = somme/n
            print('somme-',somme,'moy-',moy)
            return moy

## puissance
def puissance(x,n):
    for i in range(n-1):
        x = x*x
    return x

# séries
def somme_alterne(n):
    somme = -1
    for i in range(1,n,2):      # range(start,stop,step)
        somme = somme + 1/(i+1) - 1/(i+2)
    return somme

# diviseurs
## nbre premier
def est_premier(n):
    for i in range(n+1):
        if i>1 and n%i == 0 and i != n:
            return False
    return True

## nbr de diviseurs d'un nbr n
def nbr_diviseurs(n):
    nbr = 0
    for i in range(n+1):
        if i>0:
            if n%i == 0:
                nbr += 1
    return nbr

## decomposition en facteur premiers de n
def fact_prem(n):
    fact = tuple()
    for i in range(n+1):
        if i>0:
            if n%i == 0:
                fact = fact + (str(i),)
    return fact

# manipulation sur entiers
## somme de tous les chiffres de n
def somme(n):
    i=10
    som = 0
    while n//i != 0:        # si n > 10
        som = som + (n%i)   # somme = unité
        n = n//i            # n/10, entier seul conservé
    som = som + n           # somme dernier chiffre
    return som

## miroir de n
def miroir(n):
    i=10
    miroir=0
    while n//i != 0:
        miroir = miroir * i + n%i * i    # unité passée en dizaine
        n = n//i                    # n/10, entier seul conservé
    miroir = miroir + n%i               # ajoute le dernier chiffre
    return miroir

## produit des chiffres de n
def produit(n):
    i=10
    prod=1
    while n//i != 0:
        if n%i != 0:
            prod = prod * int(n%i)           # produit par chiffre des unités
            n = n//i                    # n/10, entier seul conservé
            print('v1-n-',n,'prod-',prod,'n%i',n%i)
        else:
            n = n//i                    # n/10, entier seul conservé
            print('v2-n-',n)
    if n%i != 0:    
        prod = prod * n                 # produit dernier chiffre
    return prod

# Nbr mystere
from random import *

def jeu():
    a = randint(1,100)
    guess = int(input('Choisissez un nombre entre 1 et 100 : '))
    for i in range(8):
        print(a)
        if guess == 0:
            return 'Abandon'
        elif guess == a:
            return 'Gagné!'
        if a > guess:
            print('Nbre plus grand.')
            guess = int(input('Choisissez un nombre entre 1 et 100 : '))
        else:
            print('Nbre plus petit.')
            guess = int(input('Choisissez un nombre entre 1 et 100 : '))
    print('Perdu! le nombre était ',a)

##jeu()        

def jeu_inverse():
    print('Choisissez un nombre entre 0 et 100')
    input('OK?')
    a = randint(1,100)
    liste_choix = ['1','100']
    while 1:
        if liste_choix[0] == liste_choix[1] or liste_choix is False:
                raise ValueError('Vous avez triché!')
        print('\n')
        print("est-ce que votre nbre est ",a,'? (+, -, ou!)')
        reponse = input()
        try:
            if reponse == '+':
                liste_choix[0] = str(a+1)
                a = randint(int(liste_choix[0]),int(liste_choix[1]))
                print (liste_choix)
            elif reponse == '-':
                liste_choix[1] = str(a-1)
                a = randint(int(liste_choix[0]),int(liste_choix[1]))
                print (liste_choix)
            elif reponse == '!':
                print('Gagné!')
        except:
            return 'vous avez triché!'
            
##jeu_inverse()        


# chaine bien parenthesee
def parenth(args):
    if args.count('(') == args.count(')'):
        if args[0] == '(' and args[-1] == ')':
            ouverte = 0
            fermee = 0
            for n in args:
                if n == '(':
                    ouverte += 1
                elif n == ')':
                    fermee += 1
                if fermee > ouverte:
                    print('mal parenthésée!')
                    return 'aaaaaaa'
            else:
                print('Bien parenthésée.')
        else:
            print('mal parenthésée!')
    else:
        print('mal parenthésée!')
            
##parenth('()(()())()')


# développement limité
def dev_lim(n):
    a = 1.0
    n = float(n)
    m = n
    while m/a > 0.0000001:
        m = m * n
        a = a + m/a
        print('m-',m,'a-',a,'m/a-',m/a)
    return a
    

# calcul du pgcd // Plus Grand Denominateur Commun de 2 nbr
def pgcd(a,b):
    f_a = fact_prem(a)  # tuple des facteurs de a
    f_b = fact_prem(b)  #tuple des facteurs de b
    commun = 0
    if a >= b:
        for i in range(len(f_a)):
            if f_b.count(f_a[i]) != 0:
                commun = f_a[i]
            else:
                pass
    elif b > a:
        for i in range(len(f_b)):
            if f_a.count(f_b[i]) != 0:
                commun = f_b[i]
            else:
                pass
    return commun

# zéro d'une fonction par dichotomie // approche 0 axe abs par un intervale [a,b]
def dicho(a,b,fonction):
    """
    Zéro d'une fonction par dichotomie
    f(x) est une fonction continue
    Approche f(x)=0 par un intervale [a,b]
    sensibilité définie à 10-7

    :param a: (int) argument tel que f(a)<0
    :param b: (int) argument tel que f(b)>0
    :param fonction: (str) fonction exprimée sous la forme 'x+8'
    :return a,b: (tuple) intervale à 10-7 près
    
    CU : f(a)<0, f(b)>0, f(x) entre tirets ''
    
    exemples :
    >>> dicho(-3,8,'x+2')
    (-2.000000052154064, -1.9999999701976776)
    >>> dicho(-7,15,'(x/2)**2-36')
    (11.99999999254942, 12.000000074505806)
    """
    m = (a+b)/2
    x = m
    f = eval(fonction)
    while b-a > 0.0000001:  # intervalle précis à 10-7
        m = (a+b)/2         # eccart entre les 2 élts de l'intervale
        x = m               # x prend la valeur de l'intervale
        f = eval(fonction)  # f(x) est calculé
        if f>0:             # si f(x)>0, b est ramené à m
            b = m
        elif f<0:           # si f(x)<0, a est ramené à m
            a = m
    return a,b

# triangles rectangles à longueurs entières
def somme_carre(n):
    k = n-1
    while k > 0:
        #print('k-',k)
        for i in range(n-2):
            #print('i-',i)
            for j in range(n-2):
                #print('j-',j)
                if j**2 + i**2 == k**2 and j >= i and i>0 and j>0:
                    print(j,i,k)
                j += 1
            i += 1
        k -= 1

# Mot le plus grand      
def long(arg):
    a = arg.split(' ')
    plus_long = 0
    index_pl = ''
    for i in range(len(a)):
        if len(a[i]) > plus_long:
            plus_long = len(a[i])
            index_pl = i
    print('le mot le plus long est',a[index_pl])
    
# motif // cherche un mot lettre par lettre dans l'ordre de la phrase s
def est_cache(motif,s):
    long_mot = motif            # motif sera décrémenté lettre par lettre
    for i in motif:
        while i in long_mot:    # recherche de la lettre tant qu'elle est dans le mot
            if i in s:
                s = s.partition(i)  #supprime les lettres avant la lettre trouvée
                s = s[2]
                print(s)
                long_mot = long_mot.replace(i,'',1)
            else:
                return 'mot non trouvé'
        print(long_mot)
    if long_mot == '':
        print('yes')
    else:
        print('no')

# code/decode
def decode(args):
    decodage = ''
    for n in range(0,len(args),2):  # range(debut,fin,pas) passe de lettre en lettre
        decodage = decodage + (args[n]*int(args[n+1]))
    print(decodage)

##decode('a5b3c8')

def encode(args):
    encodage = ''
    n = 0
    while args != '':       # tant que args n'est pas vide
        print(args)
        encodage = encodage + args[n] + str(args.count(args[n]))
        args = args.replace(args[n],'')     # on retire à args les lettres comptées
        print(encodage)
        n +=1
        
    print(encodage)

##encode('aaaaabbbccccccccccccccccccdddeeeefgghhhhhhh')

# anagrame
def est_anagrame(a,b):
    if len(a) == len(b):
        for n in a:
            b = b.replace(n,'')
    if b == '':
        print('oui')
    else:
        print('non')

##est_anagrame('migraine','imaginer')

def supprimer_car(s,i):
    s = s.replace(s[i],'')
    print(s)

##supprimer_car('il faut 8 doigts dans mon nez',8)
        
# suite logique
#???















# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
