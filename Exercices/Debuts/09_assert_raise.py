# -*-coding:latin-1 -*
#import os # windows only

while 1:
    annee = input("ann�e : ")
    try:
        annee = int(annee)
#        assert annee >= 1
        if annee == 0:
            print("Format non valide! L'erreur est : ann�e nulle")
            raise ValueError("Format non valide! L'erreur est : ann�e nulle")
        elif annee < 0:
            raise ValueError("Format non valide! L'erreur est : ann�e n�gative")
    except ValueError:
        print("Recommencez")
    else:
        print(annee)


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
