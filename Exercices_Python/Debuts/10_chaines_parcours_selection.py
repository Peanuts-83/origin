# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # syst�me d'exploitation

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
    
# s�lection de caracteres de chaine
print(chaine1[0:8],
      chaine1[:5],
      chaine1[18:])
# puis cr�ation d'une nouvelle chaine modifi�e en ne reprenant
# que les parties de la chaine d'origine qui m'int�ressent
print(chaine1[:12], "Isabelle HACQUE", chaine1[24:])

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
