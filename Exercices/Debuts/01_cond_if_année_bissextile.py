# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # syst�me d'exploitation

# boucle infinie 
while 1:
    # Demande ann�e � l'utilisateur
    annee = input("entrer une ann�e : ")
    # passe la chaine 'annee' en type int (entier)
    annee = int(annee)
    # condition de l'ann�e bissextile, divisible par 400 ou (par 4 et non par 100)
    if annee%400 == 0 or (annee%4 == 0 and annee%100) > 0:
        print("C'est une ann�e bissextile!")
    else:
        print("ce n'est pas une ann�e bissextile...")


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
os.system("pause")
