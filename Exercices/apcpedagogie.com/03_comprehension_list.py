# -*-coding:latin-1 -*
import os # On importe le module os


#appel input dans une chaine str()
suite = input("ecrivez une série d'entiers séparés par un espace :")
liste = suite.split()    # 1/transforme str en list et l'affiche
print('1/',liste)            

i=0                         # 2/liste en colonne
for n in liste: 
    print(f"2/l'index {i} renvoie {n}")
    i += 1

nums = [int(s) for s in liste]  # tranforme str en int dans liste
print('3/Somme : ', sum(nums))    # 3/somme des int de la nvelle liste nums

print('4/Multiple de 3 :', [s*3 for s in nums])   # 4/liste x3

nums.sort(reverse=True)                 # classement +gd au +ptt
print('5/Plus gde valeur : ', nums[0])    # 5/affiche 1ere valeur

print('6/Plus ptte valeur : ', nums[i-1]) # 6/affiche plus petite valeur


nums_pair = [n for n in nums if n%2 == 0]
print('7/Liste nbres pairs',nums_pair)            #7/affiche nbres pairs

nums_impair = [n for n in nums if n%2 != 0]
print('8/Somme des nbres impairs : ', sum(nums_impair)) #8/somme impairs


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
