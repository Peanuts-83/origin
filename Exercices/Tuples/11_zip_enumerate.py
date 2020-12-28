# -*-coding:latin-1 -*
#import os # On importe le module os

s = input('3 lettres : ')   # s en string
t = input('3 chiffres : ')  # t en string

t = [n for n in t]          # passer t en liste
zip(s,t)                    # zip /assemble deux séquences
for pair in zip(s,t):
    print(pair)

print(list(zip(s,t)))

for index, element in enumerate(s): # enumerate /parcours elts d'une séq et leurs index
    print(index,element)






# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
