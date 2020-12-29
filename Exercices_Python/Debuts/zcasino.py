# -*-coding:latin-1 -*
import os # On importe le module os qui dispose de variables
          #et de fonctions utiles pour dialoguer avec votre
          # système d'exploitation>

from random import randint
from math import ceil

#variables
pot = int(10)
mise_ok = False

#Boucle
while 1 :

    #user num
    num = input("""***********************
Choix numéro roulette : """)
    #validité num
    try :
        num = int(num)
    except ValueError :
        print('Choisir un chiffre. Recommencez!')
        continue
    if num < 0 or num > 49 :
        print('Choisir un nombre entre 0 et 49...')
        continue

    #user mise
    mise_ok = False
    #validité mise
    while mise_ok == False :
        try :
            mise = input('Choix mise : ')
            mise = int(mise)
        except ValueError :
            print('Choisir un montant valide.')
            continue
        if mise > pot :
            print('misez selon vos moyens.')
            continue
        else :
            print(f'Vous misez {mise} euros sur le {num}')
            mise_ok = True

    
    #roulette
    roulette = randint(0, 49)
    print('Roulette : ', roulette)

    #couleurs (noir ou rouge)
    if roulette%2 == 0 and num%2 == 0 :
        coul = 'pair'
    elif roulette%2 != 0 and num%2 != 0 :
        coul = 'impair'
    else :
        coul = False
        
    #gains
    if roulette == num :
        pot = pot + ceil(mise * 3)
        print('Gain x3, le pot est maintenant de ', pot)
    elif coul == 'pair' or coul == 'impair' :
        pot = pot + ceil(mise * 0.5)
        print('Gain x0.5, le pot est maintenant de ', pot)
    else :
        pot = pot + ceil(mise * -1)
        print('Perdu, le pot est maintenant de ', pot)
        if pot <= 0 :
            print('Vous avez perdu!')
            break
    
    

    
# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
os.system("pause")
