from os import strerror

try:
    src = open('file', 'wt')
    src.write('abAaBcCcc')
    src.close()
except Exception as ex:
    print('Error creating file : ', strerror(ex.errno))
    
try:
    src = open('file', 'rt')
    txt = src.read()
    txt = txt.lower()
    dicto = dict()
    for x in txt:
        if x in dicto.keys():
            dicto[x] += 1
        else:
            dicto[x] = 1
    src.close()
except Exception as ex:
    print('Error reading file : ', strerror(ex.errno))

dicto = dict(sorted(dicto.items(), key = lambda x: x[1], reverse = True))
for k,v in dicto.items():
    print(k,'->',v)