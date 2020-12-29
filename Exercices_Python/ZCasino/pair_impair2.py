# -*-coding:latin-1 -*
# import os # windows only

"""Module pair_impair"""

stat = 0

def couleur(n,m):
    global stat
    if n%2 == 0 and m%2 == 0 :
        stat = 'ok_pair'
    elif n%2 != 0 and m%2 != 0 :
        stat = 'ok_impair'
    else :
        stat = 0



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
# os.system("pause")
