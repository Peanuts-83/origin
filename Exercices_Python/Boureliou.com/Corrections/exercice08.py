# -*- coding: utf8 -*-

def nbOccurrences(caractere, phrase):
    """ Retourne le nombre de fois où "caractere" est présent dans "phrase".

    >>> from exercice8 import nbOccurrences
    >>> nbOccurrences('e', "Combien y a-t-il de e dans cette phrase ?")
    6
    """

    cpt = 0

    for c in phrase:
        if c == caractere:
            cpt += 1

    return cpt


# Version plus compacte et plus pythonique !
def nbOccurrences2(caractere, phrase):
    """ Retourne le nombre de fois où "caractere" est présent dans "phrase".

    >>> from exercice8 import nbOccurrences
    >>> nbOccurrences('e', "Combien y a-t-il de e dans cette phrase ?")
    6
    """
    return sum([1 for c in phrase if c == caractere])
