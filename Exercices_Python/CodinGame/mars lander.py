import sys
import math
# tribute to Pouf for the surface_pt fonctions!

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface_pt = [input().split() for _ in range(surface_n)]
for i, (x, y) in enumerate(surface_pt):
    if y == surface_pt[i+1][1]:
        land, length = ((int(x) + int(surface_pt[i+1][0]))//2, int(y)), int(surface_pt[i+1][0]) - int(x)
        break

gravity = 3.711                                         # abs val for martian gravity
angle_static_v = 21                   # angle with no loss of altitude

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    print(land,x-land[0],'length',length,'vspeed',v_speed,'h_speed',h_speed,'distx',x-land[0],'disty',y-land[1],'x',x,'y',y, file=sys.stderr, flush=True)
    
    if y-land[1] < 600:             # flying low
        if x-land[0] < length:      # close landing zone
            print('else', file=sys.stderr, flush=True)
            if v_speed < -20 or abs(h_speed) > 20:
                power = 4
                pass
            elif abs(x-land[0]) > length//2:
                power = 4
                pass
            else:
                power = 2
                pass

        elif v_speed < 0:           # far away on x axis
            power = 4
        else:
            power = 3
    else:                           # flying high
        if v_speed < -20 or abs(h_speed) > 40:
            power = 4
        else:
            power = 3

    if abs(x-land[0]) > length:         # far away on x axis
        if h_speed >= 50:               # slow down speed
            rotate = 42
        elif h_speed <= -50:
            rotate = -42
        else:                           # accelerate if speed == 0
            rotate = min(round(42*(((x-land[0]))/length)+h_speed//2), 21)
    else:                               # go to center of landing zone
        rotate = round(42*(((x-land[0]))/length)+h_speed//2)
        if y-land[1] < 50:              # lander straight for touch down
            rotate = 0
       
    print(rotate, power)
    