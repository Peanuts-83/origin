#! /bin/bash python3
import sqlite3, csv, os, sys

# chdir to .py dir
os.chdir(os.path.dirname(sys.argv[0]))


# connect database
bd = sqlite3.connect('universite.db')
cursor = bd.cursor()

# create 'Etudiants' table 
# INT PRIMARY KEY if key provided / INTEGER PRIMARY KEY if self generated key 
cursor.execute("CREATE TABLE Etudiants(\
    NumeroEtudiant INT PRIMARY KEY, \
    Prenom TEXT NOT NULL, \
    Nom TEXT NOT NULL, \
    Adresse TEXT NOT NULL, \
    CodePostal TEXT NOT NULL, \
    Ville TEXT NOT NULL, \
    TelephoneFixe TEXT, \
    TelephonePortable TEXT)")
bd.commit()
# import 'etudiants.csv'
with open('etudiants.csv', 'rt') as liste_etudiants:
    for etudiant in csv.reader(liste_etudiants, delimiter=';'):
        print(etudiant)
        cursor.execute("INSERT INTO Etudiants VALUES(:NumeroEtudiant, :Prenom, :Nom, :Adresse, :CodePostal, :Ville, :TelephoneFixe, :TelephonePortable)", etudiant)
        print('done')
bd.commit()

# create 'Enseignants' table
cursor.execute("CREATE TABLE Enseignants(\
    NumeroEnseignant INT PRIMARY KEY, \
    Prenom TEXT NOT NULL, \
    Nom TEXT NOT NULL, \
    Adresse TEXT NOT NULL, \
    CodePostal TEXT NOT NULL, \
    Ville TEXT NOT NULL, \
    TelephoneFixe TEXT, \
    TelephonePortable TEXT)")
# import 'enseignants.csv'
with open('enseignants.csv', 'rt') as liste_enseignants:
    for enseignant in csv.reader(liste_enseignants, delimiter=';'):
        print(enseignant)
        cursor.execute("INSERT INTO Enseignants VALUES(?, ?, ?, ?, ?, ?, ?, ?)", enseignant)
bd.commit()

# create 'Matieres' table
cursor.execute("CREATE TABLE Matieres(\
    CodeMatiere TEXT NOT NULL, \
    Salle TEXT NOT NULL, \
    NumeroEnseignant TEXT NOT NULL, \
    FOREIGN KEY (NumeroEnseignant) REFERENCES Enseignants(NumeroEnseignant))")
with open('matieres.csv', 'rt') as liste_matieres:
    for matiere in csv.reader(liste_matieres, delimiter=';'):
        cursor.execute("INSERT INTO Matieres VALUES(?, ?, ?)", matiere)
bd.commit()

#create 'Inscriptions' table
cursor.execute("CREATE TABLE Inscriptions(\
    NumeroInscription INT PRIMARY KEY, \
    NumeroEtudiant TEXT NOT NULL, \
    CodeMatiere TEXT NOT NULL, \
    FOREIGN KEY (NumeroEtudiant) REFERENCES Etudiants(NumeroEtudiant), \
    FOREIGN KEY (CodeMatiere) REFERENCES Matieres(CodeMatiere))")
with open('inscriptions.csv', 'rt') as liste_inscriptions:
    for inscription in csv.reader(liste_inscriptions, delimiter=';'):
        cursor.execute("INSERT INTO Inscriptions VALUES(?, ?, ?)", inscription)
bd.commit()

# create 'Resulats' table
cursor.execute("CREATE TABLE Resultats(\
    NumeroResultat INT PRIMARY KEY, \
    NumeroInscription TEXT NOT NULL, \
    Note VARCHAR(5), \
    FOREIGN KEY (NumeroInscription) REFERENCES Inscritpions(NumeroInscription))")
with open('resultats.csv', 'rt') as liste_resultats:
    for resultat in csv.reader(liste_resultats, delimiter=';'):
        cursor.execute("INSERT INTO Resultats VALUES(?, ?, ?)", resultat)
bd.commit()
bd.close()