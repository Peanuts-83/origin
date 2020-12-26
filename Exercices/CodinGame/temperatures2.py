import sys
import math


n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
print(min(temps.split(' '), key = lambda x: abs(int(x) - .1)) if n else 0)

