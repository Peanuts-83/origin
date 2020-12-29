from turtle import *
speed(12)

def rect(longueur,largeur):
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)
    forward(longueur)
    left(90)
    forward(largeur)
    left(90)

up(),goto(0,0),down()
for n in range(90):
    rect(80,30),lt(4)




done()