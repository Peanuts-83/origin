#-*-coding:latin-1 -*-
#import os # On importe le module os

############### TP string - ADN ################

#1/ verif° validité chaine ADN (bases A-T-G-C)
def estADN(chaine):
    if len(chaine) > 0 and len(chaine)%3 == 0:
        for i in chaine:
            if i not in ('A','T','C','G'):
                print('chaine ADN non valide.')
                return False
        else:
            return True
    elif len(chaine)%3 != 0:
        print('chaine ADN non valide.')
        return False
    else:
        return True

#2/ Transcription ADN>ARN en passant bases T en U  
def transcrit(chaine):
    chaineARN = chaine.replace('T','U')
    return chaineARN
    

#3/4/ base compl de la chaine // A-T et C-G // avec inversion miroir
def baseComplementaire(chaine):
    if estADN(chaine) == True:
        a = ''
        for i in chaine:
            if i == 'A':
                a = 'T' + a
            elif i == 'T':
                a = 'A' + a
            elif i == 'C':
                a = 'G' + a
            elif i == 'G':
                a = 'C' + a
        chaineCompl = a
        return chaineCompl
    else:
        print('chaine ADN non valide.')

#5/ nbr occurrences codon de 3 elts // GCU, AGC, UAG etc... dans chaine ARN
def nombreOccurrencesCodon(codon,chaineARN):
    print(chaineARN)
    if len(chaineARN)%3 == 0:
        chaine_splited = ''
        for i in range(len(chaineARN)):        # sequençage de la chaine en triplets
            if i%3 != 0 or i == 0:
                chaine_splited = chaine_splited + chaineARN[i]
            else:
                chaine_splited = chaine_splited + ',' + chaineARN[i]
        #print(chaine_splited)
        nbr_codons = chaine_splited.count(codon)
        print('Il y a ',nbr_codons,' codons ',codon,' dans la chaine',chaineARN,'.')
    else:
        print('Chaine ARN non valide.')


#6/ Mise en application des f°
while 1:
    print('\n',''.center(50,'*'))
    chaine = input('Entrez une séquence ADN : ')
    estADN(chaine)
    print('\n')
    codon = input('Entrez un codon : ')


    print('Séquence complémentaire-inversée : ',baseComplementaire(chaine))
    print('Séquence ARN : ',transcrit(chaine))
    nombreOccurrencesCodon(codon,transcrit(chaine))





    


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
