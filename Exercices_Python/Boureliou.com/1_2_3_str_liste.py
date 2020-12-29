# -*-coding:latin-1 -*
import os # On importe le module os

# import modules
import datetime


# gestion de la date
date = datetime.datetime.now()

# nom
print(' 1/ Nom '.center(50, '-'))
nom = input('entrer un nom : ')
print(f'Bonjour {nom}', '\n')
# age
print(' 2/ Age '.center(50, '-'))
annee = int(input('année de naissance ? '))
age = date.year - annee
print(f'Vous avez {age} ans', '\n')
# liste
print(' 3/ Liste '.center(50, '-'))
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{L}'.center(50,' '), '\n')

L = [n+1 for n in L]
print('a. n+1 : ', L)
L.append(11)
print('b. Ajout 11 : ', L)
L.append(12) and L.append(13)
print('c. Ajout 12 et 13 : ', L)
print(f'd. 1er elt : {L[0]}. 2 premiers elts : {L[:2]}. Dernier elt : {L[-1:]}. 2 derniers elts : {L[-2:]}') 
L_pair = [n for n in L if n%2 == 0]
L_impair = [n for n in L if n%2 != 0]
print(f'e. liste des chiffres pairs {L_pair} et des chiffres impairs {L_impair}')
L.insert(3, 3.5)
print('f. 3.5 inséré en index[4] ', L)
L.remove(3.5)
print('g. 3.5 retiré ', L)
L.sort(reverse=True)
print('h. Liste inversée', L)
print('i. nbre au hasard : ')
while 1 :
    val = input('entrer un entier : ')
    val=int(val)
    try:
        if L[val] in L:
            print('valeur comprise dans la liste.', '\n')
        else:
            print(val, 'pas dans la liste!')
            continue
    except:
        print(val, 'pas dans la liste!')
        pass
        continue




    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
