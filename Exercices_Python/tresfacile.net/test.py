#-*-coding:latin-1 -*-
# coding: utf-8
#!/usr/bin/python

print('#############################################')

# 48 // quotient et reste
def q_r(a, b):
    div = (str(a/b)).split('.')
    q = div[0]
    r = div[1]
    print(q, r)
    return (q, r)

# 49 // Plus Grand Denominateur Commun
def pgcd(a, b):     # algo d'Euclide, denominateur est le diviseur quand reste = 0
    denominateur = 1    
    temp_denom = 1
    if a < b:
        while temp_denom > 0:
            denominateur = b//a
            temp_denom = b%a
            b = a
            a = temp_denom
        print('b',b)
        return b
    if a > b:
        while temp_denom > 0:
            denominateur = a//b
            temp_denom = a%b
            a = b
            b = temp_denom
        print('a',a)
        return a



# 50 // Plus Petit Multiplicateur Commun
def ppcm(a,b):      # ppcm = a*b/pgcd
    val = pgcd(a,b)
    val = (a*b)/val
    print(val)
    return(val)

# 52 // nbre premier
def premier(n):
    num_prem = ''
    for i in range(n):
        if i<2 or n%i !=0:
            num_prem = True
        else:
            num_prem = False
            print(num_prem)
            return num_prem
    print(num_prem)
    return num_prem

# 53 liste les nbres premiers dans l'intervale / CU: m<n
def liste_premier(m,n):
    m_n = []
    for i in range(abs(m-n)+1):
        if premier(m+i) == True:
            m_n.append(m+i)
    print(m_n)
    return m_n

# 54 // le seul diviseur commun à a et b est 1
def premier_entre_eux(a,b):
    liste_a = []
    liste_b = []
    for i in range(a+1):
        if i != 0:
            if a%i == 0:
                liste_a.append(i)
    for i in range(b+1):
        if i != 0:
            if b%i == 0:
                liste_b.append(i)
    print(liste_a, liste_b)
    div_commun = list()
    for val in liste_a:
        if val in liste_b:
            div_commun.append(val)
    print('diviseurs communs aux deux nombres ',div_commun)
    return div_commun
# premier_entre_eux(5,24)

# 55 // identité de Bezout / ua + vb =1
def bezout():
    a_b = input('Entrer 2 entiers :')
    a_b = a_b.split(',')
    print((a_b[0],a_b[1]))
    if (premier_entre_eux(int(a_b[0]),int(a_b[1]))) == [1]:
        print('Nombres premiers entre eux.')
    else:
        print('Nombres non valides')
# bezout(8,24)

# 56 // diviseurs impairs de 3570 multiples de 3 dans [500:2500]
def div_impair(a):
    
    liste = tuple()
    for i in range(a):
        if i>0 and a%i == 0:
            if i%3 == 0:
                if i>500 and i<2500:
                    liste = liste + (str(i),)
    val = ', '.join(liste)
    print('Les diviseurs impairs de 3570 multiples de 3 dans [500:2500] sont :',
    '\n',val)
# div_impair(3570)

# 57 // 
