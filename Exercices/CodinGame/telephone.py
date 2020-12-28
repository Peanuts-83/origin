import sys
import math

n = int(input())
liste = [input() for _ in range(n)]
cell_memory = [liste[0]]

if n > 1:
    for a in range(1,n):
        for b in range(len(liste[a])):
            if liste[a][:b+1] != liste[a-1][:b+1]:
                cell_memory.append(liste[a][b:])
                break

length = 0
for n in range(len(cell_memory)):
    length += len(cell_memory[n])

print(length)