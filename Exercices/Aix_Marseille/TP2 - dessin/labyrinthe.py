from turtle import *

speed(12)
up(), goto(0,0), down(),
for n in range(15):
    if n > 0:
        fd(10*n), lt(90), fd(10*n), lt(90)
done()
