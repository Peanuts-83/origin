# -*-coding:latin-1 -*
import os # On importe le module os


numList = [1,2,3,4,5]   # 
alphaList = ["a","b","c","d","e"]   #
print(numList is alphaList) # False
print(numList == alphaList) # False
numList = alphaList
print(numList is alphaList) # True
print(numList == alphaList) # True
    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
