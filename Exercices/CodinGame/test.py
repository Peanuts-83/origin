import sys
import math
from random import *

r, c, a = [int(i) for i in input().split()]
back_road = []      # good route for going back
back = 0            # road closed, go back!
closed = []         # tries unfortunates!
cross = []          # crossroad to go back to

def limits(kr,kc):
    limit_r = (max(0, kr-1), min(r, kr+1))
    limit_c = (max(0, kc-1), min(c, kc+1))
    print(limit_r, limit_c, file=sys.stderr, flush=True)
    return limit_r, limit_c

def direction(row,kr,kc):
    l_r, l_c = limits(kr,kc)
    dirs = set()
    for a in range(l_r[0], l_r[1]+1):
        if '.' in row[a][kc]:
            dirs.add((a,kc))
    for b in range(l_c[0], l_c[1]+1):
        if '.' in row[kr][b]:
            dirs.add((kr,b))
    print('dirs',dirs,'back_road',back_road, file=sys.stderr, flush=True)
    dirs = list(dirs)
    dirs = [a for a in dirs if a not in back_road]
    print('dirs',dirs,'back_road',back_road, file=sys.stderr, flush=True)
    return dirs

def choice_dir(move,kr,kc):
    dir_r = move[0] - kr ; dir_c = move[1] - kc
    move_ord = 'DOWN' if dir_r > 0 else 'UP'
    move_ord = 'RIGHT' if dir_c > 0 else 'LEFT'
    return move_ord

def pos_C(row):
    commande_room = [(a, b) for a in row[a] for b in row[a][b+1] if 'C' in row[a] and 'C' in row[a][b]]
    pr, pc = commande_room[0], commande_room[1]
    return pr, pc

# def path_to_C(row,kr,kc,dirs):


while True:
    kr, kc = [int(i) for i in input().split()]
    row = [input() for _ in range(r)]  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
    print(r,c,a,'kirk',kr,kc, file=sys.stderr, flush=True)
    print(row, file=sys.stderr, flush=True)

    if back == 1:
        back_road.reverse()
        for _ in rnage(len(back_road)):
            print(choice_dir(back_road[i],kr,kc))
    else:
        pass

    dirs = direction(row,kr,kc)
    if 'C' not in row:
        if len(dirs) > 1:
            n = choice([i for i in range(len(dirs))])
            move = dirs[n]
            back_road.append(dirs[0])
        else:
            move = dirs[0]
            back_road.append(dirs[0])
    elif 'C' in row:                                    ## creer def detection C in range(len(row))
        cr,cc = pos_C(row)
        print(cr,cr, file=sys.stderr, flush=True)
        if (kr,kc) == (cr, cc):
            back = 1
            break
        # elif len(dirs) > 1:
        #     n = path_to_C(row,kr,kc,dirs)

        #     move = dirs[n]
        #     back_road.append(dirs[0])
        else:
            move = dirs[0]
            back_road.append(dirs[0])

    move_ord = choice_dir(move,kr,kc)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(move_ord)
