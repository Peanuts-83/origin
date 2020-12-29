# -*-coding:latin-1 -*
#import os # On importe le module os

print("range from 0.5 to 9.5 using list comprehension")
[print(x / 10.0, end=", ") for x in range(5, 100, 5)]

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
