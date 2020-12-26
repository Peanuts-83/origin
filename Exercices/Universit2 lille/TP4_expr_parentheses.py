#-*-coding:latin-1 -*-
#import os # On importe le module os

############### TP string - parenthèses ################

#1/ conditions
##nbr ( == nbr )
##nbr ( >= nbr )
##premiere parenthese doit etre (
##derniere parenthese doit etre )

#2/ f° de vérification des parenthèses
def bien_parenthesee(s):
    if s.count('(') == s.count(')') and s[0] == '(' and s[len(s)-1] == ')':
        ouv = 0
        fer = 0
        for i in s:
            if i == '(':
                ouv += 1
            elif i == ')':
                fer += 1
                if ouv < fer :
                    return False
        return True
    else:
        return False

#3/ calcul du nombre de facteurs d'une expression
def nbre_facteurs(s):
    ouv = 0
    fer = 0
    facteurs = 0
    for i in s:
        if i == '(':
            ouv += 1
        elif i == ')':
            fer += 1
        if ouv == fer:
            facteurs = facteurs + 1
            ouv = 0
            fer = 0
    print('nbre de facteurs : ',facteurs)
    return facteurs

#4/ affichage des facteurs séparés par *
def affiche_facteurs(s):
    ouv = 0
    fer = 0
    n = 0
    facteurs = 0
    affiche = ''
    for i in s:
        n += 1
        if i == '(':
            affiche = affiche + '('
            ouv += 1
        elif i == ')':
            affiche = affiche + ')'
            fer += 1
        if ouv == fer:
            if n < len(s):
                affiche = affiche + '*'
            facteurs = facteurs + 1
            ouv = 0
            fer = 0
    print('affiche facteurs : ',affiche)
    return affiche


    


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
