#!/usr/bin/python3
import os
"""Exercice 1. Écrivez un programme taillefichier.py. Si le programme est exécuté sans arguments, 
il affiche un message d’erreur et termine avec exit code 1. Sinon, il suppose que chaque
argument est un nom de fichier et affiche pour chacun sa taille en Ko.
Rappel. La première ligne du programme doit être #!/usr/bin/python3. N’oubliez pas de changer
les droits d’exécution avec la commande Unix :
$ chmod +x taillefichier.py"""


def taillefichier(*args):
    try:
        for name_file in args:
            print(name_file, ':', os.stat(name_file).st_size, 'Octets.')
    except FileNotFoundError:
        print(name_file, ': Fichier introuvable.')

if __name__ == "__main__":
    import sys
    try:
        if len(sys.argv[1]) > 0:
            x = sys.argv[1:]
            for n in x:
                taillefichier(n)
    except IndexError:
        print('Erreur ! Aucun fichier spécifié.')

os.system("pause")

