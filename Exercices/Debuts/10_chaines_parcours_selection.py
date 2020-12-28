# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

prenom = "Tom"
nom = "Ranque"
age = "45"

# positionnement de chaines dans une chaine // .format()
chaine1 = "je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom.upper(), age)
print(chaine1)


# parcours d'une chaine avec while:
i = 0
while i < 15 :
    print(chaine1[i])
    i += 1
    
# sélection de caracteres de chaine
print(chaine1[0:8],
      chaine1[:5],
      chaine1[18:])
# puis création d'une nouvelle chaine modifiée en ne reprenant
# que les parties de la chaine d'origine qui m'intéressent
print(chaine1[:12], "Isabelle HACQUE", chaine1[24:])

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
