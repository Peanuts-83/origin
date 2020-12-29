class Personne:

    def __init__(self):                 # __init__ est une methode spéciale
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 48
        self._lieu_de_res = "Paris"     # _ pour attribut privé
        
    def __repr__(self):       # pour Affichage des attribut de l'objet
        return f"Personne : nom({self.nom}), prénom({self.prenom}), age({self.age})"

    def __str__(self):       # Affichage dédié à la fonction 'print' ou à un obj passé en str()
        return f"{self.prenom} {self.nom} est agé de {self.age} ans."
        
    def __getattr__(self, nom_attr):     # Préviens en cas d'appel d'attribut inconnu
        print(f"Attention, l'attribut {nom_attr} n'existe pas!")

    def __setattr__(self, nom_attr, val_attr):      # definit accès à un attribut
        object.__setattr__(self, nom_attr, val_attr)
        # self.enregistrer()

    def __delattr__(self, nom_attr):        # Supprime un attribut
        object.__delattr__(self, nom_attr)

# objet = MaClasse() # On crée une instance de notre classe
# getattr(objet, "nom") # Semblable à objet.nom
# setattr(objet, "nom", val) # = objet.nom = val ou
#     objet.__setattr__("nom", val)
# delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
# hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False
#     sinon

class ZDict:
    def __init__(self):
        self._dico = {}

    def __getitem__(self, index):
        return self._dico[index]

    def __setitem__(self, index, val):
        self._dico[index] = val

    def __delitem__(self, index):
        del self._dico[index]

    def __repr__(self):
        return f'{self._dico}'

    def __contains__(self, val):
        if val in self._dico:
            return True
        else:
            return False

    def __len__(self):
        return f"Le nbre d'éléments est de {len(self._dico)}"