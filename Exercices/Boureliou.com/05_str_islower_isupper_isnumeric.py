# -*-coding:latin-1 -*
import os # On importe le module os


while 1:
    
    var = input('entrer un caractère : ')

    if var.islower() == True:
        print('lettre minuscule')
    elif var.isupper() == True:
        print('lettre majuscule')
    elif var.isnumeric() == True:
        print('chiffre')
    else:
        print('autre chose...')



    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
