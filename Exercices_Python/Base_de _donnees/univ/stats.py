#! /bin/bash python3
"""
MoyMat par matiere
MoyMax
MoyMin par matiere
NbEtudiants par matiere
MoyTotale de toutes les matieres
NbEtudParDep
"""
import sqlite3, csv, json, os, sys

# chdir to .py dir
os.chdir(os.path.dirname(sys.argv[0]))


# connect database
bd = sqlite3.connect('universite.db')
cursor = bd.cursor()

"""
# AVG by student and by matiere
cursor.execute("SELECT NumeroEtudiant, Prenom || ' ' || Nom AS Fullname FROM Etudiants")
for etu in cursor.fetchall():
    if 'NumeroEtudiant' not in etu:
        print(etu)
        cursor.execute(f"SELECT * FROM Inscriptions I WHERE I.NumeroEtudiant = {etu[0]}")
        for inscr in cursor.fetchall():
            if 'NumeroEtudiant' not in inscr:
                cursor.execute(f"SELECT AVG(Note) FROM Resultats R WHERE R.NumeroInscription = {inscr[0]} ")
                for a in cursor.fetchall():
                    print(inscr[2], ':', a)
                    """

# create json file
stats = open('statistiques.json', 'wt')
Statistiques = {}


# NbEtudiants par mat
cursor.execute("SELECT CodeMatiere FROM Matieres")
NbEtudiants = {}    # dict NbEtudiants
for mat in cursor.fetchall():
    if 'CodeMatiere' not in mat:
        cursor.execute("SELECT COUNT(NumeroEtudiant) FROM Inscriptions WHERE CodeMatiere = ?", (mat[0],))
        for etu_sum in cursor.fetchall():
            NbEtudiants[mat[0]] = etu_sum[0]
Statistiques['NbEtudiantsParMat'] = NbEtudiants

# NbEtudParDep
NbEtudParDep = {}
cursor.execute("SELECT CodePostal/1000, COUNT(NumeroEtudiant) FROM Etudiants GROUP BY CodePostal/1000 ")
for dep in cursor.fetchall():
    if dep[0] != 0:
        NbEtudParDep[dep[0]] = dep[1]
Statistiques['NbEtudParDep'] = NbEtudParDep

# MoyMat
MoyMat = {}
cursor.execute("SELECT CodeMatiere FROM Matieres")
for mat in cursor.fetchall():
    if 'CodeMatiere' not in mat:
        cursor.execute("SELECT NumeroInscription, AVG(Note) FROM Resultats GROUP BY (SELECT CodeMatiere FROM Inscriptions WHERE CodeMatiere = ?)", (mat,))
        for moy in cursor.fetchall():
            print(mat, moy)



print(Statistiques)
stats.write(json.dumps(Statistiques))
stats.close()
