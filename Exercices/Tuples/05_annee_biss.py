# -*-coding:latin-1 -*
#import os # On importe le module os

while 1 :
    annee = int(input('entrer année :'))

    if annee%100 != 0 and annee%4 == 0 or annee%400 == 0:
        print('BISSEXTILE')
    else:
        print('Non bissextile...')
    print('\n', ''.center(50,'*'))



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
