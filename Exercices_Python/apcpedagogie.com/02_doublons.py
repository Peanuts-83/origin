# -*-coding:latin-1 -*
import os # On importe le module os


liste = [3,4,5,3,4,5,1]
print('Trier les doublons de la liste : ',liste)

def supprimeDoublon(liste) :
    #méthode n°1
    ensemble = set(liste)   # par un ensemble, les doublons sont éliminés
    tri = list(ensemble)    # l'ensemble est repassé en liste
    print('Méthode n°1 : ',tri)

    #méthode n°2
    i=0
    liste2 = []     # travail sur une nvelle liste
    for nbr in liste:
        if nbr not in liste2:
            liste2.append(nbr)  # par la fonction append/ ajout en fin de liste
            i+=1
    print('Méthode n°2 : ',liste2)
    
supprimeDoublon(liste)

    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
