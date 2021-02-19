
a = lambda x: x+15
b = lambda x,y: x*y
c = lambda x: x*15
d = sorted([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)], key=lambda x: x[1])
print(a(4), b(2,3), c(3), d)

e = sorted([{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}], key=lambda x: x['color'])
print(e)

f = list(filter(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
g = list(filter(lambda x: x%2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f, g)

h = list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
i = list(map(lambda x: x**3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(h, i)

j = lambda x,y: x[0] == y
print(j('azerty','a'), j('azerty','z'))

k = lambda x: ' '.join(x.split('-')).split(' ')
print(k('2020-01-15 09:03:32.744178'))
import datetime
now = datetime.datetime.today()
year = lambda x: x.year; month = lambda x: x.month; day = lambda x: x.day
time = lambda x: x.time()
print(year(now), month(now), day(now), time(now))

l = lambda x: type(eval(x)) == int or type(eval(x)) == float
print(l('5.2'), l('-8'))

from functools import reduce
#                         2 args given v                 from initializer v
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [1, 1])
print("Fibonacci series upto 8:")
print(fib_series(8))

a = [1, 2, 3, 5, 7, 8, 9, 10]; b = [1, 2, 4, 8, 9]
m = list(filter(lambda x: x in b, a))
print('[a] in [b]: ', m)
