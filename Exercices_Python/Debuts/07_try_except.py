# -*-coding:latin-1 -*
#import os # windows only

while 1:
    annee = input("année : ")
    try:
        annee = int(annee)
        print(annee)
    except:
        print("format non valide!")

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
