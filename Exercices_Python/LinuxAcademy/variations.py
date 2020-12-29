#! /usr/bin/env python3.7
import os

var = input('Enter a message: ')

low = 'Lowercase: '+ var.lower()
upp = 'Uppercase: '+ var.upper()
cap = 'Capitalized: '+ var.capitalize()
titl = 'Title Case: '+ var.title()
words = 'Words: '+ str(var.split(' '))
alpha_1 = 'Alphabetic First Word: '+ str(var.split(' ')[0])
alpha_9 = 'Alphabetic Last Word: '+ str(var.split(' ')[-1])
 
print('\n',low,'\n',upp,'\n',cap,'\n',titl,'\n',words,'\n',alpha_1,'\n',alpha_9)
os.system("pause")