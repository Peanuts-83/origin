"""Exercice 1. Ecrivez une fonction x_en_premier(mots) qui prends en argument une liste de
chaînes mots, et renvoie une liste triée, sauf que toutes les chaînes qui commencent par ‘x’ doivent
précéder les autres.
"""
def x_en_premier(mots):
    res = [mots.pop(mots.index(x)) for x in sorted(mots) if x[0] == 'x']
    res.extend([x for x in sorted(mots)])
    return res

print(x_en_premier(['mix','xyz','apple','xanadu','aardvark']))

"""Exercice 2. 
Le triangle de Pascal. Écrivez une fonction nouvelle_ligne(ligne) qui prends une
liste ligne contenant une ligne du triangle de Pascal, et renvoie la ligne suivante. Ensuite, écrivez
une fonction pascal(n) qui affiche les première n lignes du triangle.
Reprenez le programme vu en TD 1 pour le triangle de Pascal : tapez le fonctions
dans un script pascal.py et testez-le.
. Modifiez la fonction pascal(n) de façon qu’elle renvoie une liste avec les lignes du triangle, au
lieu de l’afficher directement.
"""
def nouvelle_ligne(l):
    new = [l[n] + l[n+1] if -1 < n < len(l)-1 else l[n] for n in range(-1, len(l))]
    return new

def pascal(n):
    line = [1]
    l = ' '.join([str(x) for x in line])
    print(f"{f'{l}':^100}")
    for x in range(n):
        line = nouvelle_ligne(line)
        l =  ' '.join([str(x) for x in line])
        print(f"{f'{l}':^100}")
        
print(nouvelle_ligne([1,3,3,1]))
print(pascal(14))

"""Exercice 3. Téléchargez le fichier temperatures.txt de la page web du cours avec la commande :
$ wget http://pageperso.lif.univ-mrs.fr/~stefano.facchini/python/temperatures.txt
Le fichier contient les températures de certaines villes dans le format “«ville» : «température»”.
Le but de l’exercice est écrire un programme villes.py qui : 1. extrait les informations et les
mémorise dans une «base de données» (un dictionnaire Python) 2. propose à l’utilisateur la liste
des villes disponibles et lui demande de quelles villes il veut connaître la température 3. affiche les
informations demandées.
"""
import urllib.request, urllib.parse, json
import keyboard
x = urllib.request.urlopen('http://pageperso.lif.univ-mrs.fr/~stefano.facchini/python/temperatures.txt')
x = x.read()
city_temp = x.decode('cp1252')
ct = city_temp.split('\n')
for n in range(len(ct)):
    if len(ct[n])<1:
        ct.remove(ct[n])
new_city_temp = {}
for data in ct:
    z = (x for x in data.split(' : ') if x != '')
    a, b = tuple(z)
    new_city_temp[a] = int(b)
print(new_city_temp)

standard_input = 'Paris', 'Londres', 'Marseille', ''
print('Les températures de Londres, Marseille, New York, Paris, Rome et Vladivostock sont disponibles.')
print('Entrez les noms des villes dont vous souhaitez connaitre la température. Tapez RETURN pour terminer.')
towns = []
while True:
    a = input('NOM:')
    if a in new_city_temp.keys():
        towns.append(a)
    elif a == '':
        break
for name in towns:
    print(name, ':', new_city_temp[name],'°C', end=' - ')

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
    res = {key:val for key, val in convertir_ligne(x) for x in contenu_fichier}
    print(res)

lire_fichier('temperatures.txt')