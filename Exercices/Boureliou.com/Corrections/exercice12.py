# -*- coding: utf8 -*-

if __name__ == "__main__":

    # 1)
    print "Ecriture dans un fichier..."
    phrases = ["Ah non attention, je suis mon meilleur modèle car le cycle du cosmos dans la vie...",
               "Je me souviens en fait, si vraiment tu veux te rappeler des souvenirs.",
               "You see, je ne suis pas un simple danseur car on vit dans une réalité qu'on a créée et que j'appelle illusion.",
               "Même si on se ment, après il faut s'intégrer tout ça dans les environnements et le cycle du cosmos dans la vie..."]
    f = open('texte.txt', 'w')
    try:
        for phrase in phrases:
            f.write(phrase + '\n')
    finally:
        f.close()

    """ Autre solution en python >2.6, qui gère automatiquement le try/finally/close:
    with open('texte.txt', 'w') as f:
        for phrase in phrases:
            f.write(phrase + '\n')
    """

    # 2)
    print "Lecture et étude du fichier..."
    with open('texte.txt', 'r') as f:
        lignes = f.readlines()
        print 'Nombre de lignes : %d' % len(lignes)

        for i in range(len(lignes)):
            print "Ligne %d: %d caractères" % (i+1, len(lignes[i]))


