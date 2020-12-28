#-*-coding:latin-1 -*-
#import os # On importe le module os


# imprimer 5 lignes vides sans boucle
print('\n','\n','\n','\n','\n')

# impression verticale
def impr_vert(args):
    for i in range(len(args)):
        print(args[i])

# longueur de chaine
def my_len(args):
    n = 0
    for i in args:
        n += 1
    print(n)

# tirets ins�r�s dans la chaine
def tirets(args):
    t = '-'.join(tuple(args))
    t2 = str(t).replace(' -',' ')
    print(t,'\n',t2)

# miroir
def miroir(args):
    a = str()
    for n in range(len(args)):
        a = a + args[-n-1]
    return a
    print(a)

# palindrome
def est_palind(args):
##    t1 = ''
##    t2 = ''
##    for n in range(len(args)):      # comparaison de 2 chaines
##        t1 = t1 + args[n]
##        t2 = t2 + args[-n-1]
##    print(t1, t2)
##    if t1 == t2:
##        print(True)
##        return True
##    else:
##        print(False)
##        return False
    # ou en utilisant la fonction 'miroir' au-dessus
    print('args',args,' - miroir',miroir(args))
    if args == miroir(args):
        print(True)
        return True
    else:
        print(False)
        return False

# suppression occurences d'un caract�re
def suppr_occ_caract(c,chaine):
    chaine2 = chaine.replace(c,'')
    return chaine2
    
##a = suppr_occ_caract(' ','esope reste ici et se repose')
##a = est_palind(a)
##print(a)

# en maj
def mettre_maj(args):
    a = ''
    for n in range(len(args)):
        if args[n] in ('�������'):
            a = a + (args[n])
        else:
            a = a + (args[n].upper())    
    print(a)

# en min
def mettre_min(args):
    a = ''
    for n in range(len(args)):
        if args[n] in ('�������'):
            a = a + (args[n])
        else:
            a = a + (args[n].lower())    
    print(a)

# modifier la casse
def min_maj(args):
    a = ''
    for n in args:
        if n in ('�������'):
            a = a + n
        elif n in ('�������'):
            a = a + n
        else:
            a = a + n.swapcase()    
    print(a)

# comparaison de chaine
def comparer_chaines(a,b):
    if a == b :
        print('0')
    else:
        if a > b :
            print(1)
        else:
            print(2)

# rechercher caractere
def search_caract(chaine,i):
    if i in chaine:
        print(chaine.index(i))
    else:
        print('-1')

# nbr occurences
def nbr_occurences(chaine,i):
    if i in chaine:
        print(chaine.count(i))
        return chaine.count(i)
    else:
        print('0')
        return '0'

# caractere le plus frequent
def plus_frequent(chaine):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    max_i = 0
    lettre_i = ''
    for i in chaine:
        if i in alphabet:
            if chaine.count(i) > max_i:
                max_i = chaine.count(i)
                lettre_i = i
    print(f'la lettre "{lettre_i}" est r�p�t�e {max_i} fois.')

def plus_frequent2(chaine):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    max_i = list()
    for i in chaine:
        if i in alphabet:
            alphabet = alphabet.replace(i,'')
            max_i.append((i, nbr_occurences(chaine,i)))
    max_i = sorted(max_i, key=lambda x : x[1], reverse = True)  # tri de liste par le 2eme elt du tuple
    print(f'la lettre "{max_i[0][0]}" est r�p�t�e {max_i[0][1]} fois.')

# suppression de caractere
def suppr_caract(chaine,i):
    if i >= 0 and i <= len(chaine):
        chaine = chaine.replace(chaine[i],'')
        print(chaine)
    else:
        print(chaine)

def suppr_caract2(chaine,i):
    if i <= len(chaine) and  i >= 0:
        chaine = chaine.replace(chaine[i],'')
        print(chaine)
    elif i >= -len(chaine) and i < 0:           # gestion index negatifs
        chaine = chaine.replace(chaine[i],'')
        print(chaine)     
    else:
        print(chaine)

# insertion caractere
def insert_caract(chaine,index,n):
    a = ''
    if index > 0 and index <= len(chaine):
        for i in range(len(chaine)):
            if i == index:
                a = a + n + chaine[i]
            else:
                a = a + chaine[i]
        print(a)
    else:
       print(chaine) 
    
# remplacement de caractere
def rempl_caract(chaine,index,n):
    chaine = chaine.replace(chaine[index],n)
    print(chaine)
        
# remplacement d'occurences d'une chaine dans une autre chaine
def rempl_occ(chaine1,n,chaine2):
    chaine1 = chaine1.replace(n,chaine2)
    print(chaine1)



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
