# -*-coding:latin-1 -*
#import os # On importe le module os


def est_divisible(x,y):
    if x%y == 0:
        return True
    else:
        return False

def est_bissextile(annee):
##    if annee%400 == 0 or (annee%4 == 0 and annee%100 != 0):
    if est_divisible(annee,400) or (est_divisible(annee,4) and est_divisible(annee,100)):
        return True
    else:
        return False

def nbre_jours(m,a):                                # nombre de jours dans un mois
    mois = [('janvier',1), ('février',2), ('mars',3), ('avril',4),
            ('mai',5), ('juin',6), ('juillet',7), ('aout',8),
            ('septembre',9), ('octobre',10), ('novembre',11),
            ('décembre',12)]
    for n in range(len(mois)):
        moi_ = (mois[n][1])                         # moi_ = 2eme elt du tuple
        if m == moi_ and m in (1,3,5,7,8,10,12):
            print('Mois de 31 jours')
            val_mois = 31                           # donne le nbre de jour dans le mois
            return val_mois
        elif m == moi_ and m in (4,6,9,11):
            print('Mois de 30 jours.')
            val_mois = 30
            return val_mois
        elif m == moi_ and m == 2:
            if est_bissextile(a) == True :
                print('Mois de 29 jours')
                val_mois = 29
                return val_mois
            else:
                print('Mois de 28 jours.')
                val_mois = 28
                return val_mois    

def est_date_valide(j,m,a):                         # validité du format de date
    date = False
    val_mois = nbre_jours(m,a)
    if val_mois in (28,29,30,31):
        date = True
    else:
        date = False
    if date == True:
        print('Date valide.')
        nom_jour(j,m,a)
    else:
        print('Date invalide.')

def corrige_mois(m,a):                              # valeur corrigée M du mois
    if est_bissextile(a) == True:                       # pour les années bissextiles
        val_corrigee = [3,6,0,3,5,1,3,6,2,4,0,2]
        M = val_corrigee[m-1]
        print(val_corrigee[m-1])
    elif est_bissextile(a) == False:                    # pour les années normales
        val_corrigee = [4,0,0,3,5,1,3,6,2,4,0,2]
        M = val_corrigee[m-1]    
    return M

def num_jour(j,m,a):                                # Valeur du n° du jour de la date renseignée
    long_a = len(str(a))
    if str(a).count('-'):                           # gestion des années négatives
        long_a = long_a - 1
    if long_a >= 4:                                 # année de 4 chiffres ou plus (ex:1853)
        part_annuel = str(a)[-2] + str(a)[-1]
        a_annuel = int(part_annuel)
        part_seculaire = str(a)[-4] + str(a)[-3]
        a_seculaire = int(part_seculaire)
    elif long_a == 3:                               # année de 3 chiffres (ex:672)
        part_annuel = str(a)[-2] + str(a)[-1]
        a_annuel = int(part_annuel)
        part_seculaire = str(a)[-3]
        a_seculaire = int(part_seculaire)
    elif long_a == 2:                               # année de 2 chiffres (ex:24)
        part_annuel = str(a)[-2] + str(a)[-1]
        a_annuel = int(part_annuel)
        part_seculaire = '0'
        a_seculaire = int(part_seculaire)
    elif long_a == 1:                                # année de 1 chiffre (ex:1)
        part_annuel =str(a)[-1]
        a_annuel = int(part_annuel)
        part_seculaire = '0'
        a_seculaire = int(part_seculaire)
    k = a_annuel//4
    q = a_seculaire//4
    ab = a_seculaire
    cd = a_annuel
    M = corrige_mois(m,a)
    jour = (k+q+cd+M+j+2+5*ab)%7                    # Formule de Delambre
    return jour

def nom_jour(j,m,a):                                # Traduction du n° de jour en nom
    num = ('dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche')
    jour = num_jour(j,m,a)
    print('Jour correspondant à la date entrée : ',num[jour])

######################################

# test f° est_date_valide
while 1:
    print('\n',"Validité d'une date".center(50,'*'))
    j = int(input('jour? '))
    m = int(input('mois? '))
    a = int(input('année? '))
    est_date_valide(j,m,a)





# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
