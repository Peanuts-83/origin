
#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP1')
turtle.title('Ma super fenêtre')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('yellow')
turtle.bgpic('img.png')
print(turtle.bgpic())
turtle.exitonclick()