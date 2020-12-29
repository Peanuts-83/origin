class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.prenom = 'Tom'
    
    def __repr__(self):
        return f"{self.prenom} {self.nom}"

class AgentSpecial(Personne):               # classe fille de la classe Personne
    def __init__(self, nom, matricule):     # possible class D(A,B,C):
        # Personne.__init__(self, nom)        # nom et prenom attr de Personne
        super().__init__(nom)                 # nom et prenom par super() >> + simple
        self.matricule = matricule

    def __repr__(self):
        return f"Agent {self.prenom} {self.nom}, matricule {self.matricule}"


# >>> issubclass(AgentSpecial,Personne)
# True
# >>> issubclass(Personne,AgentSpecial)
# False
# >>> issubclass(AgentSpecial,object)
# True
# >>> isinstance(agent,Personne)
# True
# >>> isinstance(agent,AgentSpecial)
# True