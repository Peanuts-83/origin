# -*-coding:latin-1 -*
#import os # windows only

while 1:
    annee = input("année : ")
    try:
        annee = int(annee)
#        assert annee >= 1
        if annee == 0:
            print("Format non valide! L'erreur est : année nulle")
            raise ValueError("Format non valide! L'erreur est : année nulle")
        elif annee < 0:
            raise ValueError("Format non valide! L'erreur est : année négative")
    except ValueError:
        print("Recommencez")
    else:
        print(annee)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
