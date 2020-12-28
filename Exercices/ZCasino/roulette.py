# -*-coding:latin-1 -*
# import os # windows only

"""Module roulette"""

# fonction randint du module intégré random
def roul():
    global nbr_lott
    from random import randint
    nbr_lott = randint(0, 49)
#    return(nbr_lott)
    
    


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
# os.system("pause")
