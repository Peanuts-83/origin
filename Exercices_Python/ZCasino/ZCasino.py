# -*-coding:latin-1 -*
#import os # windows only


# cagnotte initiale user
cagnotte = 10
gain = 0
nbr_lott = 0

#import des modules
import roulette
import banque
import pair_impair2



### banque - calcul des gains
##def gain_user(mise, multiplicateur):
##    global gain
##    gain = mise * multiplicateur
##    print (gain)
##
##def val_cagnotte(cagn, gain):
##    global cagnotte
##    cagnotte = cagn + gain


while cagnotte > 0:
    print(f"Votre cagnotte est de {cagnotte} euros")
    # def poche_user(cagnotte):

    # choix numéro user
    numero = input("""
**********************************************
Choisissez un numéro entre 0 à 49 pour la mise : """)
    numero = int(numero)
    if numero < 0 or numero > 49 or int(numero) == False :
        print("Mauvais choix! Recommencez...")
        numero = input("Choisissez un numéro entre 0 à 49 pour la mise : ")
    else:

        # choix mise user
        mise = input("Faites votre mise : ")
        mise = float(mise)
        if mise <= 0 :
            print("Misez plus!")
            numero = input("Faites votre mise : ")
        elif float(mise) == False :
            print("Misez des sous, pas des paroles!")
            numero = input("Faites votre mise : ")
        elif mise > cagnotte:
            print("Vous n'avez pas les moyens!")
            numero = input("Faites votre mise : ")
        else:
            print(f"Vous avez misé {mise} euros sur le {numero}")


    # Affiche résultat de la roulette
    roulette.roul()
    nbr_lott = int(roulette.nbr_lott)
    print("Résultat roulette : ", nbr_lott)
    pair_impair2.couleur(nbr_lott, numero)
    
    if roulette.nbr_lott == numero :
        print("Numéro EXACT! Vous avez GAGNÉ 3 fois la mise!!!")
        banque.gain_user(mise, 3)
        banque.val_cagnotte(cagnotte, gain)
    elif pair_impair2.stat == 'ok_pair' :
        print("Nbres pairs, vous avez gagné 1/2 fois la mise!")
        gain_user(mise, 0.5)
        val_cagnotte(cagnotte, gain)  
    elif pair_impair2.stat == 'ok_impair' :
        print("Nbres impairs, vous avez gagné 1/2 fois la mise!")
        banque.gain_user(mise, 0.5)
        banque.val_cagnotte(cagnotte, gain)
        print(gain, cagnotte)

    else :
        print("Perdu, retentez votre chance...")
        banque.gain_user(mise, -1)
        banque.val_cagnotte(cagnotte, gain)
        print(gain, cagnotte)
else :
    print("Vous n'avez plus de pépettes! Au revoir :)")



##
# ... placez votre programme ici AVANT les lignes suivantes On met le
# programme en pause pour éviter qu'il ne se referme (Windows)
# os.system("pause")##
