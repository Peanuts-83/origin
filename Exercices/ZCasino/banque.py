# -*-coding:latin-1 -*
# import os # windows only

"""Module banque"""

#
def gain_user(mise, multiplicateur):
    global gain
    gain = mise * multiplicateur


def val_cagnotte(cagn, gain):
    global cagnotte
    cagnotte = cagn + gain

    


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
# os.system("pause")


