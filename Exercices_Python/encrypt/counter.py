#! bin/bash python3
import os, re, json, argparse

# define var for txt1 & txt2 as args
parser = argparse.ArgumentParser()
parser.add_argument('txt1', help='Reference txt to evaluate', type=str)
parser.add_argument('txt2', help='Txt to decode', type=str)
parser.add_argument('-txt3', help='Third txt to encrypt', type=str)
args = parser.parse_args()

os.chdir(os.getcwd())       # set py dir to cwd

class Txt:
    
    def __init__(self, txt):
        self.txt = txt
        self.letters = {}
        self.ref_letter = ''
        
    def eval_txt(self):
        # open and count/sort letters    
        with open(self.txt, 'r') as txt:
            search_letter = re.findall('[a-z]|[A-Z]', txt.read(), flags=re.IGNORECASE)
            for let in search_letter:
                if let in self.letters:
                    self.letters[let] += 1
                else:
                    self.letters[let] = 1
        self.letters = dict(sorted(self.letters.items(), key = lambda x: x[1], reverse=True))
        print(f'sorted letters for {self.txt}:', self.letters)
        
        # reference letter
        self.ref_letter = list(self.letters.keys())[0]
        print('ref_letter: ', self.ref_letter)

        # save dict in json
        with open('stats.json', 'a') as txt:
            txt.write(f'Statistique de présence des lettres dans {self.txt}:\n\n')
            txt.write(json.dumps(self.letters))
            txt.write('\n\n')
            
    def decrypt(self, ref):
        diff = ord(self.ref_letter) - ord(ref)
        with open(self.txt, 'r') as txt:
            crypted = [ord(n) for n in txt.read()]
        decrypted = []
        for n in crypted:
            if n >= 65 and n <= 90:
                if (n-diff) < 65:
                    decrypted.append(chr(n-diff +26))
                elif (n-diff) > 90:
                    decrypted.append(chr(n-diff -26))
                else:
                    decrypted.append(chr(n-diff))
            else:
                decrypted.append(chr(n))
        for n in decrypted:
            print(n, end='')
            
    def encrypt(self, decal):
        with open(self.txt, 'r') as txt:
            decrypted = [ord(n) for n in txt.read()]
        crypted = []
        for n in decrypted:
            if n >= 65 and n <= 90:
                if (n-decal) < 65:
                    crypted.append(chr(n-decal +26))
                elif (n-decal) >90:
                    crypted.append(chr(n-decal -26))
                else:
                    crypted.append(chr(n-decal))
            else:
                crypted.append(chr(n))
        for n in crypted:
            print(n, end='')
            
            
print(args)        
first_txt = Txt(args.txt1)
second_txt = Txt(args.txt2)
first_txt.eval_txt()
second_txt.eval_txt()
print('\n*** traduction du second txt ***\n')
second_txt.decrypt(first_txt.ref_letter)
print('\n\n*** encryptage du 3eme txt ***\n')
third_txt = Txt(args.txt3)
third_txt.encrypt(5)
