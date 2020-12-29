#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
""" Exercice 3. Création et utilisation d’un module geometrie.py.
    3 formes géométriques peuvent être utilisées : le carré, le triangle équilatéral 
    et le cercle.

"""
import turtle

def carre(x, y, size):
    """
        Fonction du carré.
        x et y pour le point de départ en bas à gauche.
        size pour la longueur du coté.
    """
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def triangle(x, y, size):
    """
        Fonction du triangle équilatéral.
        x et y pour le point de départ en bas à gauche.
        size pour la longueur du coté.
    """
    for _ in range(3):
        turtle.forward(size)
        turtle.left(360/3)

def circle(x, y, size):
    """
        Fonction du cercle.
        x et y pour le point de départ en bas.
        size/36 pour la longueur du segment.
    """
    for _ in range(36):
        turtle.forward(size/36)
        turtle.left(360/36)

os.system("pause")

