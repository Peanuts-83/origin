from turtle import *
speed(12)

def etoile(longueur,pointes):
    for n in range(pointes):
        forward(longueur)
        rt(180-(180/pointes))
 
up(),goto(0,0),down()
etoile(80,5)




done()