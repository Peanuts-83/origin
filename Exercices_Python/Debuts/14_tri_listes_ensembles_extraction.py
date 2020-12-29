# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation>

#création de 2 listes
ville = ['john', 'will', 'tom', 'vic', 'sam']
salon = ['john', 'isa', 'ducop', 'tom', 'vic', 'andrew']
print(type(ville))

#trie les noms en commun/ incrementation par += 1
nbr = 0
for nom in salon :
    if nom in ville:
        print(nom)
        nbr += 1
print('nbre de nom en commun : ',nbr)
        
print('######################')

#création de 2 ensembles
ville = {'john', 'will', 'tom', 'vic', 'sam'}
salon = {'john', 'isa', 'ducop', 'tom', 'vic', 'andrew'}
print(type(ville))

#trie les noms en commun/ len pour length
nbr = len(salon & ville)
print(salon & ville)
print('nbre de nom en commun : ',nbr)
#idem
nbr = len(salon.intersection(ville))
print('nbre de nom en commun : ',nbr)
        
print('######################')

#le nbre inconnu dans un ensemble/ on connait 1
ens = {3800, 1}
connu = 1
inconnu = (ens - {connu})
print(inconnu)                  #ensemble réduit à un valeur
inconnu = (ens - {connu}).pop() #valeur unique extraite par pop()
print(inconnu)
    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
