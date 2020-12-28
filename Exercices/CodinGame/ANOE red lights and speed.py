import sys
import math

speed = int(input())
light_count = int(input())
liste_feux = []                            # list of green lights' distance and timing in tuples
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    liste_feux.append((distance,duration))
max_speed = int()           # maxspeed returned finaly
temp_speed = int()          # speed evaluated
bing = 0                    # validate series of green lights

for i in range(speed+1):
    if i > 0:
        speed_m_sec = (i)*1000/3600
        for n in range(light_count):
            distance = liste_feux[n][0]         # accessing liste for distance values
            duration = liste_feux[n][1]         # accessing liste for duration values
            tempo = round(distance/speed_m_sec)/duration        # tempo for green/red light // round important!
            if int(tempo)%2 == 0 and temp_speed <= i:           # speed ok for green light?
                temp_speed = i
                bing += 1                                       # bing == light_count for validate
            # if i == 60:                                       # test module
                # print(i, tempo,distance/speed_m_sec, bing)
        if bing != light_count:
            bing = 0
        elif bing == light_count:
            max_speed = temp_speed
            bing = 0
        
print(max_speed)
