#!/usr/bin/env python3
import os
import turtle

# print(os.getcwd())
os.chdir('G:/ReCONVERSION Tom/PYTHON/Exercices/Turtle/TP4')
turtle.title('TP4 - Key press')
turtle.setup(640, 480, 50, 50)
turtle.bgcolor('grey')
# turtle.speed('fast')

# interragir avec user
def appui_a():
    print("Touche 'a' pressée.")

def relache_a():
    print("Touche 'a' relachée...")

def appui_autre():
    print("Autre touche pressée!")


# turtle.exitonclick()

if __name__ == "__main__":
    turtle.listen()
    turtle.onkeypress(appui_autre)
    turtle.onkeypress(appui_a, 'a')
    turtle.onkeyrelease(relache_a, 'a')
    turtle.mainloop()
