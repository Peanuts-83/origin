import re

def arithmetic_arranger(*args):
  for x in args[0]:
    parts = x.split()
    print(parts)
    larg = int(''.join([max(len(x)) for x in parts]))
    for x in parts:
      if len(x) < larg+1 and parts.index(x) != 1:
        x = '0'*(larg+1-len(x)) + x
        parts[parts.index(x)] = x
    print(parts)



    # return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])