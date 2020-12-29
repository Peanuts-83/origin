# -*- coding: utf8 -*-

from random import randint # fonction de génération aléatoire d'entiers

if __name__ == "__main__":

    print "=== LE JEU DU PLUS OU MOINS ==="

    # Proposition initiale, volontairement erronée
    proposition = 0

    # Génération aléatoire du nombre mystère entre 1 et 100
    nombre_mystere = randint(1, 100)

    # Compteur de coups
    cpt = 1

    # Boucle "tant que l'utilisateur n'a pas trouvé le nombre mystère"
    while proposition != nombre_mystere:

        try:
            proposition = int(raw_input("Devinez le nombre mystère ? "))
        except ValueError:
            print 'Attention vous devez entrer un nombre !!!'
            continue

        if proposition < nombre_mystere:
            print "%d est trop petit !" % proposition
            cpt += 1

        elif proposition > nombre_mystere:
            print "%d est trop grand !" % proposition
            cpt += 1

        else:
            print "Félicitations, le nombre mystère est bien %d !!!" % proposition
            print "Nombre de coups joués : %d" % cpt


