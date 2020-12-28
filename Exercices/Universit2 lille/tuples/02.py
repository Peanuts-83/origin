# -*-coding:latin-1 -*
#import os # On importe le module os



#mois= [('janv',1),('fev',2),('mars',3),('avril',4),('mai',5),('juin',6),
#('juill',7),('aout',8),('sept',9),('oct',10),('nov',11),('dec',12)]
mois = ('janv','fev','mars','avril','mai','juin','juill','aout','sept','oct','nov','dec')

def nom_mois(args):
    print(mois[args-1])


while 1:
    var = int(input('nbr 1-12? '))
    nom_mois(var)
    

# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
