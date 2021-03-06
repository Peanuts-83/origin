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

    def __repr__(self):
        return f'{self.nom_complet}, {self.age} ans, résidant à {self.lieu_de_res}.'

    def __getattr__(self, data):
        return f"{data} n'a pas été attribué à {self.name}."

    @property                              # ACCESSEUR : lieu de résidence protégé appelé par une propriété 
    def lieu_de_res(self):
        return self._lieu_de_res

    @lieu_de_res.setter                    # MUTATEUR : modifie lieu de résidence protégé
    def lieu_de_res(self, nouveau_lieu):
        self._lieu_de_res = nouveau_lieu
        return f'{self.prenom} a déménagé à {self._lieu_de_res}'

    @property                               # ACCESSEUR : donne nom complet par prénom + nom
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"
    
    @nom_complet.setter                     # MUTATEUR : change nom et prénom
    def nom_complet(self, nouveau_nom):
        try:
            prenom, nom = nouveau_nom.split(' ')
        except ValueError:
            print("Entrer un prénom et un nom séparés d'un espace")
        else:
            self.prenom = prenom
            self.nom = nom

pers1 = Personne()
print(pers1.nom_complet)
print(pers1)
pers1.lieu_de_res = 'Anger'
pers1.nom_complet = 'Ange Musso'
setattr(pers1,'nom','John')
print(pers1)
setattr(pers1, 'vehicule', 'piaggio')
print(pers1.vehicule)
pers1._code = '1234'
print(pers1._code)
print(hasattr(pers1, '_code'))
print(pers1.__dict__)





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

