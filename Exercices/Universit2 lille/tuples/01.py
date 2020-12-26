# -*-coding:latin-1 -*
#import os # On importe le module os

########### faire parler TUX ##########

def tux_say(args):
##    print(args)
    t = args
##    print('t1-',t,type(t))
    if len(t) > 1:
        length_longest(args)
    else:                       # affectation de '?' à args si vide
        args = '?'
        length_longest(args)
##        print(len(t))


def length_longest(args):
    t = args
##    print('t2-',t,type(t))
    msg = tuple()
##    print('msg-',msg,type(msg))
    long = 0
    n_phrase = 0
    for i in range(len(t)):     # éval° de la plus grande chaine du tuple
        msg = msg + (t[i],)
        if len(t[i]) > long:    # on défini chaque ligne de msg avec sa longueur
            long = len(t[i])
            n_phrase = i
            if long == 1:       
                long = -1
##    print('msg final-',msg,type(msg))     
##    print('long-',long,' n° de phrase',n_phrase)
    dash_line(long)             # impression de la bulle
    msg_line(msg,long)          #
    dash_line(long)             #
    print(TUX)

def dash_line(n_tirets):        # ligne de traits horizontaux
    bulle_h = ''.center(n_tirets+6, '-')
    bulle_h = ' '+bulle_h+' '
    print(bulle_h)

def msg_line(msg,long):         # txt + traits verticaux
    for i in range(len(msg)):
        print('|  ',msg[i].center(long,' '),'  |')
    
    



while 1:            # Boucle d'input des paroles de TUX
        
##    tux_say (("Cher-e-s étudiant-e-s,", "", "Vous programmez très bien !"))
    # Dessin de TUX #
    TUX = "   \\\n    \\\n        .--.\n       |o_o |\n       |:_/ |\n      //   \\ \\\n     (|     | )\n    /'\_   _/`\\\n    \___)=(___/"
    

##    tux_say(('azerty','qssdfghh'))
    
    var = input('Tux dit ( format"xxx","xxx")? ')
    var = var.split('"')
    var = [n for n in var if n != "" and n != "," and n !=","]  # liste
    tux_say(var)



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
