
#!/usr/bin/env python3
import os
from turtle import *

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP2')
title('TP2- exo 2')
setup(640, 480, 50, 50)
bgcolor('light grey')
speed('fast')

# stamp circle
spacer = 0
for _ in range(50):
    up()
    circle(spacer *spacer*0.1, spacer)
    down()
    stamp()
    spacer += 1

exitonclick()