# -*-coding:latin-1 -*
import os # On importe le module os

liste=[17,38,10,25,72]
print(liste)


liste.sort()
print('1/ tri liste : ', liste)

liste.append(12)
print('2/ ajout 12 : ', liste)

liste.sort(reverse=True)
print('3/ tri inverse : ', liste)


print('4/ index chiffre 17 : ', liste.index(17))

liste.remove(38)
print('5/ 38 supprimé : ', liste)

print('6/ sous liste du 2e au 3e elt : ', liste[1:3])

print('7/ sous liste du debut au 2e elt : ', liste[:2])

print('8/ sous liste du 3e à la fin : ', liste[2:])

print('9/ sous liste complete : ', liste[0:])

print('10/ dernier elt avec indice neg : ', liste[-1:])



    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
