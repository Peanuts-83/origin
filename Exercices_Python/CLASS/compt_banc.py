class CpteBanc:
    def __init__(self, num, nom, solde):
        if not isinstance(num, int):
            return 'Numérode compte non valide.'
        self.num = num
        self.nom = nom
        self.solde = solde

    def __repr__(self):
        if self.solde >= 0:
            return f"Compte n°{self.num}, {self.nom}, solde: {self.solde} €."
        else:
            return self.agios()

    def versement(self, som_v):
        self.solde += som_v
        print(f"Versement effectué, le solde est désormais de {self.solde} €.")
    
    def retrait(self, som_r):
        self.solde -= som_r
        print(f"Retrait effectué, Le solde est maintenant de {self.solde} €.")

    def agios(self):
        agios = abs(self.solde*0.05)
        return f"Des agios de 5% sont applicables sur le découvert. Soit {agios} €.\n \
        Nouveau solde: {self.solde - agios} €."



######
a = CpteBanc(1485233994, 'Tom', 1200)
print(a)
a.retrait(500)
a.versement(200)
a.retrait(1100)
print(a)