#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP4')
turtle.title('TP4 - allumettes')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('light blue')
# turtle.speed('fast')

class Joueur:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name}"


# allumettes
def pos(x, y):
    turtle.up(); turtle.goto(x, y); turtle.down()

def affiche(txt, col = '#cc6600'):
    turtle.clear()
    turtle.color(col)
    turtle.write(txt, align= 'center', font= ('ISOCPEUR', 18, 'bold'))

def call_joueur():
    j1 = turtle.textinput('nom joueur', 'Nommez le joueur 1:')
    j1 = Joueur(j1)
    j2 = turtle.textinput('nom joueur', 'Nommez le joueur 2:')
    j2 = Joueur(j2)
    return j1, j2

def whos_turn():
    global turn
    if turn == 1: turn = 2; pos(0, 100); affiche(f"C'est à {j2} de jouer."); jeu(allumettes)
    else: turn = 1; pos(0, 100); affiche(f"C'est à {j1} de jouer."); jeu(allumettes)

def choice(num):
    global allumettes
    allumettes -= num
    jeu(allumettes)
    if turn == 1:
        if allumettes <= 0:
            pos(0, -100)
            affiche(f"{j1} a gagné!", 'blue')
        else:
            whos_turn()
    else:
        if allumettes <= 0:
            pos(0, -100)
            affiche(f"{j2} a gagné!", 'red')
        else:
            whos_turn()

def allum():
    turtle.pensize(4); turtle.pencolor('red'); turtle.fd(10)
    turtle.pencolor('pink'); turtle.fd(90)

def jeu(nbr_allum):
    pos(-300, 100)
    depart = -300
    turtle.right(90)
    for x in range(nbr_allum):
        allum()
        depart += 20
        pos(depart, 100)

if __name__ == "__main__":
    turtle.hideturtle()
    pos(0, 100)
    turtle.ontimer(affiche("Bienvenu(e) au jeu des allumettes."), 2000)
    turtle.ontimer(affiche("                   Il y a 19 allumettes, \nchoisissez en 1, 2 ou 3 avec les touches 'a', 'z' et 'e'."), 3000)
    j1, j2 = call_joueur()
    allumettes = 19
    jeu(allumettes)
    turn = 2
    

    turtle.listen()
    whos_turn()
    turtle.onkeypress(lambda : choice(1) , 'a')
    turtle.onkeypress(lambda : choice(2) , 'z')
    turtle.onkeypress(lambda : choice(3) , 'e')
    
    
    turtle.exitonclick()
    # turtle.mainloop()