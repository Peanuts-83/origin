# -*- coding: utf8 -*-

import pickle

def sauvegarderVoiture(voiture, nom_fichier):
    fichier = open(nom_fichier, 'w')
    pickle.dump(voiture, fichier)
    fichier.close()

def chargerVoiture(nom_fichier):
    fichier = open(nom_fichier, 'rw')
    voiture = pickle.load(fichier)
    fichier.close()
    return voiture

