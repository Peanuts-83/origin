#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP4')
turtle.title('TP4 - timer')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('grey')
# turtle.speed('fast')

# timer
def affiche_temps():
    turtle.clear()
    turtle.write(f"Le temps passe depuis {sec//1000} secondes.",align= 'center', font= ('Arial', 18, 'bold'))
    
def increment_temps():
    global sec
    sec += 1000
    affiche_temps()
    turtle.ontimer(increment_temps, 1000)


if __name__ == "__main__":
    sec = 0
    turtle.hideturtle()
    affiche_temps()
    turtle.ontimer(increment_temps, 1000)
    turtle.exitonclick()