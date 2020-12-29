# -*-coding:latin-1 -*
#import os # windows only

while 1:
    annee = input("année : ")
    try:
        annee = int(annee)
    except TypeError as except_return1:
        print(f"Format non valide! L'erreur(1) est : {except_return1}")
    except ValueError as except_return2:
        print(f"Format non valide! L'erreur(2) est : {except_return2}")
    except ZeroDivisionError as except_return3:
        pass
    else:
        print(f"l'année {annee} est valide")
    finally:
        print("Quoiqu'il arrive j'affiche ça")

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
