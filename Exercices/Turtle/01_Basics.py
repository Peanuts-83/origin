#-*-coding:latin-1 -*-
#import os # On importe le module os

from turtle import *

def carre(l):
    color('black')
    for i in range(4):
        forward(l),right(90)
    

def dix_carres(l):
    speed(20)
    pu(),lt(180),fd((l+5)*5),rt(180),pd()
    for i in range(10):
        carre(l)
        penup(),fd(l+5),pendown()
        
def cent_carres(l):
    speed(20)
    depl = (l+5)*5
    depl_v = l+5
    pu(),goto(0,0),lt(90),fd(depl),rt(90),pd()
    for i in range(10):
        dix_carres(l)
        pu(),lt(180),fd(depl),lt(90),fd(depl_v),lt(90),pd()

def coin(n):
    speed(20)
    l=20
    pu(),goto(-250,-250),pd()
    for i in range(n):
        carre(l)
        pu(),lt(90),fd(10),rt(90),pd()
        l=l+10

def carre_tournant(n):
    speed(20)
    l = 100
    pu(),goto(0,0),pd()
    for i in range(n):
        carre(l)
        lt(360/n)




########################################################################
def test():
    print('Dessiner avec des carrés')
    print('Q1')
    carre(100)
    print('Q2')
    clearscreen()
    dix_carres(100)
    print('Q3')
    clearscreen()
    cent_carres(50)
    print('Q4')
    clearscreen()
    coin(50)
    print('Q5')
    clearscreen()
    carre_tournant(18)

test()
mainloop()

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
