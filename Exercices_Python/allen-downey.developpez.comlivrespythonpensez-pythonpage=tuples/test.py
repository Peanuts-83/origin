# -*-coding:latin-1 -*
#import os # On importe le module os

#def mostfrequent(*args):
t = "Les listes, les dictionnaires et les tuples sont des exemples de structures de données ; dans ce chapitre, nous commençons à découvrir les structures composées de données, comme les listes de tuples, ou les dictionnaires qui contiennent des tuples comme clés et des listes comme valeurs. Les structures composées de données sont utiles, mais elles sont sujettes à ce que j'appelle des erreurs de forme, c'est-à-dire des erreurs provenant du fait qu'une structure de données n'a pas le bon type, la bonne taille ou la bonne constitution. Par exemple, si vous vous attendez à une liste contenant un nombre entier et je vous donne un simple entier (qui ne se trouve pas dans une liste), cela ne fonctionnera pas."
print(t)

dico = {}
for n in t:                         # string en dictionnaire elt:val
    if n not in dico.keys():
        dico[n] = t.count(n)
print(dico)

cles = [n for n in dico]            # 1 dict en 2 listes
vals = [dico[n] for n in dico]
print('clés :',cles,'\n','vals :',vals)
liste = [(a, b) for a, b in zip(cles, vals)]    # 2 liste en 1 liste de tuples
print('\n', 'liste :', liste)

# tri par sorted/lambda (ici tri par valeur)
print('\n','liste double triée par valeur puis par clée :'.center(75,'*'),
      '\n', sorted(s, key=lambda val : val[1]))

# tri complexe (double) par sorted/operator.itemgetter
from operator import itemgetter, attrgetter 
print('\n',sorted(liste, key=itemgetter(1,0)))  # tri par valeur puis par clée



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
