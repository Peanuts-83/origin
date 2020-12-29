
def diviseurs():
    val = int(input('saisir un entier -'))
    vals = ()
    for n in range(val):
        if n > 0 and val%n == 0:
            vals += (str(n),)
    print(f'liste des diviseurs de {val} :',vals)

def parfait(val):
    vals = 0
    parfait = ''
    for n in range(val):
        if n > 0 and val%n == 0:
            vals += n
    if vals == val:             # nbre parfait
        parfait = 0
    elif vals > val:            # nbre abondant
        parfait = 1
    elif vals < val:            # nbre deficient
        parfait = -1
    print(parfait)

def poly(x):
    P = x**3 - 10*(x**2) -2610*x +84
    return P

def ptt_poly():
    mini = poly(-50)
    indice = -50
    for i in range(-50,51):         # range fonctionne aussi sur un tuple
        if poly(i) < mini:
            mini = poly(i)
            indice = i
    return f"l'indice {i} donne la valeur de P la plus basse : {mini}."

##############################################################################################

def syracuse(x):                    # f° Syracuse
    if x%2 == 0:
        return (x/2)
    else:
        return (3*x + 1)

def terms():                        # renvoie toutes les valeurs de P jusqu'à 1
    N = int(input('Entrer un nbr >= 0 : '))
    while N != 1:
        N = syracuse(N)
        print(val)

def indice(N):                       # renvoie indice i(N) pour Ui(N)=1
    i = 0
    while N != 1:
        N = syracuse(N)
        i += 1
    return i

def cent_terms():                   # renvoie 100 premiers termes de i(N)
    for N in range(1,101):
        print(f"i({N}) vaut {indice(N)}")

def maxi():                         # renvoie N pour i(N) maxi avec n[0:100]
    maxi = 0
    maxi_N = 0
    for N in range(1,101):
        if indice(N) > maxi:
            maxi = indice(N)
            maxi_N = N
    return maxi_N

def sommet(N):                      # renvoie la plus gde valeur pour i(N)
    sommet = 0
    for i in range(1,N):
        if indice(N) > sommet:
            sommet = indice(N)
    return sommet

def maxi_sommet():                  # renvoie N donne la plus gde valeur 
    maxi_sommet = sommet(1)
    maxi_N = 1
    for N in range(1,101):
        if sommet(N) > maxi_sommet:
            maxi_sommet = sommet(N)
            maxi_N = N
    return f"i({maxi_N}) (pour N <= 100) est l'indice de la plus grande valeur : {maxi_sommet}"

##############################################################################################

