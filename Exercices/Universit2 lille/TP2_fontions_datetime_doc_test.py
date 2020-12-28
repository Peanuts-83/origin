# -*-coding:latin-1 -*
#import os # On importe le module os


#1/ conversion celsius/farenheit
def c(F):
    c = 5/9*(F-32)
    return c
def f(C):
    f = 9/5*C+32
    return f

print(f'Une température de 20°C correspond à un température de {f(20)}F')
print(f'Une température de 75F correspond à un température de {c(75)}°C')
valc = int(input('température en °C :'))
print(valc,'°C vaut ',f(valc),'F',
      '\n la preuve, ',f(valc),'F vaut ',c((f(valc))),'°C!')

print('\n'.center(75,'*'))
#2/ age en secondes
ref_an = 1975
ref_mois = 3
ref_jour = 22
nbre_sec_jour = 24 * 60 * 60
nbre_sec_an = nbre_sec_jour * 365.2425
auj_an = 2020
auj_mois = 10
auj_jour = 4

ecart = (auj_jour * nbre_sec_jour + auj_mois * 30 * nbre_sec_jour
         + auj_an * nbre_sec_an) - (ref_jour * nbre_sec_jour
                                    + ref_mois * 30 * nbre_sec_jour
                                    + ref_an * nbre_sec_an)
print('Votre age est de ',ecart,'secondes','\n')

### age reel avec date reelle du jour par datetime.date.today()
from datetime import *
auj = date.today()
def age_en_sec(args):
    naiss = args
    ecart = (auj.day * nbre_sec_jour + auj.month * 30 * nbre_sec_jour
         + auj.year * nbre_sec_an) - (int(naiss[0]) * nbre_sec_jour
                                    + int(naiss[1]) * 30 * nbre_sec_jour
                                    + int(naiss[2]) * nbre_sec_an)
    print('Votre age réel est de ',ecart,' secondes!')

age = input('age jj/mm/aaaa :')
age = age.split('/')
age_en_sec(age)

print('\n'.center(75,'*'))
#3/ analyse de f°
while 1 :
    from math import *
    def undefined(x):
        """
            Doc normalisée de la fonction undefined(x)
            Calcul du logarithme décimal de 'x' auquel
            on ajout 1.
            La valeur entière(floor) de ce calcul est
            retourné sous forme d'entier.
            : param x : (int or float) valeur numérique
            : return : (all) valeur numerique ]0:infini[

            CU : x > 0

            Exemples :
            >>> undefined(8)
            1
            >>> undefined(56)
            2
            >>>  undefined(789)
            3
            ...
            ValueError: math domain error
        """
        a = log10(x) + 1
        b = floor(a)
        print(b)

    # test standard de la doc #
    print('\n','lancement automatique de la procédure de test de la doc da la fonction'.center(75,'*'),'\n')
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose = True)

    # demande de valeur numérique > 0
    print('\n',''.center(75,'*'))
    x = int(input('??? '))
    undefined(x)
##    print(b)




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
