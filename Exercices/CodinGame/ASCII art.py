import sys
import math

l = int(input())
h = int(input())
t = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
for i in range(h):
    row = input()
    result += (row[alphabet.index(t)*4 : (alphabet.index(t)*4)+4] + '\n')

print(result)
