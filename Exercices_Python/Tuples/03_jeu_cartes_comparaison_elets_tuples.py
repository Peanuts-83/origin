# -*-coding:latin-1 -*
#import os # On importe le module os

suite1='Pique,Trèfle,Coeur,Carreau'
liste_val=[(2,'Deux'),(3,'Trois'),(4,'Quatre'),
        (5,'Cinq'),(6,'Six'),(7,'Sept'),(8,'Huit'),
        (9,'Neuf'),(10,'Dix'),(11,'valet'),(12,'dame'),(13,'roi'),(14,'as')]

liste_coul = suite1.split(',')
jeu = []
for a in liste_coul:                    # creation des tuples ('coul',num,'num')
    for b in liste_val:
        jeu.append((a,) +b)
print(jeu)

from random import shuffle
shuffle(jeu)                                        # mélange des cartes
print('\n', 'Jeu mélangé : ', jeu)
joueur1 = [n for n in jeu if jeu.index(n)%2 == 0]   # main joueur1 cartes pair
print('\n', 'Joueur 1 : ', joueur1)
#for i in range(0,52,2):                            # alternative main joueur1
#   joueur1.append(jeu[i])

joueur2 = [n for n in jeu if jeu.index(n)%2 != 0]
print('\n', 'Joueur 2 : ', joueur2)

# désigne le nom et la couleur d'une carte
# accès à l'interieur d'un tuple par [][]
print('\n','carte 3 du joueur 1 : ','le %s de %s'%(joueur1[2][2],joueur1[2][0]))
print('\n',f'la carte du joueur 2 est le {joueur1[2][2]} de {joueur1[2][0]}')
print(joueur1[2][1])

# jeu manche par manche
# les carte de valeur égale sont écartées
pt_1 = 0
pt_2 = 0
i=0
for n in joueur1:
    if int(joueur1[i][1]) > int(joueur2[i][1]):
        pt_1 += 1
        print('carte joueur1 : ', joueur1[i][2],' de ',joueur1[i][0],
              '|| carte joueur2 : ', joueur2[i][2],' de ',joueur2[i][0])
        print(f"joueur1 : {pt_1}pt. joueur2 : {pt_2}pt.".center(70,'-'))
        i+=1
    elif joueur1[i][1] < joueur2[i][1]:
        pt_2 += 1
        print('carte joueur1 : ', joueur1[i][2],' de ',joueur1[i][0],
              '|| carte joueur2 : ', joueur2[i][2],' de ',joueur2[i][0])
        print(f"joueur1 : {pt_1}pt. joueur2 : {pt_2}pt.".center(70,'-'))
        i+=1
    else:
        print('carte joueur1 : ', joueur1[i][2],' de ',joueur1[i][0],
              '||carte joueur2 : ', joueur2[i][2],' de ',joueur2[i][0])
        print('Egalité!'.center(70, '*'))
        i+=1
        continue



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
