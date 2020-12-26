import sys
import math

n = int(input())  # the number of temperatures to analyse
temp = input()  # the temperatures values
if n != 0:
    t_temp = int(temp.split()[0])   # first value of str(temp) used for recursive comparaison
    if n == len(temp.split()):
        for i in temp.split():
            # t: a temperature expressed as an integer ranging from -273 to 5526
            t = int(i)
            if abs(t) < abs(t_temp):
                t_temp = t
            elif abs(t) == abs(t_temp):
                if t > 0 and t_temp < 0:
                    t_temp = t
                else:
                    t_temp = t_temp
    else:
        t_temp = 'Le nombre de températures ne correspondt pas à la liste.'
else:
    t_temp = 0

# n       = int(input())  # the number of temperatures to analyse
# temps   = input()  # the n temperatures expressed as integers ranging from -273 to 5526
# print(min(temps.split(' '), key = lambda x: abs(int(x) - .1)) if n else 0)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(t_temp)


