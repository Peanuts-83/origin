class Personne:
    objets = 0
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_res = 'Paris'
        Personne.objets += 1

    @property
    def lieu_res(self):
        return self._lieu_res

    @lieu_res.setter
    def lieu_res(self, lieu):
        print(f"{self.prenom} déménage à {lieu}.")
        self._lieu_res = lieu


    @ property
    def nom_complet(self):
        return f'{self.prenom} {self.nom}'

    @nom_complet.setter
    def nom_complet(self, nouveau_nom):
        try:
            nom, prenom = nouveau_nom.split(' ')
        except ValueError:
            raise ValueError("Donner un nom et un prénom séparés d'un espace")
        else:
            self.nom = nom
            self.prenom = prenom


class Panier:
    def __init__(self):
        self.produits = {}

    @property
    def total(self):
        total = 0
        for produit, prix in self.produits.items():
            total += prix
        return total

    def acheter(self, nom_prod, prix):
        self.produits[nom_prod] = prix




class Tableau:
    def __init__(self):
        self.surface = ''

    def ecrire(self, message):
        if self.surface != '':
            self.surface += '\n'
        self.surface += message

    def lire(self):
        print(self.surface)

    def effacer(self):
        self.surface = ''




