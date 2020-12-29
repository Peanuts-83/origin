""" Exercice 1. Un vecteur sur le plan cartésien est représenté par un tuple (x, y), où x et y sont
des nombres. Soit vec une liste des vecteurs, par exemple vec = [(-3, 0), (1, 2), (4, -1)].
Triez la liste selon la longueur des vecteurs. Essayez sans et avec expressions lambda.
Rappel : la longueur d’un vecteur de coordonnées (x, y) est √x**2 + y**2
"""

import os#;print(os.getcwd())
from math import sqrt
from operator import attrgetter

def longueur_v(vect):
    x, y = vect
    return sqrt(x**2 + y**2)

vec = [(-3, 0), (1, 2), (4, -1)]
vec1 = sorted(vec, key=lambda x: longueur_v(x))
# vec2 = sorted(vec, key=attrgetter(longueur_v(x))

print('1. vecteurs:', vec, '\ntri par lambda:',vec1)

""" Exercice 2. Triez une liste de chaînes selon le nombre de ’a’ contenu dans chaque chaîne."""
list1 = ['abc', 'abababa', 'bbbbb']; list2 = ['antani', 'cool', 'belazio']

list1.sort(key=lambda x : x.count('a'))
list2.sort(key=lambda x : x.count('a'))
print('\n2.',list1, list2)

""" Exercice 3. Écrivez une fonction pair(...) qui accepte plusieurs nombres en argument 
et renvoie une liste avec les nombres pairs. Si on ne passe pas d’argument, elle renvoie None."""
def pair(*args):
    for x in args:
        if isinstance(x, int):
            return [x for x in args if x%2 == 0]
        else:
            return [y for y in x for x in args if y%2 == 0]

print('\n3.', pair(0,3,5,6,8,15,4,7,12,24,35,64), pair(), pair((3,5,6,8,14,13)))

""" Exercice 4. Écrivez un programme qui demande à l’utilisateur de saisir des nombres séparés par
des espaces, et applique la fonction pair(...) sur la liste des nombres saisis.
"""
standard_input = '2 3 5 6 8 12 19 24'
espaces = input('Enter nums separated by blank spaces:')
print('\n4.', '2 3 5 6 8 12 19 24')
espaces = [int(x) for x in espaces.split(' ')]    
print(pair(espaces))

""" Exercice 5. Écrivez une fonction g(...) qui se comporte de la façon suivante :
>>> g()
hello
>>> g(’salut’)
salut
>>> g(’salut’, john=3)
salut john, salut john, salut john
>>> g(’ciao’, john=2, jack=3)
ciao john, ciao john
ciao jack, ciao jack, ciao jack
La fonction doit marcher pour n’importe quel keyword argument (donc non pas seulement john et
jack).
"""
print('\n5.')
def g(*args, **kwargs):
    if len(args) > 0:
        for x in args:
            if isinstance(x, str):
                val1 = x
    else:
        val1 = 'Hello '
    list_kwargs = []; counter = 0
    if len(kwargs) > 0:
        for val, key in kwargs.items():
            counter += 1
            val2 = str(val)
            key2 = int(key)
            list_kwargs.append((val2, key2))
    else:
        counter = 1
        val2 = ''
        key2 = 1
        list_kwargs.append((val2, key2))
    res = [(val1+' '+val[0]+' ')*val[1] for n, val in enumerate(list_kwargs)]
    for x in res:
        print(x)
    return ''

g(); g('Salut'); g('Salut', john = 3); g('ciao', john=2, jack=3, sally=8)
