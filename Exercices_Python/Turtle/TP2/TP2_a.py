
#!/usr/bin/env python3
import os
from turtle import *

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP2')
title('TP2- exo 1')
setup(640, 480, 50, 50)
bgcolor('light grey')


# 1st square
up(); goto(-50, 50); down()
for _ in range(4): fd(100); right(90)
#2nd square 
up(); goto(-75, 75); down()
for _ in range(4): fd(150); right(90)
# big circle
up(); goto(0, -110); down(); circle(110)
# tiny circles
up(); home(); ang = 22.5
for _ in range(8):
    up(); right(ang); fd(150); down(); dot(30, 'red')
    up(); home(); down()
    ang += 45
exitonclick()