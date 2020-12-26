# -*-coding:latin-1 -*
#import os # On importe le module os

#def mostfrequent(*args):
t = "Les listes, les dictionnaires et les tuples sont des exemples de structures de donn�es ; dans ce chapitre, nous commen�ons � d�couvrir les structures compos�es de donn�es, comme les listes de tuples, ou les dictionnaires qui contiennent des tuples comme cl�s et des listes comme valeurs. Les structures compos�es de donn�es sont utiles, mais elles sont sujettes � ce que j'appelle des erreurs de forme, c'est-�-dire des erreurs provenant du fait qu'une structure de donn�es n'a pas le bon type, la bonne taille ou la bonne constitution. Par exemple, si vous vous attendez � une liste contenant un nombre entier et je vous donne un simple entier (qui ne se trouve pas dans une liste), cela ne fonctionnera pas."
print(t)

dico = {}
for n in t:                         # string en dictionnaire elt:val
    if n not in dico.keys():
        dico[n] = t.count(n)
print(dico)

cles = [n for n in dico]            # 1 dict en 2 listes
vals = [dico[n] for n in dico]
print('cl�s :',cles,'\n','vals :',vals)
liste = [(a, b) for a, b in zip(cles, vals)]    # 2 liste en 1 liste de tuples
print('\n', 'liste :', liste)

# tri par sorted/lambda (ici tri par valeur)
print('\n','liste double tri�e par valeur puis par cl�e :'.center(75,'*'),
      '\n', sorted(s, key=lambda val : val[1]))

# tri complexe (double) par sorted/operator.itemgetter
from operator import itemgetter, attrgetter 
print('\n',sorted(liste, key=itemgetter(1,0)))  # tri par valeur puis par cl�e



# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour �viter qu'il ne se referme (Windows)
#os.system("pause")
