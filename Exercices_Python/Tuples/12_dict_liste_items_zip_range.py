# -*-coding:latin-1 -*
#import os # On importe le module os

liste = [('a',1),('b',2),('c',3)]
print(liste)
d = dict(liste)
print('passe liste en dictionnaire :',d)
nbr_d = d.items()
print('passe dictionnaire en liste :',d.items())
for paire in nbr_d:
    print(paire)
for a,b in nbr_d:
    print(a,b)

d2 = dict(zip('abc', range(3)))
print(d2)
liste2 = list(zip('rty', range(4,7)))
print(liste2)
d2.update(liste2)
print(d2)




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
