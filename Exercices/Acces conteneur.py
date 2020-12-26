class Zdico:

    def __init__(self):
        self._dico = {}     # _ pour attribut protégé, le dico accessible que depuis la class

    def __getitem__(self, index):       # renvoie l'index demandé
        if index in self._dico:         # si l'index est présent dans le dico
            return self._dico[index]
        else:                           # sinon message d'erreur
            raise ValueError("Erreur d'index!")

    def __setitem__(self, index, val):  # modifie une entrée du dico
        self._dico[index] = val

    def __delitem__(self, index):       # pour suppression d'index
        del self._dico[index]

    def __contains__(self, index):        # pour utiliser 'in' dans une recherche d'index
        return self._dico.__contains__(index)     # 'aze' in dico (par exemple)

    def __len__(self):                  # nbre d'index du dico
        return len(self._dico)

    def __repr__(self):                 # affiche contenu dico
        return f"Zdico : dico({self._dico})"

    def __str__(self):                  # affiche par print
        return f"le contenu du dictionnaire Zdico est {self._dico}."

    