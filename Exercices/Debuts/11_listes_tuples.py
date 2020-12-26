# -*-coding:latin-1 -*
#import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation

# creation de liste
ma_liste = [1, 0.56, 'coucou', "youpi"]
print(ma_liste)

# appel de l'objet 'coucou' par son n° d'index et changement de cet objet
ma_liste[2] = 'snif...'
print(ma_liste)

# append ajoute un objet en fin de liste // insert ajoute en n° d'index un obj
ma_liste.append(83)
print(ma_liste)
ma_liste.insert(2, 'yes')
print(ma_liste)

# Suppression par del ou remove
del ma_liste[2]
print(ma_liste)
ma_liste.remove('snif...')
print(ma_liste)

# Parcours de liste / lecture en boucle / elt in + enumerate
for elt in ma_liste:
    print(elt)
for i, elt in enumerate(ma_liste):
    print(f"A l'index {i} se trouve {elt}")
for elt in enumerate(ma_liste):
    print(elt)

# tuple / liste non modifiable marquée par ()
while 1:
    def decomposer(entier, diviseur):
        p_e = entier // diviseur
        reste = entier % diviseur
        return p_e, reste
    entier = input("entrer nombre : ")
    diviseur = input("entrer diviseur : ")
    entier = int(entier)
    diviseur = int(diviseur)
    p_e, reste = decomposer(entier, diviseur)
    print("partie entiere :", p_e, "reste : ", reste)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
