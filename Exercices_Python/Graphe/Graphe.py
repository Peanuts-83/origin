graphe = [
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','*','.','A','.','.'],
    ['.','.','T','.','.','*','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.']
]

# situer T(Départ) et A(Arrivée)
for line in graphe:
    if 'A' in line:
        A = (graphe.index(line), line.index('A'))
        print('A = ',A)
    if 'T' in line:
        T = (graphe.index(line), line.index('T'))
        graphe[T[0]][T[1]] = 0
        print('T = ',T)
print('graphe:', graphe)

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
path.append(A)
target = path[-1]
print(path, target)
for n in range(graphe[A[0]][A[1]]-1, -1, -1):                           # range(8) num looking for
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
print('Path:',path)

# Renvoi des valeurs dans l'ordre
for _ in range(len(path)):
    print(path.pop())
