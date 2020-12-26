# -*-coding:latin-1 -*
#import os # On importe le module os

import math
import random

#1
i = input('saisir un angle-')
print(type(i))
i = int(i)
print(math.acosh(i),'\n')

#2
##result = float()
##val1 = float()
##val2 = float()
def addition(val1,val2):
    result = val1+val2
    return result
def carre(val1):
    result = val1**2
    return result
def cube(val1):
    result = val1**3
    return result
def de_dix_faces():
    result = random.randint(0,10)
    return result

#3
def resultat(result):
    print(result,'cm')

resultat(carre(int(4)))
resultat(addition(carre(4),carre(4)))
resultat(cube(5.5))
resultat(addition(cube(5.5),cube(5.5)))
resultat(addition(de_dix_faces(),de_dix_faces()))

#4
def al(n):
    annee_lum = 299792.458 * 31557600
    dist = annee_lum * n
    print(n,' année lumière = ',dist,'km')
    
n = float(input('Entrer une distance en année/lumière : '))
al(n)






# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
