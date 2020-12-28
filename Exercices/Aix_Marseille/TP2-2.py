""" . Ecrivez une fonction convertir_ligne(s) qui prends une chaîne dans le format “«ville» :
«température»” et renvoie une liste avec le nom de la ville et la température."""
def convertir_ligne(str):
    if ':' in str:
        a, b = str.split(' : ')
        return [a, int(b)]

""" . Ecrivez une fonction lire_fichier(nom_du_fichier) qui lit un fichier de données dont le
nom est passé en argument, et renvoie un dictionnaire qui contient les informations sous-forme
clé-valeur, par exemple :"""
def lire_fichier(file_name):
    fichier = open(file_name, 'r', encoding='cp1252')
    contenu_fichier = fichier.read().split('\n')
    print(contenu_fichier)
    res = {}
    for x in contenu_fichier:
        a, b = convertir_ligne(x)
        res[a] = b
    demande_ville(res)

standard_input = 'Paris', 'Londres', 'Vladivostok', ''
""" . Ecrivez une fonction demande_villes(base_donnees) qui prends un dictionnaire base_donnees,
affiche la liste de villes disponibles dans le dictionnaire et demande à l’utilisateur de quelles villes
il veut connaître la température. Finalement, la fonction renvoie une liste avec les noms entrés."""
def demande_ville(base_donnees):
    print('Les temps des villes suivantes sont disponibles:')
    for ville in base_donnees:
        print(ville, end=', ')
    print('entrez les villes dont vous souhaitez connaitre la temp.', '\nEnter pour terminer.')
    villes_demandees = []
    while True:
        ville = input('Ville:')
        if ville in base_donnees.keys():
            villes_demandees.append(ville)
        elif ville == '':
            break
    affiche_donnees(base_donnees, villes_demandees)

""" . Ecrivez une fonction affiche_donnees(base_donnees, villes) qui prends un dictionnaire
base_donnees et une liste de noms de ville villes, et affiche un tableau avec les températures
pour les villes demandées. L’affichage doit suivre le modèle de la session d’exemple en haut.
"""
import numpy as np
def affiche_donnees(base_donnees, villes_demandees):
    print('base de données:',base_donnees)
    tableau = np.array([['TOWN', '°C']])
    tableau = np.append(tableau, [[key, val] for key, val in base_donnees.items() if key in villes_demandees], 0)
    
    print(tableau)

lire_fichier('temperatures.txt')