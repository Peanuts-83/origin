# -*- coding: utf8 -*-

ANNEE_COURANTE = 2011

if __name__ == "__main__":

    # Ce script ne gère pas si l'anniversaire est passé ou non d'où le "environ"
    annee_naissance = raw_input("Quelle est votre année de naissance ? ")
    age = ANNEE_COURANTE- int(annee_naissance)

    print "Vous avez environ %d ans" % age