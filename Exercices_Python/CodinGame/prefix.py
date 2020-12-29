table = {b:chr(int(c)) for b,c in [input().split() for i in range(int(input()))]}
encoded = input()
decoded = ""
start = 0

for end in range(1,len(encoded)+1):
    if encoded[start:end] in table:
        decoded += table[encoded[start:end]]
        start = end

print([decoded, f"DECODE FAIL AT INDEX {start}"][start!=end])

############################

n = int(input())
table = dict()

for i in range(n):
    b, c = input().split()
    table[b] = chr(int(c))

s = input()
res, buf = "", ""

for i, c in enumerate(s):
    buf += c
    if buf in table:
        res += table[buf]
        buf = ""

print(res if not buf else f"DECODE FAIL AT INDEX {i - len(buf) + 1}")

### LE MIEN #########################

n = int(input())

code = []
for i in range(n):
    b, c = input().split()
    c = int(c)
    code.append((b,c))
s = input()

decode = []
r = 0
try:
    for j in range(len(s)):
        validate = 0
        for i in range(n):
            if code[i][0] in s[r:r+len(code[i][0])] :
                decode.append(chr(code[i][1]))
                r += len(code[i][0])
                validate = 1
        if r != len(s) and validate == 0:
            raise ValueError     
    print(''.join(decode))
except ValueError:
    print(f"DECODE FAIL AT INDEX {r}")
