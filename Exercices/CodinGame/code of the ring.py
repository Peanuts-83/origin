magic_phrase = input()
code = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
com = '+-.<>'
res = ''
val = 0
for x in magic_phrase:
    dist = code.index(x)-code.index(code[val])
    for i in range(len(code)+1):
        if x==code[val]:
            res += com[2]
            break
        if -27<=dist<-13 or 0<dist<=13:
            if x==code[val]:
                res += com[0]+com[2]  
                val = val+1 if val<26 else 0
                break
            else:
                res += com[0]
                val = val+1 if val<26 else 0
        else:
            if x==code[val]:
                res += com[1]+com[2]  
                val = val-1 if val>0 else  26
                break
            else:
                res += com[1]
                val = val-1 if val>0 else  26    
print(''.join(res))
