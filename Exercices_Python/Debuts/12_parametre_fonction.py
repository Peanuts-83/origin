# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

# parametre de fonction libre en *z (autant qu'on veux!)
def fonction(a, b, *z):
    print(a, b, z)
    
print(fonction('non', 'non', 'oui', 'peut-', 'etre'))

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
