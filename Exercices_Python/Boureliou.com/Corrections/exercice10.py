# -*- coding: utf8 -*-

class Voiture:
    """ Reproduit le comportement d'une voiture """

    def __init__(self, marque='Peugeot', couleur='rouge'):
        """ Constructure, seules la marque et la couleur peuvent être définies """
        self.marque = marque
        self.couleur = couleur
        self.pilote = ''
        self.vitesse = 0
        self.moteur = ''

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
        print "%s %s %s pilotée par %s à la vitesse de %s m/s." % (
                    self.marque,
                    self.couleur,
                    self.moteur,
                    pilote,
                    self.vitesse
                    )

class VoitureEssence(Voiture):

    def __init__(self, marque='Peugeot', couleur='rouge'):
        """ Constructure, seules la marque et la couleur peuvent être définies """
        Voiture.__init__(self, marque, couleur)
        self.moteur = 'essence'

class VoitureDiesel(Voiture):

    def __init__(self, marque='Peugeot', couleur='rouge'):
        """ Constructure, seules la marque et la couleur peuvent être définies """
        Voiture.__init__(self, marque, couleur)
        self.moteur = 'diesel'

    def accelerer(self, taux, duree):
        """ Accélération/décélération """
        if taux > 30:
            print 'Une voiture Diesel ne peux pas accélérer à un taux suppérieur à 30 m/s !'
        else:
            Voiture.accelerer(self, taux, duree)

