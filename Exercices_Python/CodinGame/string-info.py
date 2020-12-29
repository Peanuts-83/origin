a = input('Enter a message: ')
first = 'First character: '+ a[0]
last = 'Last character: '+ a[-1]
middle = 'Middle character: '+ a[len(a)//2]
even = 'Even index character: '+ a[0::2]
odd = 'Odd index character: '+ a[1::2]
rev = 'Reversed character: '+ a[::-1]

print('\n',first,'\n',last,'\n',middle,'\n',even,'\n',odd,'\n',rev)