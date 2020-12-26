points = [input().split() for _ in range(int(input()))]
for i, (x, y) in enumerate(points):
    if y == points[i+1][1]:
        start, end, alt = int(x), int(points[i+1][0]), int(y)
        mid = (start + end) / 2
        break

while 1:
    x, y, h_speed, v_speed, *_ = [int(i) for i in input().split()]
    power = 4
    rotate = -20 if x < mid else 20
    if v_speed > 0:
        power = 0
    if abs(h_speed) > 80:
        rotate *= -1
    if abs(x - mid) < 1300:
        if abs(h_speed) > 10:
            rotate = 60 if h_speed > 0 else -60
        else:
            rotate = 0
            if v_speed < -36:
                power = 4
            else:
                power = 0
        if y - alt < 90:
            rotate = 0

    print(rotate, power)
