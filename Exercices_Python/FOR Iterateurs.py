class RevStr(str):
    """
    renverse le sens de l'itération en parcourant 
    une liste de la fin au début. La chaine reste la même,
    seul l'appel de l'itérateur "for" provoque l'inversion 
    de la chaine. cf fin de script.
    Peut se faire en une seule classe, auquel cas la méthode
    __iter__ doit s'appeler par "self".
    """
    def __iter__(self):
        return ItRevStr(self)

class ItRevStr:
    def __init__(self, chaine_a_parcourir):
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)

    def __next__(self):
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaine_a_parcourir[self.position]

# >>> chaine = RevStr("azerty")
# >>> chaine
# 'azerty'
# >>> for lettre in chaine:
# ...     print(lettre)
# ... 
# y
# t
# r
# e
# z
# a