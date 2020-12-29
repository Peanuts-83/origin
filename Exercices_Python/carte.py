
# jeu = Jeu52Cartes()
# str(jeu)
# jeu.melanger()
# str(jeu)
# carte = jeu.piocher()
# carte = Carte('As', 'coeur')
# main = [jeu.piocher() for i in range(7)]
############################

from random import shuffle

VALEURS = "2 3 4 5 6 7 8 9 10 Valet Dame Roi As".split()
ENSEIGNES = "Coeur Carreau Trèfle Pique".split()
COULEURS = {"Coeur":"rouge","Carreau":"rouge","Pique":"noir","Trèfle":"noir"}


class Carte:
    """
        Classe représentant une carte (à jouer), avec une valeur et une enseigne.

        La valeur d'une carte représente sa "force" au sein d'une enseigne
        (2, 3, 8, valet, dame, roi, as...). Son enseigne est la suite à
        laquelle elle appartient (pique, coeur, carreau, trèfle). Sa couleur
        (rouge ou noir) dépend de son enseigne.

        Note : pour éviter la confusion dans notre code, le nom "couleur"
        définit strictement une carte rouge ou noire. Le nom "enseigne"
        désigne la suite à laquelle la carte appartient (aussi appelée
        couleur dans de nombreux jeux).

        Pour construire une carte, donnez en argument sa valeur et son
        enseigne (toutes deux sous la forme de str). Par exemple :

        >>> carte = Carte("3", "carreau")

        (Si la valeur ou l'enseigne n'existe pas, une exception ValueError
        est levée).
    """
    def __init__(self, valeur, enseigne):
        if valeur not in VALEURS:
            raise ValueError('Mauvaise valeur entrée.')
        if enseigne not in ENSEIGNES:
            raise ValueError('Mauvaise enseigne entrée.')
        self.valeur = valeur
        self.enseigne = enseigne
        

    @property
    def couleur(self):                  # couleur selon l'enseigne
        return COULEURS[self.enseigne]

    def __repr__(self):
        return f"{self.valeur} de {self.enseigne}"

    def __str__(self):
        return f"Carte(valeur={self.valeur}, enseigne={self.enseigne})"


class Jeu52Cartes:
    """
        Classe du jeu de 52 cartes.
        Il est composé de 13 cartes de 4 enseignes. On peut:
        mélanger (méthode mélanger)
        retirer une carte du sommet (méthode piocher)
        afficher tout le jeu (methodes __str__ et __repr__)
        isoler les cartes par leur indice (notation jeu[indice])

    """
    
    def __init__(self):
        self.jeu = []

        for enseigne in ENSEIGNES:
            for valeur in VALEURS:
                carte = Carte(valeur, enseigne)
                self.jeu.append(carte)

    def __repr__(self):
        return ", ".join(str(carte) for carte in self.jeu)
    
    def __str__(self):                  # affiche le jeu
        return ", ".join(str(carte) for carte in self.jeu)

    def __contains__(self, carte):      # gère carte in jeu
        return carte in self.jeu

    def __getitem__(self, index):       # affiche carte par index
        return self.jeu[index]

    def len(self):
        return len(self.jeu)

    def melanger(self):         # jeu.melanger()
       shuffle(self.jeu)

    def piocher(self):          # jeu.piocher()
        if len(self.jeu) == 0:
            raise ValueError("Le jeu ne contient plus de cartes.")
        return self.jeu.pop(0)
            
