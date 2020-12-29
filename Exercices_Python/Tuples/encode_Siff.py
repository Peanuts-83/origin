'''
    using args[n] , start going bad starting at N = 3
    N : 3
    Args : dddeeeefgghhhhhhh => args[3]  = e 
    Args in loop : dddfgghhhhhhh => e processed in place of d and replaced by '', cause bad index used
    a5b3c18e4 => d missing
    replace put at blank the character processed, so for next loop, we just need to take first coming character
'''
n = 0
def encode(chaine):
    encodage = ''
    while chaine != '':       # tant que args n'est pas vide
        #print('chaine : ' + chaine)
        currentChar = chaine[n] # store indexed value being processed before calling replace method
        encodage = encodage + currentChar + str(chaine.count(currentChar))
        print("chaine before : " + chaine)
        chaine = chaine.replace(currentChar,'')     # on retire à args les lettres comptées
        if len(chaine) != 0:
            print("chaine after : " + chaine)
        else:
            print("chaine empty")
        
    print(encodage)

encode('aaaaabbbccccccccccccccccccdddeeeefgghhhhhhh')
