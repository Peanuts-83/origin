# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

# parametre de fonction libre en *z (autant qu'on veux!)
def fonction(a, b, *z):
    print(a, b, z)
    
print(fonction('non', 'non', 'oui', 'peut-', 'etre'))

# exercice p129 / ecrire fonction identique à print
def afficher(*param, sep=' ', fin='\n') :
    param = list(param) # on passe le tuple en liste
    for i, parametre in enumerate(param) :
        param[i] = str(parametre) # les param sont convertis en chaines str()
    chaine = sep.join(param) # les chaines sont concaténées en une seule
                             # avec séparateurs sep=' '
    chaine += fin            # parametre fin ajouté à la chaine
    print(chaine, end='')    # 
    
print(afficher(input("entrer des parametres : ")))

# compréhension et modification de liste avec []
liste = [1, 2, 5, 8, 11, 15, 22]
print("modif liste au carré = [1, 2, 5, 8, 11, 15, 22]",
      [ nbr * nbr for nbr in liste])
print("modif conditionnelle, recherche des nbr pairs : ",
      [ nbr for nbr in liste if nbr%2 == 0])

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
