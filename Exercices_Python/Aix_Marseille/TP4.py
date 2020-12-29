#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Exercice 1. Une liste vous est donnée, qui contient des noms de personne complets, par exemple :
>>> liste = [’Jean Mollet’, ’Marie Curie’, ’Louise Ducray’]
Écrivez la fonction trie(l) qui permet de trier une telle liste par nom de famille :
"""
def trie(l):
    return sorted(l, key=lambda x : x.split()[1])

print(trie(['Jean Mollet', 'Marie Curie', 'Louise Ducray']))

"""Exercice 2. Supposons d’avoir une fonction frobnicate(...) qui prend en arguments des nombres
et renvoie le résultat d’un certain calcul sur ces nombres. Écrivez une fonction fiddle(...) qui
accepte des nombres quelconques (entiers, flottants, ...) et renvoie le résultat de frobnicate()
appliquée à la partie entière de ses arguments. Par exemple fiddle(1.1, 2.3, 3.9) doit donner
le même résultat de frobnicate(1, 2, 3)."""
import math
def frobnicate(*args):
    if isinstance(args[0], tuple):
        return sum(args[0])
    else:
        return sum(args)

def fiddle(*args):
    res = tuple()
    for x in args:
        res += (int(x),)
    return frobnicate(res)

print(frobnicate(4,8,3,1,7,2))
print(fiddle(5.2,3.8,2.1))

