# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

# boucle infinie 
while 1:
    # Demande année à l'utilisateur
    annee = input("entrer une année : ")
    # passe la chaine 'annee' en type int (entier)
    annee = int(annee)
    # condition de l'année bissextile, divisible par 400 ou (par 4 et non par 100)
    if annee%400 == 0 or (annee%4 == 0 and annee%100) > 0:
        print("C'est une année bissextile!")
    else:
        print("ce n'est pas une année bissextile...")


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
