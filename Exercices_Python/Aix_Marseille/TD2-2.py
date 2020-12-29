""" Exercice 1. Ecrivez une fonction tete_queue(s) qui renvoie une chaîne construite avec les deux
derniers et les deux premiers caractères de s. Si la taille de s est inférieur à 2, renvoie la chaîne
vide"""
def tete_queue(s):
    if len(s)>=2 :
        s = s[-2:]+s[:2]
    else:
        s = ''
    return f"'{s}'"

print(tete_queue('hello')); print(tete_queue('aba')); print(tete_queue('x'))

""" Exercice 2. Ecrivez une fonction affiche_triangle_droite(n) qui affiche un triangle croissant
d’astérisques, alignés à droite. Utilisez les méthodes de formatage."""
def affiche_triangle_droite(n):
    for x in range(1,n+1):
        print(f"{'*'*x:>5}")
    return ''

print(affiche_triangle_droite(5))

""" Exercice 3. Ecrivez une fonction enumerer(liste) qui renvoie une liste de tuples, chacun formé
par un élément de la liste et son indice numérique."""
def enumerer(l):
    return [ (i, val) for i, val in enumerate(l) ]
    
print(enumerer(['bleu', 'jaune', 'vert', 'rouge']), '\n')

""" Exercice 4. Ecrivez une fonction compte_chiffres() qui demande à l’utilisateur d’entrer deux
nombres entiers séparés par une virgule, les multiplie entre eux et affiche le nombre de chiffres du
résultat."""
standard_input = '18, 33'
def compte_chiffres():
    vals = input(f'Entrez 2 chiffres séparés par une virgule: {standard_input}')
    a, b = (vals.split(','))
    a = int(a); b = int(b)
    print(f"{a*b} a {len(str(a*b))} chiffres.",'\n')

compte_chiffres()

""" Exercice 5. Ecrivez une fonction chiffres_zero(nom_fichier) qui lit le contenu d’un fichier
“nom_fichier”, met tous les chiffres à 0 et écrit le résultat dans un deuxième fichier, à rebours à
partir du dernier caractère. Le fichier doit s’appeler “nom_fichier”.res. Par exemple spam.log
→ spam.log.res."""
from os import path
def chiffres_zero(nom_fichier):
    f1 = open(nom_fichier, 'r', encoding='cp1252')
    f2 = open('spam.txt.res', 'w', encoding='cp1252')
    txt_content = ''
    for x in f1:
        for y in x:
            if y.isdigit():
                txt_content += '0'
            else:
                txt_content += y
    reversed_txt = ''.join([x for x in list(txt_content)[::-1]])
    print(reversed_txt, file=f2)
    f2.close()
    f2 = open('spam.txt.res', 'r', encoding='cp1252')
    print('\n', f2.read())

chiffres_zero('spam.txt')
print('\n')

""" Exercice 6. Ecrivez une fonction compte_mots(s) qui compte le nombre d’occurrences de chaque
mots dans la chaînes s et affiche le résultat dans l’ordre alphabétique :"""
from collections import Counter
def compte_mots(s):
    mots = s.split()
    print(mots)
    count = Counter(mots)
    count_list = sorted([(x, y) for x, y in count.items()])
    for x in count_list:
        print(f"{x[0]} : {x[1]}")

compte_mots('le chien poursuit le chat mais le chat est plus rapide')