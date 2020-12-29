

var = 20#int(input('How many values should we process? '))
res = ''
if var > 0:
    for i in range(1,var):
        
        if i%3 == 0 and i%5 == 0:
            res += 'FizzBuzz,'
        elif i%3 == 0:
            res += 'Fizz,'
        elif i%5 == 0:
            res += 'Buzz,'
        else:
            res += str(i)+','
res = res.split(',')
res = '\n'.join(res)
print(res)