# -*-coding:latin-1 -*
#import os # On importe le module os

nom = input('Nom? ')
sexe = input('Sexe (M ou F)? ')

if sexe == 'M':
    print(f'Bonjour Mr {nom}.')
elif sexe == 'F':
    print(f'Bonjour Mme {nom}.')
else:
    print('entrer sexe valide.')
    

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
