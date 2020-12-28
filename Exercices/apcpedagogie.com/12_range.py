# -*-coding:latin-1 -*
import os # On importe le module os

lstVide=[]
lstFlottant=[0.0]*5

print('lstVide=',lstVide,'\n','lstFlottant=',lstFlottant,'\n')
rien=input('Return')
lstVide += range(0,1000,200)
print('lstVide=',lstVide,'\n','lstFlottant=',lstFlottant,'\n')
rien=input('Return')
print('index 0 à 3 : ', range(4))


    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
