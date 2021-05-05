#!/bin/bash python3
from random import choice
import os, re

# choose mystery word
path = os.path.dirname(__file__)                # path of current file
with open(f'{path}/mots.txt', 'r') as mots:
    mots = mots.read()                          # word in list from mots.txt
    mystery = choice(mots.split())

class Pendu:
    mot = ['-' for _ in range(len(mystery))]
    def __init__(self, chances=7):
        self.n = chances
    
    def run(self):
        while self.n > 0:
            win = False
            print('n: ', self.n)
            for letter in self.mot:
                print('\033[31m'+ letter , end='')      # '\033[31m' > red
            print(f' ({self.n} chances)')
            new_letter = input('\033[39m'+ 'Entrez une lettre: ').upper()    # '\033[39m' > couleur par defaut
            
            # eval given letter
            if new_letter not in mystery:
                self.n -= 1
            else:
                for num in re.finditer(new_letter, mystery, flags=re.IGNORECASE):
                    self.mot[num.start()] = num.group()
            
            # victory
            if not '-' in self.mot:
                win = True
                break
            
        if win == True:
            print(mystery)
            print('Gagné!')
        else:
            print('Looser!!!')
        

p = Pendu()
p.run()