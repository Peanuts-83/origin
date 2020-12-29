# -*-coding:latin-1 -*
#import os # On importe le module os

note = input('entrer note/total : ')

note_tot = tuple(note.split('/'))
print(note_tot)
pourc_note = int(note_tot[0])*100/int(note_tot[1])
print('note ',note,' vaut : ',pourc_note,'%')


# ... placez votre programme ici AVANT les lignes suivantes
# On met le programme en pause pour éviter qu'il ne se referme (Windows)
#os.system("pause")
