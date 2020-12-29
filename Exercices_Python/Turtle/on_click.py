
#!/usr/bin/env python3
import os
import turtle

crayon_clique, crayon_relache = turtle.Turtle(), turtle.Turtle()
crayons = { 'pink' : crayon_clique, 'grey' : crayon_relache }
pos = [-75, 0]
for clef, valeur in crayons.items():
    valeur.color(clef, clef)
    valeur.shapesize(7, 7)
    valeur.up(); valeur.goto(pos); valeur.down(); pos[0] += 150
crayon_clique.onclick(lambda x, y: print("cliqué !"))
crayon_relache.onrelease(lambda x, y: print("relâché !"))

