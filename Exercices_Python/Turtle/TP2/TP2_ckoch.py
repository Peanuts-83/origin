
#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP2')
turtle.title('TP2- exo 3')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('light grey')
turtle.speed('fast')

# courbe de Von Koch
def courbe_koch(longueur, etape):
    """Fonction récursive pour dessiner une courbe de Von Koch
    (une fonction récursive étant une fonction s'appelant elle-même"""
    if etape == 0:
        turtle.forward(longueur)
    else:
        courbe_koch(longueur/3, etape-1)
        turtle.left(60)
        courbe_koch(longueur/3, etape-1)
        turtle.right(120)
        courbe_koch(longueur/3, etape-1)
        turtle.left(60)
        courbe_koch(longueur/3, etape-1)
 
def flocon_koch(longueur, etape):
    """Fonction pour dessiner un flocon de Von Koch
    depuis le coin haut gauche"""
    for i in range(3):  #Pour chaque côté du triangle initial
        courbe_koch(longueur, etape)  #Courbe de Von Koch
        turtle.right(120)



if __name__ == "__main__":
    flocon_koch(200, 3)
    turtle.exitonclick()

