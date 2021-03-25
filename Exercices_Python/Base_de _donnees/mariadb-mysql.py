#! /bin/bash python3
import mysql.connector

### création base de données > CREATE > INSERT %s // pour connection à serveur MariaDB ou MySQL ###
basedonnees = mysql.connector.connect(host='localhost', user='catalogue', password='Azerty789', database='Catalogue')
curseur = basedonnees.cursor()
curseur.execute("CREATE TABLE Produits (reference CHAR(5) NOT NULL PRIMARY KEY,nom TINYTEXT NOT NULL, prix FLOAT NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
curseur.execute("INSERT INTO Produits (reference, nom, prix) VALUES (%s, %s, %s )", ('ARB42', "Canapé deux places noir", 199.99))
basedonnees.commit()
basedonnees.close()

### insertion de données depuis un dict > INSERT %()s ###
basedonnees = mysql.connector.connect(host='localhost', user='catalogue', password='Azerty789', database='Catalogue')
curseur = basedonnees.cursor()
produits = [
	{"reference":"EIS3P", "nom":"Chaise de salle à manger", "prix":25},
	{"reference":"BA9KI", "nom":"Commode blanche", "prix":139.90},
	{"reference":"OI4HE", "nom":"Table basse", "prix":24.95},
	{"reference":"IOM9X", "nom":"Lit double", "prix":699.99}
]
for fiche in produits:
    curseur.execute("INSERT INTO Produits (reference, nom, prix) VALUES (%(reference)s, %(nom)s, %(prix)s)", fiche)
basedonnees.commit()
basedonnees.close()

### récupérer des données > SELECT > FETCHONE > FETCHALL ###
>>> basedonnees = mysql.connector.connect(host='localhost', user='catalogue', >>> password='Azerty789', database='Catalogue')
>>> curseur = basedonnees.cursor()
>>> curseur.execute("SELECT reference, nom, prix FROM Produits")
>>> for ligne in curseur.fetchall():
...     print(ligne)
...
('ARB42', 'Canapé deux places noir', 199.99)
('BA9KI', 'Commode blanche', 139.9)
('EIS3P', 'Chaise de salle à manger', 25.0)
('IOM9X', 'Lit double', 699.99)
('OI4HE', 'Table basse', 24.95)
>>> basedonnees.close()

