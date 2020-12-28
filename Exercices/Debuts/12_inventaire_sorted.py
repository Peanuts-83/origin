# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

inventaire = [('pomme', 22), ('melons', 4), ('poires', 18),
              ('fraises', 76), ('prunes', 51)] 
print("Inventaire dans le désordre : ", inventaire)

print('Soluce 1 **************************')
# Inversion des objets dans les listes
inventaire_inv = [(qtt, nom) for nom, qtt in inventaire]
# Tri par ordre décroissant des nbr avec fonction de liste .sort
inventaire_inv.sort(reverse = True)
# Inversion à nouveau
inventaire = [(nom, qtt) for qtt, nom in inventaire_inv]
print("Inventaire dans l'ordre : ", inventaire)

print('Soluce 2 **************************')
# Inversion des objets dans les listes
inventaire_inv = [(qtt, nom) for nom, qtt in inventaire]
# Tri et ré-inversion de la liste en 1 seule fois avec fonction sorted
inventaire = [(nom, qtt) for qtt, nom in sorted(inventaire_inv, reverse = True)]
print("Inventaire dans l'ordre : ", inventaire)



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
