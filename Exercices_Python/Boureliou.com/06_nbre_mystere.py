# -*-coding:latin-1 -*
import os # On importe le module os


from random import randint

var = randint(0, 100)
user = input('Choisir un nbre entre 0 et 100 : ')

while user != var:
    
    user = int(user)
    if user > var:
        print('le nbre est plus petit')
        user = input('Choisir un nbre entre 0 et 100 : ')
    elif user < var:
        print('le nbre est plus grand')
        user = input('Choisir un nbre entre 0 et 100 : ')
    else:
        break

print('Bravo, vous avez trouvé!'.center(50, '#'))



    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
