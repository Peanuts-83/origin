# -*- coding: utf8 -*-

if __name__ == "__main__":

    # Liste initiale
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print L

    # a)
    for i in range(len(L)):
        L[i] = L[i] + 1
    print "a)", L
    """ Autre solution avec une liste compréhension:
    L = [el+1 for el in L]
    """

    # b)
    L.append(11)
    print "b)", L

    # c)
    L.extend([12, 13])
    print "c)", L

    # d)
    print "d) Premier élément :", L[0]
    print "d) Deux premiers éléments :", L[0:2]
    print "d) Dernier élément :", L[-1]
    print "d) Deux dernier éléments :", L[-2:]

    # e)
    print "e) Éléments paires", [el for el in L if el % 2 == 0]
    print "e) Éléments impaires", [el for el in L if el % 2 == 1]

    # f)
    L = L[0:4] + [3.5] + L[4:]
    # autre solution: L.insert(4, 3.5)
    print "f)", L

    # g)
    L = L[0:3] + L[4:]
    # autre solution: L.remove(3.5)
    print "g)", L

    # h)
    L.reverse()
    print "h)", L

    # i)
    nombre = int(raw_input('Donnez un nombre au hasard : '))
    if nombre in L:
        print "%d est dans L." % nombre
    else:
        print "%d n'est pas dans L." % nombre

