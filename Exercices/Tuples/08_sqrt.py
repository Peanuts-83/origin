# -*-coding:latin-1 -*
#import os # On importe le module os

import math

while 1:
    nbr = int(input('nbre = '))

    try:
        print('racine carr�e =',math.sqrt(nbr))
    except:
        print('racine carr�e pas calculable')




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
