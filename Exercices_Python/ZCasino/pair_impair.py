# -*-coding:latin-1 -*
# import os # windows only

"""Module pair_impair"""

stat_roulette = 0
stat_numero = 0

def couleur(n,m):
    print(n)
    #
    if n%2 == 0 :
        stat_roulette = 2
    else :
        stat_roulette = 1
    #
    if m%2 == 0 :
        stat_numero = 2
    else :
        stat_numero = 1

    #
    global pi
    if stat_roulette == stat_numero :
        pi = True
        print("couleur : true")
        return(pi)
    else :
        pi = False
        print("couleur : false")
        return(pi)
        

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
# os.system("pause")
