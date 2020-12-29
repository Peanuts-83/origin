#-*-coding:latin-1 -*-
#import os # On importe le module os

from turtle import *

def poly_reg_conv(n):
    deg = 360/n
    for i in range(n):
        fd(100),lt(deg)

def poly_reg_convexe(n,l):
    deg = 360/n
    for i in range(n):
        fd(l),lt(deg)

def figure(n,l):
    compteur = 0
    pu(),goto(250,-250),pd()
    for i in range(4):
        for i in range(n):
            deg = 360/n
            fd(l),lt(deg)
        compteur += 1
        n -= 1
        if compteur == 1:
            pu(),goto(-250,-250),pd()
        elif compteur == 2:
            pu(),goto(250,250),pd()
        else:
            pu(),goto(-250,250),pd()

def polygone_etoile(n,l,k):
    """
    n = nbr de sommets
    l = longueur entre 2 sommets opposés
    k = sommets parcourus de k en k
    pour 1 polygone convexe, k=1
    pour 1 polygone étoilé, k=[2:inf[
    """
##    pu(),goto(0,0),pd()
    speed(10)
    for i in range(n):
        deg = 360/(n/k)
        fd(l),lt(deg)
    
def figure_etoile(n,l,k):
    compteur = 0
    pu(),goto(250,-250),pd()
    for i in range(4):
        if compteur > 2:
            n = 5
        polygone_etoile(n,l,k)
        compteur += 1
        n -= 1
        if n<9 and n>=7:
            k = 3
        elif n<7:
            k = 2
        if compteur == 1:
            pu(),goto(-250,-250),pd()
        elif compteur == 2:
            pu(),goto(250,250),pd()
        else:
            pu(),goto(-250,250),pd()

def tortue_sortie(x,y):
    """
    x = xcor tortue dans un carré de 400 de coté
    y = ycor tortue dans un carré de 400 de coté
    CU: x et y E [-200:200]
    """
    from random import randint      # import fé randint
    speed(10)
    pu(),goto(-200,200),pd()
    color('blue')
    for i in range(4):      # création du territoire (un carré de 400 de coté)
        fd(400),rt(90)
    turtle = (x,y)          # position initiale tortue
    pu(),goto(turtle),pd()  # postionnement du curseur sur turtle
    color('green')
    while xcor()>-200 and xcor()<200 and ycor()>-200 and ycor()<200:    # le curseur doit rester dans le carré
        lt(randint(1,359)),fd(randint(10,30))   #rotation puis déplact aléatoires
    return 'sorti!'


def sens_boule(x,y,old_x,old_y):    # détecte le sens de dépl de la boule NSEW
    if old_x - x > 0:
        sens_x = 'W'
    else:
        sens_x = 'E'
    if old_y - y > 0:
        sens_y = 'S'
    else:
        sens_y = 'N'
    return (sens_x,sens_y)

def moderate(angle):
    """
    passe l'angle de ]90:360] à un angle de [0:90]
    """
    ang=int(angle)
    while ang>90:
        ang=ang-90 
    return ang

def billard(x,y,angle,nbr_bandes):
    """
    x = xcor boule
    y = ycor boule
    angle = angle de départ en degrés
    nbre_bandes = rebonds a effectuer
    CU: x et y E [-200:200,-300;300], angle E [0:359], nbre_bandes is int()>0
    """
    speed(20)
    pu(),goto(-200,300),pd()
    color('red','green')
    begin_fill()
    for i in range(2):      # création du territoire (un rect de 400*600 de coté)
        fd(400),rt(90),fd(600),rt(90)
    end_fill()
    bande = int(nbr_bandes)
    pu(),goto(x,y),pd()      # curseur a la place de la boule
    rt(angle)               # angle de la queue
    angle=moderate(angle)
    old_x = x       # pr déterminer sens E/W de la boule    
    old_y = y       # pr déterminer sens N/S de la boule
    import time             # import des fonctions time
    while bande > 0:
        fd(5)
        sens = sens_boule(xcor(), ycor(), old_x, old_y)
        # print(sens,xcor(),ycor())
        old_x=xcor()
        old_y=ycor()
        if xcor()<=-195 or xcor()>=195 or ycor()<=-295 or ycor()>=295:
            time.sleep(0.1)           # temporisation 0.3 sec
            if sens[0] == 'W':        # vers la gauche, bas ou haut, rebond
                if ycor()<=-295:
                    rt(180-angle*2),fd(20)
                    bande -= 1
                elif ycor()>=295:
                    lt(180-angle*2),fd(20)
                    bande -= 1
            if sens[0] == 'E':        # vers la droite, bas ou haut, rebond
                if ycor()<=-295:
                    lt(180-angle*2),fd(20)
                    bande -= 1
                elif ycor()>=295:
                    rt(180-angle*2),fd(20)
                    bande -= 1
            if sens[1] == 'S':        # vers le bas, gauche ou droite, rebond
                if xcor()<=-195:
                    lt(180-angle*2),fd(20)
                    bande -= 1
                elif xcor()>=195:
                    rt(180-angle*2),fd(20)
                    bande -= 1
            if sens[1] == 'N':        # vers le haut, gauche ou droite, rebond
                if xcor()<=-195:
                    rt(180-angle*2),fd(20)
                    bande -= 1
                elif xcor()>=195:
                    lt(180-angle*2),fd(20)
                    bande -= 1
            
                
########################################################################
def test():
    print('Dessiner des polygones convexes')
    print('Q1')
    poly_reg_conv(5)
    print('Q2')
    clearscreen()
    poly_reg_convexe(8,150)
    print('Q3')
    clearscreen()
    figure(7,120)
    print('Dessiner des polygones étoilés')
    print('Q1')
    clearscreen()
    polygone_etoile(10,250,3)
    print('Q2')
    clearscreen()
    figure_etoile(9,125,4)
    print('Mouvement brownien')
    print('Q1-Q2')
    clearscreen()
    tortue_sortie(100,100)
    print('Billard')
    print('Q1-Q2')
    clearscreen()
    billard(0,150,315,12)

test()
mainloop()

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
