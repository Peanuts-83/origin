# -*-coding:latin-1 -*
import os # On importe le module os


semaine = ['lundi', 'mardi', 'merc', 'jeudi', 'vendr', 'samedi', 'dimanche']
print(semaine)
print(semaine[4])
(semaine[0], semaine[6]) = (semaine[6], semaine[0])
print(semaine)
i = 1
while i<13 :
    print(semaine[6])
    i += 1

    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
