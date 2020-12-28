# -*-coding:latin-1 -*
#import os # On importe le module os

import cmath

#1/ prédicats

def range_float(a,b,c):
    range_ls = [(n / 10.0) for n in range(a, b, c)]
##        print(range_ls)
    return range_ls

def est_dans(x):
    I1 = set(n for n in range_float(-10, 31, 1))
    I2 = set(n for n in range_float(-9, 31, 1))
    I3 = set(n for n in range_float(-9, 31, 1)) | set(n for n in range_float(80, 100, 1))
##        inf = round(cmath.inf)
##        I4 = set(n for n in range_float(-9, 31, 1)) | set(n for n in range_float(80, inf, 1)) 
    print('ensemble 1 :',x in I1)
    print('ensemble 2 :',x in I2)
    print('ensemble 3 :',x in I3)
    
x = float(input('nbre? '))
est_dans(x)

print('\n',''.center(50,'*'))
#2/ Signes
    
def est_positif(x):
    if x >= 0:
        print('True')
    else:
        print('False')

def meme_signe(x,y):
    if (x >= 0 and y>= 0) or (x <= 0 and y <= 0):
        print('True')
    else:
        print('False')

est_positif(int(input('nbre positif? ')))

a = input('même signe? ')           # chaine nbre sép par ','
a = a.split(',')                    # a devient liste
meme_signe(int(a[0]), int(a[1]))    # appelle f°


print('\n',''.center(50,'*'))
#3/ Géométrie

def dans_rectangle(x,y):
    if x >=2 and x <= 10 and y >= 4 and y <= 8:
        print(True)
    else:
        print(False)

a = input(' x, y rectangle? ')
a = a.split(',')
dans_rectangle(int(a[0]), int(a[1]))

##def dans_disque(x,y):
##    if x in (cmath.pi * 2 * 2):


print('\n',''.center(50,'*'))
#4/ Arithmétique

def yacoupe(annee):
    if annee > 1930 and annee%2 == 0 and annee%4 != 0:
        print('Ya coupe!')
    else:
        print('nope...')

a = int(input('date de coupe ? '))      
yacoupe(a)    # appelle f°


print('\n',''.center(50,'*'))
#5/ instr condit°

















# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
