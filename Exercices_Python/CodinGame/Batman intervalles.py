import sys
import math
# from interval import interval >>> would be cool with this!

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x_zone = [i for i in range(w)]                        # active zone w
y_zone = [i for i in range(h)]                        # active zone h


# game loop
while True: 
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    directions = {'U' : [y0,h], 'D' : [0,y0], 'R' : [0,x0], 'L' : [x0,w]}   # forms : zone to substract f° to direction
    for i in bomb_dir:
        di = directions[i]
        retrait = [n for n in range(di[0], di[1]+1)]            # zone to substract
        if i in ('U','D'):                                      # if Up or Down
            y_zone = [n for n in y_zone if n not in retrait]
        elif i in ('R','L'):                                    # if Right or Left
            x_zone = [n for n in x_zone if n not in retrait]
    
    x0 = sum(x_zone)//len(x_zone)
    y0 = sum(y_zone)//len(y_zone)
    # the location of the next window Batman should jump to.
    print(x0,y0)