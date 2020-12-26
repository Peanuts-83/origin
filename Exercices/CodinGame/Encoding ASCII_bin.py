import sys
import math

message = input()
# message.encode('ascii')
message = ''.join(bin(ord(x))[2:].zfill(7) for x in message)    # binary conversion
# The bin function converts an integer to binary.
# The ord f° gives unicode value of string
# The [2:] strips the leading 0b. 
# The .zfill(7) pads each byte to 7 bits.

sortie = ''
recurse = ''
for i in message:       # turns 1 in 0 and 0 in 00
    if recurse == i:
        sortie += '0'
    elif recurse != i:
        if i == '1':
            sortie += ' 0'+' 0'
            recurse = '1'
        elif i == '0':
            sortie += ' 00'+' 0'
            recurse = '0'
    sortie = sortie.lstrip()        # takes out first 0
print(sortie)

