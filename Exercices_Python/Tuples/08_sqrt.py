# -*-coding:latin-1 -*
#import os # On importe le module os

import math

while 1:
    nbr = int(input('nbre = '))

    try:
        print('racine carrée =',math.sqrt(nbr))
    except:
        print('racine carrée pas calculable')




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
