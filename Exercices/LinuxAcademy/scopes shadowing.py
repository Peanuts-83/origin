### SCOPES (espaces) and shadowing #####

y = 5

def set_x(y):
    print('Inner y:', y)
    x = y
    y = x//2

set_x(10)

print('Outer y:', y)