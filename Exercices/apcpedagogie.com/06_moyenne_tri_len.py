# -*-coding:latin-1 -*
import os # On importe le module os


moyennes = [14.84,12.66,11.9,12,18.3,3.56,5.8,8,17.33]
moyennes.sort()
print('3 moyennes les plus basses : ',moyennes[:3])
length = len(moyennes) - 3
print('3 moyennes les plus hautes : ',moyennes[length:])



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
