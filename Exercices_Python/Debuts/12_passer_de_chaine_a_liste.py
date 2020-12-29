# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # syst�me d'exploitation

# parametre de fonction libre en *z (autant qu'on veux!)
def fonction(a, b, *z):
    print(a, b, z)
    
print(fonction('non', 'non', 'oui', 'peut-', 'etre'))

# exercice p129 / ecrire fonction identique � print
def afficher(*param, sep=' ', fin='\n') :
    param = list(param) # on passe le tuple en liste
    for i, parametre in enumerate(param) :
        param[i] = str(parametre) # les param sont convertis en chaines str()
    chaine = sep.join(param) # les chaines sont concat�n�es en une seule
                             # avec s�parateurs sep=' '
    chaine += fin            # parametre fin ajout� � la chaine
    print(chaine, end='')    # 
    
print(afficher(input("entrer des parametres : ")))

# compr�hension et modification de liste avec []
liste = [1, 2, 5, 8, 11, 15, 22]
print("modif liste au carr� = [1, 2, 5, 8, 11, 15, 22]",
      [ nbr * nbr for nbr in liste])
print("modif conditionnelle, recherche des nbr pairs : ",
      [ nbr for nbr in liste if nbr%2 == 0])

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
