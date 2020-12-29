from turtle import *
speed(12)

def carre(longueur):
    forward(longueur)
    left(90)
    forward(longueur)
    left(90)
    forward(longueur)
    left(90)
    forward(longueur)
    left(90)

up(),goto(-100,0),down()
for n in range(12):
    carre(50),lt(30)

up(),goto(150,0),down()
for n in range(24):
    carre(80),carre(10),lt(15)


done()