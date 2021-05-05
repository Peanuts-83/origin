# -*- coding: utf8 -*-

import string

if __name__ == "__main__":

    # Attention, le programme suivant n'inclu pas de gestion d'erreur
    #

    lettre = raw_input('Entrez un caractère : ')

    if lettre in string.lowercase: # abcdefghijklmnopqrstuvwxyz
        print "C'est une lettre minuscule."
    elif lettre in string.uppercase: # ABCDEFGHIJKLMNOPQRSTUVWXYZ
        print "C'est une lettre majuscule."
    elif lettre in string.digits: # 0123456789
        print "C'est un chiffre."
    else:
        print "C'est autre chose."
