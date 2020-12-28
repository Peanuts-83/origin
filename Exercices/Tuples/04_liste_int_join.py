# -*-coding:latin-1 -*
#import os # On importe le module os


a = int(input('val_a : '))
b = int(input('val_b : '))
ind = b-a+1
liste = []
n = 0

while n < ind:
    liste.append(n)
    n += 1

liste = [n for n in liste if n%3 == 0 and n%5 ==0]
print(liste)

somme = 0
for n in liste:
    somme = somme + n

addition = '+'.join([str(_) for _ in liste])
print(addition, '=',somme)
print('somme des nbres =',somme)




# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
