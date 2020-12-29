def square(num):
    return num * num

square_lambda = lambda num : num * num
assert square(3) == square_lambda(3)

# map ### pour un iterable, chaque terme est traité
domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain) # nom de l'iterable en 2eme arg
print(list(our_range))
>>> [2, 4, 6, 8, 10]    # liste de l'iterable

# filter ### pour un itérable, retourne termes filtrés
domain = [1, 2, 3, 4, 5]
evens = filter(lambda num: num % 2 == 0, domain) # nom de l'iterable en 2eme arg
print(list(evens))      # liste de l'iterable
>>> [2, 4]

# reduce ### import necessaire
from functools import reduce
domain = [1, 2, 3, 4, 5]
the_sum = reduce(lambda acc, num: acc + num, domain, 0) # 0 pour 1ere val de acc
print(the_sum)

# sort & sorted with lambdas ###
words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
words.sort(key=str.lower)
print(words)