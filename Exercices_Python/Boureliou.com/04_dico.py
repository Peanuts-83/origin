# -*-coding:latin-1 -*
import os # On importe le module os



d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

d['prenom']='Jacques'
print(d, '\n')

print(d.keys())
for cles in d.keys():
    print('Clés : ',cles)
print(d.values())
for valeurs in d.values():
    print('Valeurs : ', valeurs)

for cles, valeurs in d.items():
    print('Tuples clés/valeurs : ', cles, valeurs)

#for valeurs in d.values():
#for cles, valeurs in d.items():
print(f"{d['prenom']} {d['nom']} a {d['age']} ans")


    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
