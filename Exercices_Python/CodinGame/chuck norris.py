import sys
import math

def repr_bin(str, encoding):
     message = ""
     for v in str.encode(encoding):
         message += bin(v)[2:].zfill(7)
     return message

def repr_chuck(message_bin):
    answer = ''
    recurse = '2'
    for n in message_bin:
        if recurse == n:
            answer += '0'
        elif recurse != n:
            if n == '1':
                answer += ' 0'+' 0'
                recurse = '1'
            elif n == '0':
                answer += ' 00'+' 0'
                recurse = '0'
    answer = answer.lstrip()
    return answer


message = input()
message_bin = repr_bin(message,'ascii')


print(repr_chuck(message_bin))