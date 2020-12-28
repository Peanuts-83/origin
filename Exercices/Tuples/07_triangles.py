# -*-coding:latin-1 -*
#import os # On importe le module os

while 1:
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    liste = [a,b,c]
    liste.sort(reverse=True)
    print(liste)
    v0 = liste[0]
    v1 = liste[1]
    v2 = liste[2]
    print(v0,v1,v2)
    if v0 < v1 + v2:
        if v1 == v2 or v0 == v1:
            if v0**2 == v1**2 + v2**2:
                print('triangle isocele rectangle')
            else:
                print('triangle isocele')
        elif v0 == v1 and v0 == v2:
            print('triangle equilateral')
        elif v0**2 == v1**2 + v2**2:
            print('triangle isocele rectangle')
        else:
            print('triangle simple')
    else:
        print('Données non valide.')




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
