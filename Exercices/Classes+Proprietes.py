class Personne:
    objets_créés = 0                    # compteur à 0

    def __init__(self):                 # initialisation des attributs
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 48
        self._lieu_de_res = "Paris"     # _ pour attribut privé
        self.surface = ""
        Personne.objets_créés += 1      # incrémentation du compteur
        
    def ecrire(self,message_a_ecrire):  # écrire msg sur surface
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):                        # lire msg sur surface
        print(self.surface)

    def effacer(self):                     # effacer msg
        self.surface = ""

    @property                              # ACCESSEUR : lieu de résidence protégé appelé par une propriété 
    def lieu_de_res(self):
        return self._lieu_de_res

    @lieu_de_res.setter                    # MUTATEUR : modifie lieu de résidence protégé
    def lieu_de_res(self, nouveau_lieu):
        self._lieu_de_res = nouveau_lieu
        print(f'{self.prenom} a déménagé à {self._lieu_de_res}')

    @property                               # ACCESSEUR : donne nom complet par prénom + nom
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"
    
    @nom_complet.setter                     # MUTATEUR : change nom et prénom
    def nom_complet(self, nouveau_nom):
        try:
            prenom, nom = nouveau_nom.split(' ')
        except ValueError:
            raise ValueError("Entrer un prénom et un nom séparés d'un espace")
        else:
            self.prenom = prenom
            self.nom = nom

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

