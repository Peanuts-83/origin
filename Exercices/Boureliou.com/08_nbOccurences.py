# -*-coding:latin-1 -*
import os # On importe le module os

def nbOccurences(lettre, phrase):
    print(f'il y a {phrase.count(lettre)} "{lettre}" dans la phrase "{phrase}"')

nbOccurences('e', 'Return a copy where all tab characters are expanded using spaces')
    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
