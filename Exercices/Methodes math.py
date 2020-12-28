class Duree:
    def __init__(self, minutes=0, secondes=0):
        self.minutes = minutes
        self.secondes = secondes
        self.attr_temporaire = 5

    def __repr__(self):                         # pr affichage direct
        return f"{self.minutes:02} : {self.secondes:02}"

    def __str__(self):                          # pour affichage via print
        return f"{self.minutes:02} : {self.secondes:02}"    # :02 pr afficher 2 chiffres

    def __add__(self,obj_a_ajouter):            # ajout de temps 
        nvelle_duree = Duree()
        nvelle_duree.secondes = self.secondes
        nvelle_duree.minutes = self.minutes
        if isinstance(obj_a_ajouter, int):      # ajout de temps int() type d1 + 40
            nvelle_duree.secondes += obj_a_ajouter  # imp! +=
        elif isinstance(obj_a_ajouter, Duree):  # ajout de durée type d1 + d2
            nvelle_duree.secondes += obj_a_ajouter.secondes
            nvelle_duree.minutes += obj_a_ajouter.minutes
        else:                                   # erreur si autres données
            raise TypeError("Seuls des temps int() ou des durées peuvent être ajoutés.")
        if nvelle_duree.secondes >= 60:         # gestion sec >= 60
            nvelle_duree.minutes += nvelle_duree.secondes // 60
            nvelle_duree.secondes = nvelle_duree.secondes % 60
        return nvelle_duree

    def __iadd__(self, obj_a_ajouter):          # augmente self par incrément type d1 += 120
        self.secondes += obj_a_ajouter
        if self.secondes >= 60:
            self.minutes += self.secondes // 60
            self.secondes = self.secondes % 60
        return self

    def __radd__(self, obj_a_ajouter):          # ajout type 40 + d1 / Right ADD
        return self + obj_a_ajouter

    def __gt__(self, autre_duree):              # comparer 2 durées / Greater Than
        nbr_sec1 = self.secondes + self.minutes * 60
        nbr_sec2 = autre_duree.secondes + autre_duree.minutes * 60
        return nbr_sec1 > nbr_sec2              # renvoie True/False

    def __getstate__(self):             # modifie attr_temp avant enreg par pickler
        dict_attr = dict(self._attr)
        dict_attr["attr_temporaire"] = 0
        return dict_attr

    def __setstate__(self,dict_attr):  # modifie attr_temp après ouvreture par unpikcler
        dict_attr["attr_temporaire"] = 0
        self.__dict__ = dict_attr

a = Duree(25, 30); b = (Duree(12, 54))
print(a,'  ', b)
print(a+b)
print(a.__add__(b))