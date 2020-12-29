#!/usr/bin/python3
import os
""" Exercice 2. Supposons que le dossier courant contient des fichiers textuels numérotés avec trois
chiffres, nommés par exemple 002-spam.txt, 013-eggs.txt, 425-systemlog.txt, 099-blabla.txt,
etc. Écrivez un programme renommeur.py qui renomme tous les fichiers en décrémentant le nombre
d’une unité :"""
import re
files = ['002.txt', '013-egg.txt', '014_balalala.txt']
for f in files:
    with open(f, 'r', utf-8) as f:
        a = str(f.name)
        a_digit = ''.join(re.findall("\d+", a))
        a_digit_new = (len(a_digit), int(a_digit)-1)
        a_digit_new = '0'*(a_digit_new[0] - len(str(a_digit_new[1]))) + str(a_digit_new[1])
        a = a.replace(''.join(re.findall("\d+", a)), a_digit_new, 1)
        print(a)
        with open(a, 'w') as new_file:
            new_file.write(f.read())


os.system("pause")

