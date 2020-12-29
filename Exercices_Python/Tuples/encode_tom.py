# -*-coding:latin-1 -*
#import os # On importe le module os




def encode(args):
     encodage = ''
     n = 0
     while args != '':       # tant que args n'est pas vide
         print(args)
         encodage = encodage + args[0] + str(args.count(args[0]))
         print('n-',n,'args[0]',args[0],'args.count(args[0])-',args.count(args[0]))

         args = args.replace(args[0],'')     # on retire à args les lettres comptées
         print(encodage)
         n +=1
         
     print(encodage)

encode('aaaaabbbccccccccccccccccccdddeeeefgghhhhhhh')
    


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
