"""Exercice 3. Créez un programme jeudupendu.py qui implémente le fameux Jeu du Pendu :
le programme choisit un mot « secret » et communique au joueur sa longueur (par moyen d’une
séquence de tirets bas). Le joueur essaie de deviner les lettres du mot : si la lettre est présente, toutes
les positions correspondantes seront affichées ; sinon, la figure d’un pendu est progressivement
dessinée.
Vous pouvez procéder par étapes, en écrivant différentes versions du programme, qui améliorent
progressivement le jeu. Par exemple, on pourrait procéder selon les étapes suivantes :
(a) Le programme est purement textuel et utilise un mot fixé (ou un mot passé en argument du
script) comme mot secret. À ce stade, la « figure » du pendu sera simplement une séquence
d’astérisques.
(b) Le programme dessine le pendu à l’aide du module turtle, mais le reste de l’interface est
encore textuelle.
(c) Le mot sera choisi au hasard parmi une liste (vous pouvez télécharger une telle liste à l’adresse
http://pageperso.lif.univ-mrs.fr/~stefano.facchini/python/mots.txt).
(d) Toute l’interface est programmée avec turtle (pour l’affichage du texte et la capture des
touches du clavier, étudiez les fonction write() et onkey() du module).
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, re, turtle
# import TP4_pendu_turtle as t

class Pendu(object):
    def __iter__(self):
        yield turtle.forward(50); turtle.backward(25); turtle.left(90)
        yield turtle.forward(200); turtle.left(90)
        yield turtle.forward(100); turtle.left(90)
        yield turtle.forward(20); turtle.right(90)
        yield 
        for _ in range(27): 
            turtle.forward(5); turtle.left(360/18)
        turtle.right(90)
        yield turtle.forward(60); turtle.backward(50); turtle.left(90)
        yield turtle.forward(40); turtle.backward(40); turtle.left(180)
        yield turtle.forward(40); turtle.backward(40); turtle.left(90); turtle.forward(50); turtle.left(60)
        yield turtle.forward(60); turtle.backward(60); turtle.right(120)
        yield turtle.forward(60); turtle.backward(60); turtle.left(60)
        yield turtle.forward(20); turtle.backward(20)
        for _ in range(8):
            turtle.forward(3); turtle.left(360/8)
        for _ in range(8):
            turtle.forward(3); turtle.right(360/8)
        


mot_secret = 'papa'
mot = '*' * len(mot_secret)
gen = iter(Pendu())
# for x in pendu():
#     print(x)
chance = 0

while chance < 12:
    turtle.write(mot, font = ('Arial', 15, 'bold'))
    query = turtle.textinput('Choix lettre:', 'Veuillez choisir une lettre')
    mot = ''.join([x if x==query else mot[mot_secret.index(x)] for x in mot_secret])
    chance += 1
    gen.next()
    if '*' not in mot:
        turtle.write(mot)
        turtle.write('gagné!')
        break




os.system("pause")