#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP4')
turtle.title('TP4 - boule')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('light yellow')
# turtle.speed('fast')

# dirriger une boule
def deplacer_sans_tracer(x, y = None):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def affiche(diam, coul):
    deplacer_sans_tracer(pos_x, pos_y)
    turtle.clear()
    turtle.dot(diam, coul)
    turtle.write(pos_x, True , font=('Arial', 15, 'bold'))
    turtle.write(' / ', True , font=('Arial', 15, 'bold'))
    turtle.write(pos_y, True , font=('Arial', 15, 'bold'))
    

def deplace_x(num = 0):
    global pos_x
    if -310 < pos_x + num < 310:
        pos_x += num
    else:
        pos_x = -pos_x
    affiche(diam, coul)

def deplace_y(num = 0):
    global pos_y
    if -230 < pos_y < 230:
        pos_y += num
    else:
        pos_y = -pos_y
    affiche(diam, coul)

def reloading():
    global pos_x, pos_y
    pos_x, pos_y = 0, 0
    affiche(diam, coul)


# turtle.exitonclick()

if __name__ == "__main__":
    turtle.speed(0)
    pos_x, pos_y = 0, 0
    diam, coul = 20, 'red'
    turtle.hideturtle()
    affiche(diam, coul)

    turtle.listen()
    turtle.onkeypress(lambda : deplace_x(10), 'Right')
    turtle.onkeypress(lambda : deplace_x(-10), 'Left')
    turtle.onkeypress(lambda : deplace_y(10), 'Up')
    turtle.onkeypress(lambda : deplace_y(-10), 'Down')
    turtle.onkeyrelease(reloading, 'space')
    turtle.mainloop()
