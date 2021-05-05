#! /bin/bash python3
import sqlite3

### Creation et insertion de données > CREATE > INSERT ? ###
basedonnees = sqlite3.connect('contacts.db')
curseur = basedonnees.cursor()
# creation base SQL
curseur.execute('CREATE TABLE Contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, prenom TEXT NOT NULL, adresse TEXT NOT NULL, telFixe TEXT')
# envoi de la requête
basedonnees.commit()
# ajout d'un enregistrement
curseur.execute('INSERT INTO Contacts (nom, prenom, adresse, telFixe) VALUES(?, ?, ?, ?)', ('Dupont', 'Paul', "15 rue Louis Pasteur 10000 SEVRES", '0156382437'))
# envoi de la requête
basedonnees.commit()
basedonnees.close()

### Création et insertion de données via une liste de dict > INSERT : ###
basedonnees = sqlite3.connect('contacts.db')
curseur = basedonnees.cursor()
personnes = [
	{"nom":"Chabot", "prenom":"Martin", "adresse":"18 rue Général Leclerc 13600 La Ciotat", "telephoneFixe":"0499506373"},
	{"nom":"Delbois", "prenom":"Julie", "adresse":"35 rue du Château 77176 Savigny le Temple", "telephoneFixe":"0199836074"},
	{"nom":"Rivard", "prenom":"Christelle", "adresse":"83 rue de Québec 83400 Hyères", "telephoneFixe":"0499687013"}
]
for contact in personnes:
    curseur.execute("INSERT INTO Contacts  (nom, prenom, adresse, telFixe) VALUES(:nom, :prenom, :adresse, :telFixe)", contact)
basedonnees.commit()
# get last id inserted
idDernierEnregistrement = curseur.lastrowid
basedonnees.close()

### modifier des données > UPDATE ###
basedonnees = sqlite3.connect('contacts.db')
curseur = basedonnees.cursor()
curseur.execute("UPDATE Contacts SET telFixe = ? WHERE id = ?", ('0523659874', 2))
basedonnees.commit()
basedonnees.close()


### récupérer les données > SELECT > FETCHONE ###
>>> basedonnees = sqlite3.connect('contacts.db')
>>> curseur = basedonnees.cursor()
>>> curseur.execute("SELECT nom, prenom, telFixe FROM Contacts WHERE id = ?", ('2',))
>>> contact = curseur.fetchone()
>>> print(contact)
('Chabot', 'Martin', '0598635076')
>>> basedonnees.close()

### récupérer les données > SELECT > FETCHALL ###
>>> basedonnees = sqlite3.connect('contacts.db')
>>> curseur = basedonnees.cursor()
>>> curseur.execute("SELECT nom, prenom, telFixe FROM Contacts")
>>> for contact in curseur.fetchall():
...     print(contact)
...
('Dupont', 'Paul', '0325997452')
('Chabot', 'Martin', '0598635076')
('Delbois', 'Julie', '0199836074')
('Rivard', 'Christelle', '0499687013')
>>> basedonnees.close()

