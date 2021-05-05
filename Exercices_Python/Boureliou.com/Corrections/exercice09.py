# -*- coding: utf8 -*-

class Voiture:
    """ Reproduit le comportement d'une voiture """

    def __init__(self, marque='Peugeot', couleur='rouge'):
        """ Constructure, seules la marque et la couleur peuvent être définies """
        self.marque = marque
        self.couleur = couleur
        self.pilote = ''
        self.vitesse = 0

    def accelerer(self, taux, duree):
        """ Accélération/décélération """
        if self.pilote == '':
            print "Cette voiture n'a pas de conducteur !"
        else:
            self.vitesse = self.vitesse + taux * duree

    def choix_conducteur(self, nom):
        """ Choix d'un conducteur """
        self.pilote = nom

    def description(self):
        """ Description de la voiture """
        pilote = self.pilote
        if pilote == '':
            pilote = 'personne'
        print "%s %s pilotée par %s à la vitesse de %s m/s." % (
                    self.marque,
                    self.couleur,
                    pilote,
                    self.vitesse
                    )
