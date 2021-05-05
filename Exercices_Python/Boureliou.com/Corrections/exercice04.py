# -*- coding: utf8 -*-

if __name__ == "__main__":

    d = {'nom'   : 'Dupuis',
         'prenom': 'Jacque',
         'age'   : 30}

    # Correction
    d['prenom'] = 'Jacques'

    # clés
    print d.keys()

    # valeurs
    print d.values()

    # paires clés/valeur
    for key, value in d.items():
        print '%s : %s' % (key, value)

    # il a quel âge ?
    print "%s %s a %d ans" % (d['prenom'], d['nom'], d['age'])