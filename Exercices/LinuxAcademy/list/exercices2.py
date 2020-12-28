# 69. Write a Python program to remove duplicates from a list of lists.
l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l2 = []
for x in l:
    if x not in l2: l2.append(x) 
print('69. Remove duplicates:', l2 )

from itertools import groupby
l.sort()
l3 = [l for l,_ in groupby(l)]
print('   ', l3)

# 70. Write a Python program to get the depth of a dictionary.
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print('70. Dict depth:',dict_depth(dic))

# 71. Write a Python program to check whether all dictionaries in a list are empty or not.
def empty(liste):
    for x in liste:
        return True if len(x)==0 else False
a, b = [{},{},{}], [{1,2},{},{}]
print('71. Dicts empty:', empty(a), empty(b), all(not d for d in a), all(not d for d in b))

# 72. Write a Python program to flatten a given nested list structure.
l1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l2 =[]
for x in l1:
    if isinstance(x, int): l2.append(x)
    elif isinstance(x, list): l2 += x
print('72. Flatten list:', l2)

# 73. Write a Python program to remove consecutive duplicates of a given list.
from collections import Counter
l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
count_l1 = Counter(l1)
l2 = [x for x in count_l1]
from itertools import groupby
l3 = [ key for key, num in groupby(l1)]
print('73. Remove duplicates:', list(set(l1)), l2, l3)

# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
from itertools import groupby
l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print('74. Group duplicates:', [list(num) for key, num in groupby(l1)])

# 75. Write a Python program to create a list reflecting the run-length encoding 
# from a given list of integers or a given list of characters.
l1 = [1, 1, 2, 3, 4, 4.3, 5, 1]
l2 = 'comment'
print('75. Run-length:', [[len(list(num)), key] for key, num in groupby(l1)], 
[(len(list(num)), key) for key, num in groupby(l2)])

# 76. Write a Python program to create a list reflecting the modified run-length encoding 
# from a given list of integers or a given list of characters.
l1 = [1, 1, 2, 3, 4, 4, 5, 1]
l2 = 'aabcddddadnss'
def counter(liste):
    return [[len(list(num)), key] if len(list(num))>1 else key for key, num in groupby(liste)]
print('76.Run-length2:', counter(l1), counter(l2))

# 77. Write a Python program to decode a run-length encoded given list.
l1 = [[2, 1], 2, 3, [3, 4], 5, 1]
def decount(liste):
    l2 = []
    for x in liste:
        if isinstance(x, list):
            l2 += [x[1] for _ in range(x[0])]
        elif isinstance(x, int):
            l2.append(x)
    return l2
print('77. Decoder:', decount(l1))

# 78. Write a Python program to split a given list into two parts where the length 
# of the first part of the list is given.
l1 = [1,2,3,4,5,6,7,8,9]
def splitter(l, length):
    return [l[:length], l[length:]]
print('78. Split list:', splitter(l1, 5))

# 79. Write a Python program to remove the K'th element from a given list, print the new list.
l1.remove(8)
l1.pop(2)
del l1[5]
print('79. Remove Kth elt:', l1)

# 80. Write a Python program to insert an element at a specified position into a given list.
l1.insert(3,10)
print('80. Insert at index:', l1)

# 81. Write a Python program to extract a given number of randomly selected elements from a given list. 
from random import randint
l1 = [1,2,3,4,5,6,7,8,9]
def extract(l, num):
    return [l[n] for n in [randint(0, len(l)-1) for _ in range(num)]]
print('81. Extracts 3 random elets:', extract(l1,3))

# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
from itertools import combinations
l1 = [1,2,3,4,5,6,7,8,9]
print('82. Combinations:',  list(combinations(l1,2)))

# 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied 
# by the length of the list.
l1 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
print('83. Num_round * length:', (sum([round(x) for x in l1]))*len(l1), sum(list(map(round, l1)))*len(l1))

# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers 
# and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
l1 = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print(f'84. Num max is {max([round(x) for x in l1])} and num min is {min([round(x) for x in l1])}')
print('    list *5 :', sorted(list(map(lambda x: round(x)*5, l1))))

# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
print('85. Multidim list:', [[[0 for _ in range(3)] for _ in range(5)] for _ in range(2)])

# 86. Write a Python program to create a 3X3 grid with numbers.
print('86.', [[n for n in range(1,4)]for _ in range(3)])

# 87. Write a Python program to read a matrix from console and print the sum for each column. 
# Accept matrix rows, columns and elements for each column separated with a space(for every row) 
# as input from the user.
# standard_input = 3,3,'1 2 3','4 5 6', '7 8 9'
# row, col = int(input('row:')), int(input('col:'))
# array = [[0]* col for row in range(row)]
# for r in range(row):
#     lines = list(map(int, input('vals:').split(' ')))
#     for c in range(col):
#         array[r][c] = lines[c]
# print('87. Array1:')
# for x in array:
#     print(x)
# print(list(map(lambda x: x, array)))
# sum = [0]*c
# for c in range(col):
#     for r in range(row):
#         sum += array[r][c]

# 89. Write a Python program to Zip two given lists of lists.
l1 = [[1, 3], [5, 7], [9, 11]]
l2 = [[2, 4], [6, 8], [10, 12, 14]]
a = list(zip(l1,l2))
print('89.', list(map(lambda x: x[0]+x[1], a)))

res = list(map(list.__add__, l1, l2))
print('   ', res)

# 90. Write a Python program to count number of lists in a given list of lists.
l1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
print('90. Number of elts:', len(l1))

# 91. Write a Python program to find the list with maximum and minimum length.
l1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
liste = list(sorted(l1, key=lambda x: len(x)))
print('91. Max length:', liste[-1], 'Min length:', liste[0])

# 92. Write a Python program to check if a nested list is a subset of another nested list.
def nested(l1, l2):
    return all(map(l1.__contains__, l2))
l1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]; l2 = [[1, 3], [13, 15, 17]]
l3 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]; l4 = [[[3, 4], [5, 6]]]
l5 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]; l6 = [[[3, 4], [5, 6]]]
print('92. Nested list:', nested(l1,l2), nested(l3,l4), nested(l5,l6))

# 93. Write a Python program to count the number of sublists contain a particular element.
def count_elt(l, elt):
    return elt, len([x for x in l if elt in x])
l1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
l2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
print('93. Count elts:', count_elt(l1, 1), count_elt(l1, 7), count_elt(l2, 'A'), count_elt(l2, 'E'))

# 94. Write a Python program to count number of unique sublists within a given list.
def count_sub(l):
    d = dict()
    n = 0
    for x in l:
        d.setdefault(tuple(x), list()).append(1)
    for key, val in d.items():
        d[key] = sum(val)
    return d
l1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
l2 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
print('94. Count elts:', count_sub(l1), count_sub(l2))

# 96. Write a Python program to sort a given list of lists by length and value.
l1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
a = sorted(l1)
print('96. Sorted sub:', sorted(a, key=len))

# 97. Write a Python program to remove sublists from a given list of lists, which are outside a given range.
l1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
print('97. Selct by length:', list(filter(lambda x: len(x)==4, l1)))

# 98. Write a Python program to scramble the letters of string in a given list.
import random
l1 = ['Python', 'list', 'exercises', 'practice', 'solution']
for num, x  in enumerate(l1):
    mix = list(x)
    random.shuffle(mix)
    l1[num] =''.join(mix)
print('98. Shuffle letters:', l1)

# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
l1 = ['Python', 3, 2, 4, 5, 'version']
def min_max(l):
    temp = []
    for x in l:
        if isinstance(x, int):
            temp.append(x)
    return f'max: {max(temp)}, min: {min(temp)}'
print('99.', min_max(l1))

# 100. Write a Python program to extract common index elements from more than one given list.
l1, l2, l3 = [1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]
def common(l1,l2,l3):
    return list(val for key, val in enumerate(l1) if l2[key]==l3[key]==val)
print('100. Common values:', common(l1,l2,l3))

# 101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
l1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]; l2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
def ascend_sum(l):
    return sorted(l, key=sum)
print('101.', ascend_sum(l1), ascend_sum(l2))

# 102. Write a Python program to extract specified size of strings from a give list of string values.
l1 = ['Python', 'list', 'exercises', 'practice', 'solution']
def extract(l, num):
    return [x for x in l if len(x)==num]
print('102. Extract by length:', extract(l1,8))

# 103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
from itertools import groupby
l1, l2 = [1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
def follow(l, num):
    return  [x for x,y in groupby(l) if len(list(y))==num]
print('103. Groupby:', follow(l1,2), follow(l2,4))

# 104. Write a Python program to find the difference between consecutive numbers in a given list. 
l1, l2 = [1, 1, 3, 4, 4, 5, 6, 7], [4, 5, 8, 9, 6, 10]
def diff(l):
    return [b-a for a, b in zip(l[:-1], l[1:])]
print('104. Diff:', diff(l1), diff(l2))

# 105. Write a Python program to compute average of two given lists.
l1, l2 = [1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 5, 7, 8]
def average(l1,l2):
    return sum((sum(l1)/len(l1), sum(l2)/len(l2)))/2
print('105. Average:', average(l1,l2))

# 106. Write a Python program to count integer in a given mixed list.
l1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print('106. Integer count:', len([x for x in l1 if isinstance(x, int)]))

# 107. Write a Python program to remove a specified column from a given nested list.
l1, l2 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]], [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
def remove_col(l, col):
    for x in l:
        del x[col-1]
    return l
print('107. Remove by index:', remove_col(l1, 1), remove_col(l2, 3))

# 108. Write a Python program to extract a specified column from a given nested list.
l1, l2 =[[1, 2, 3], [2, 4, 5], [1, 1, 1]], [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
def extract(l, num):
    return list(map(lambda x: x[num-1] , l))
print('108. Extract by index:', extract(l1, 1), extract(l2, 3))

# 109. Write a Python program to rotate a given list by specified number of items to the right or left direction. 
from collections import deque
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def rotation(l, num):
    d_list = deque(l); d_list.rotate(num)
    return [x for x in d_list]
print('109. Rotate by index:', rotation(l1, -4), rotation(l1, 4))

# 110. Write a Python program to find the item with maximum occurrences in a given list.
from collections import Counter
l1 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
c = Counter(l1)
print('110. Max elt:', list(x for x, y in c.most_common(1)))

# 111. Write a Python program to access multiple elements of specified index from a given list.
l1, index_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]
def multi(l, ind):
    return [l1[x] for x in ind]
print('111. Select by index', multi(l1, index_list))

# 112. Write a Python program to check whether a specified list is sorted or not.
l1, l2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17], [1, 2, 4, 6, 8, 10, 12, 11, 16, 17]
def is_sorted(l):
    temp = sorted(l)
    return temp == l
print('112. Sorted or not:', is_sorted(l1), is_sorted(l2))

# 113. Write a Python program to remove duplicate dictionary from a given list.
l1 = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
l2 = []
for n in l1:
    if n not in l2:
        l2.append(n)
print('113. Remove dupl:', l2 )
print('    ', [dict(x) for x in {tuple(d.items()) for d in l1}])

# 114. Write a Python program to extract the nth element from a given list of tuples.
l1 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
def select(l, num):
    return [x[num] for x in l]
print('114. Select by index:', select(l1,0), select(l1,2))

# 115. Write a Python program to check if the elements of a given list are unique or not.
from collections import Counter
l1, l2 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17], [2, 4, 6, 8, 10, 12, 14]
def uniq(l):
    c = Counter(l)
    return sum(c.values())/len(c) == 1
print('115. Duplicates:', uniq(l1), uniq(l2))

# 116. Write a Python program to sort a list of lists by a given index of the inner list.
l1 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
def sort_by(l, num):
    return list(sorted(l, key=lambda x: x[num]))
print('116. Sort by index:', sort_by(l1, 0), sort_by(l1, 2))

# 117. Write a Python program to remove all elements from a given list present in another list.
l1, l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]
print('117. Remove from list:', [x for x in l1 if x not in l2])

# 118. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
l1 = [1, 2, 6, 7, 8, 10]
print('118. difference 1by1:', [x-(l1[l1.index(x)-1]) for x in l1 if x > 1])

# 119. Write a Python program to check if a substring presents in a given list of string values.
l1 = ['red', 'black', 'white', 'green', 'orange']
def sub_find(l, sub):
    return sub in str(list(filter(lambda x: sub in x, l)))
print('119. Search for substring:', sub_find(l1, 'ack'), sub_find(l1, 'abc'))

# 120. Write a Python program to create a list taking alternate elements from a given list.
l1, l2 = ['red', 'black', 'white', 'green', 'orange'], [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
print('120. Get 1 on 2:', l1[::2], l2[::2])

