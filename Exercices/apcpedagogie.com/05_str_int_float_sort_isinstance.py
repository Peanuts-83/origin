# -*-coding:latin-1 -*
import os # On importe le module os

stock = ['ordi bureau','ordi portable',100,'camera',310.28,'haut-parleurs',
         27.00,'tele',1000,'carte mere','souris','clavier',
         500,'barette memoire']

print('liste stock : ',stock)    # 1/ Affiche liste

stock_str = [n for n in stock if isinstance(n, str) == True]
print('liste 1 :',stock_str)                # 2/ Affiche 1 liste str et 1 liste nbr
stock_nbr = [n for n in stock if isinstance(n, float) == True
               or isinstance(n, int) == True]
print('liste 2 :',stock_nbr)

print('liste 1 :',len(stock_str))           # 3/ nbre d'éléments par liste
print('liste 2 :',len(stock_nbr))

stock_str.sort()
print('liste 1 croissant :', stock_str)     # 4/ Tri par ordre croiss/decroissant
stock_str.sort(reverse=True)
print('liste 1 décroissant :',stock_str)

stock_nbr.sort()
print('liste 2 croissant : ', stock_nbr)    # 5/ Tri par ordre croiss/decroissant

stock_nbr.sort(reverse=True)
print('liste 2 décroissant : ', stock_nbr)



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
