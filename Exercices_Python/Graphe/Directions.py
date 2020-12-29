graphe = [
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','*','.','C','.','.'],
    ['.','.','T','.','.','*','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.']
]

# situer T(Départ) et A(Arrivée)
for line in graphe:
    if 'C' in line:
        C = (graphe.index(line), line.index('C'))
        print('C = ',C)
    if 'T' in line:
        T = (graphe.index(line), line.index('T'))
        # graphe[T[0]][T[1]] = 0
        print('T = ',T)
for x in graphe:
    print(x)



# construction des valeurs du graphe
for l in range(len(graphe)):
    wall = 0
    for c in range(len(graphe[0])):
        if graphe[l][c] != '*':
            graphe[l][c] = abs(T[0]-c) + abs(T[1]-l) + wall
        else:
            wall += 2 
print('valeurs:')
for x in graphe:
    print(x)

# choix du chemin / de la cible(8) au départ(0)
path = []
path.append(C)
target = path[-1]
for n in range(graphe[C[0]][C[1]]-1, -1, -1):                           # range(8) num looking for
    for c in range(len(graphe[0])):                                     # range(10) cols
        for l in range(len(graphe)):                                    # range(6) lines
            if (l == target[0]+1 or l == target[0]-1) and c == target[1] and n == graphe[l][c]:         # lines up or down
                path.append((l, c))
                target = path[-1]
                break
            elif l == target[0] and (c == target[1]-1 or c == target[1]+1) and n == graphe[l][c]:       # line
                path.append((l, c))
                target = path[-1]
                break
path.pop(0)
print('Path:',path)

def trad_dir(path):
    global C
    if C[0] == path[0]:
        dir = 'LEFT' if C[1] > path[1] else 'RIGHT'
        C = path
        print(C)
        return dir
    if C[1] == path[1]:
        dir = 'UP' if C[0] > path[0] else 'DOWN'
        C = path
        print(C)
        return dir

# Renvoi des valeurs dans l'ordre
for _ in range(len(path)):
    print(trad_dir(path.pop(0)))
