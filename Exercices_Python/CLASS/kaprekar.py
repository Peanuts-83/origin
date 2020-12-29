def kaprekar(n):
    carre = n**2
    for i in range(1, len(str(carre))):
        a, b = int(str(carre)[:i]), int(str(carre)[i:])
        if a+b == n:
            return 'KAPREKAR'
    return 'PAS KAPREKAR'

print(kaprekar(45))
print(kaprekar(12))

def algo_kaprekar(n):
    a = int(''.join(sorted(str(n), reverse=True)))
    b = int(''.join(sorted(str(n))))
    temp = []
    while 1:
        c = a-b
        if c not in temp:
            temp.append(c)
            c = str(c)
        else:
            return int(c)
        if int(c) < 10:
            c = '0'+str(c)
        a = int(''.join(sorted(c, reverse=True)))
        b = int(''.join(sorted(c)))

print(algo_kaprekar(326))
print(algo_kaprekar(34))