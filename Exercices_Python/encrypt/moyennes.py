#! bin/bash python3
import os, csv, json

# extract csv to convert
convert = []
with open('notes.csv', 'rt') as notes:
    lecteur = csv.reader(notes, delimiter=(';'))
    for n in lecteur:
        convert.append(n)
        
# calculate averages 
moy = {}; count = 0
for matiere in convert[0]:
    sum_mat = [int(n[count]) for n in convert if n[count].isnumeric()]
    moy[matiere] = round(sum(sum_mat) / len(sum_mat), 2)
    count += 1
moy_sum = [value for key, value in moy.items()]
moy['Moyenne générale'] = round(sum(moy_sum) / len(moy_sum), 2)
print(moy)

# send averages to json file
with open('moyennes.json', 'wt') as txt:
    txt.write(json.dumps(moy))

