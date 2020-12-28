import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over. Why do we need it?
# x0, y0: Batman's position.
x0, y0 = [int(i) for i in input().split()]

# initial ranges for the jump.
x_min, x_max, y_min, y_max = [0, w, 0, h]

# game loop
while True:
    bomb_dir = input()

    # Get new ranges for the jump.
    x_min, x_max, y_min, y_max = {
        'U': [x0, x0, y_min, y0],
        'D': [x0, x0, y0, y_max],
        'L': [x_min, x0, y0, y0],
        'R': [x0, x_max, y0, y0],
        'UL': [x_min, x0, y_min, y0],
        'UR': [x0, x_max, y_min, y0],
        'DL': [x_min, x0, y0, y_max],
        'DR': [x0, x_max, y0, y_max]
    }[bomb_dir]

    x0 = math.floor((x_min + x_max)/2)
    y0 = math.floor((y_min + y_max)/2)

    print(f'{x0} {y0}')