# 1. Write a Python program to create a tuple.
t = tuple()
print('1. Create:', t)

# 2. Write a Python program to create a tuple with different data types.
t = ('text', 1, True, 5.4)
print('2. Diff data types:', t)

# 3. Write a Python program to create a tuple with numbers and print one item.
t = tuple(x for x in range(5))
print('3.', t)

# 4. Write a Python program to unpack a tuple in several variables.
a,b,c,d,e = t
print('4.', 'a=',a,'b=',b,'c=',c,'d=',d,'e=',e)

# 5. Write a Python program to add an item in a tuple.
t = t + (a,)
t += t[:3]
print('5. Add:', t)

# 6. Write a Python program to convert a tuple to a string.
t = ('a','e','i','o','u')
s = ' '.join(t)
print('6. convert to string:', s)

# 7. Write a Python program to get the 3rd element and 4th element from last of a tuple.
print('7.', t[2:4])

# 8. Write a Python program to create the colon(independant copy) of a tuple.
from copy import deepcopy
t = ('a',[],5,'o','u')
t2 = tuple(t)
t3 = deepcopy(t)
t2 += ('b',); t2[1].append(20)
t3 += ('c',); t3[1].append(30)
print('8. Deepcopy:', t, t2, t3)

# 9. Write a Python program to find the repeated items of a tuple.
t = 2, 4, 5, 6, 2, 3, 4, 4, 7
print('9. Count:', t.count(4))

# 10. Write a Python program to check whether an element exists within a tuple.
t = 2, 4, 5, 6, 2, 3, 4, 4, 7
print('10. Is in:', 8 in t, 4 in t)

# 11. Write a Python program to convert a list to a tuple.
l = ['a', 'b', 'c']
print('11. List to tuple:', tuple(l))

# 12. Write a Python program to remove an item from a tuple.
def suppr(t, item):
    t = t[:item] + t[item+1:]
    return t
print('12. Suppr:', suppr(t,2), suppr(t3,2))

# 13. Write a Python program to slice a tuple.
print('13. Slice:', t[5:])

# 14. Write a Python program to find the index of an item of a tuple.
print('14. Index of item:', t.index(6))

# 15. Write a Python program to find the length of a tuple.
print('15. Length:', len(t))

# 16. Write a Python program to convert a tuple to a dictionary.
t = ((2,'w'),(5,'z'))
print('16. Tuple to dictionnary:', {key:val for val,key in t})

# 17. Write a Python program to unzip a list of tuples into individual lists.
t = [('a','b','c'),(1,2,3),('d','e',[8])]
print('17. Unzip to lists:', list(zip(*t)))

# 18. Write a Python program to reverse a tuple.
t = ('a', 'b', 'c', 'd')
print('18. Reverse:', t[::-1], tuple(reversed(t)))

# 19. Write a Python program to convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a,b in l:
    d.setdefault(a, []).append(b)
print('19. List of tuples to dict:', d)

# 20. Write a Python program to print a tuple with string formatting.
t = (100, 200, 300)
print(f'20. String: This is a tuple {t}')

# 21. Write a Python program to replace last value of tuples in a list.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print('21. Replace last:', list(map(lambda x: x[:2]+(100,), l)))


# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.
l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l2 = [a for a in l if a ]
print('22. ', l2)

# 23. Write a Python program to sort a tuple by its float element.
l = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print('23. Sort by float:', sorted(l, key=lambda x: x[1], reverse=True))

# 24. Write a Python program to count the elements in a list until an element is a tuple.
l = num = [10,20,30,(10,20),40]
county = 0
for a in l:
    if isinstance(a, tuple):
        break
    else:
        county += 1
print('24. Count till tuple:', county )
