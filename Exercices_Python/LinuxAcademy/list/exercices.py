# 1. Write a Python program to sum all the items in a list.
def sum_list(l):
    sum = 0
    for n in l: sum += n 
    return sum
print('1.',sum_list([1,2,-8]))

# 2. Write a Python program to multiplies all the items in a list.
def mult_list(l):
    mult = 1
    for n in l: mult *= n
    return mult
print('2.',mult_list([3, 5, -8]))

# 3.4. Write a Python program to get the largest/lowest number from a list.
def largest(l):
    return max(l), min(l)
print('3.4.',largest([8, -5, 22, -3]))

# 5. Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings.
def count(l):
    return len(list(filter(lambda x: x[0]==x[-1] and len(x)>=2, l)))
print('5.',count(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples.
def sorting_tuple(l):
    return sorted(l, key=lambda x: x[1])
print('6.',sorting_tuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.
def duplicates(l):
    return list(set(l))
print('7.',duplicates([10,20,30,20,10,50,60,40,80,50,40]))

# 8. Write a Python program to check a list is empty or not.
def empty(l):
    if not l:
        return 'liste vide.'
print('8.',empty([]))

# 9. Write a Python program to clone or copy a list.
a= [1,2,3]
b= list(a)
print('9.',b)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(num, string):
    return list(filter(lambda x: len(x)>num, string.split()))
print('10.',long_words(3, "The quick brown fox jumps over the lazy dog"))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def common_data(l1, l2):
    for n in l1:
        if n in l2: 
            return True
            break 
    return False
print('11.',common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def remover(l):
    l.remove(l[5]); l.remove(l[4]); l.remove(l[0])
    return l
print('12.',remover(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
array = [[['*' for col in range(3)] for col in range(4)] for row in range(6)]
print('13.',array)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
def rem_even(l):
    return list(filter(lambda x: x%2!=0, l))
print('14.',rem_even(range(10)))

# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle
def shuff(l):
    shuffle(l)
    return l
print('15.',shuff(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 16. Write a Python program to generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30 (both included).
val = lambda x: x**2
val_list = list(map(lambda x: val(x), range(1,30)))
l = [val_list[0]]
for n in val_list[-5:]:
    l.append(n)
print('16.',l)

# 18. Write a Python program to generate all permutations of a list in Python.
from itertools import permutations
print('18.',list(permutations([1,2,3])))

# 19. Write a Python program to get the difference between the two lists.
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
print('19.',list(filter(lambda x: x not in list1, list2)) + list(filter(lambda x: x not in list2, list1)))

# 20. Write a Python program to access the index of a list.
def access(l):
    for n in enumerate(l):
        print(n)
print('20.',access([5, 15, 35, 8, 98]))

# 22. Write a Python program to find the index of an item in a specified list.
def access2(l, i):
    for counter, val in enumerate(l):
        if val == i:
            return counter
print('22.',access2([5, 15, 35, 8, 98], 35))

# 23. Write a Python program to flatten a shallow list.
def flat(l):
    liste = []
    for n in l:
        liste += n
    return liste
print('23.',flat([[2,4,3],[1,5,6], [9], [7,9,0]]))

# 24. Write a Python program to append a list to the second list.
a, b= [2,4,3], [1,5,6]
a.extend(b)
print('24.',a)

# 25. Write a Python program to select an item randomly from a list.
from random import randint
c = [5, 15, 35, 8, 98]
# print('25.',c[randint(0,len(c))])

# 26. Write a python program to check whether two lists are circularly identical.
from collections import deque
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('26.',''.join(map(str, list1)) in ''.join(map(str, list2 *2)))
print(''.join(map(str, list1)) in ''.join(map(str, list3 *2)))

l1, l2 = deque(list1), deque(list2)
for n in range(len(l1)):
    l1.rotate(1)
    if l1 == l2:
        print('yes')

# 27. Write a Python program to find the second smallest number in a list.
c = [5, 15, 35, 8, 98]
print('27.',sorted(c)[1])

# 28. Write a Python program to find the second largest number in a list.
print('28.',sorted(c, reverse=True)[1])

# 30. Write a Python program to get the frequency of the elements in a list.
from collections import Counter
my_list = Counter([10,10,10,10,20,20,20,20,40,40,50,50,30])
print('30.',my_list)

# 45. Write a Python program to convert a pair of values into a sorted unique array.
L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print('45.',sorted(set().union(*L)))

# 47. Write a Python program to insert an element before each element of a list.
d = [5, 15, 35, 8, 98]
long = len(d)
for key in range(long-1, -1, -1):
    d.insert(key, "*")
print('47.',d)

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
colors = [['Red'], ['Green'], ['Black']]
print('48.','\n'.join([str(a) for a in colors]))

# 49. Write a Python program to convert list to list of dictionaries.
a=  ["Black", "Red", "Maroon", "Yellow"]; b= ["#000000", "#FF0000", "#800000", "#FFFF00"]
print('49.',[{'color_name': x, 'color_code': y} for x, y in zip(a, b)])

# 50. Write a Python program to sort a list of nested dictionaries.
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
sorted_list = sorted(my_list, key=lambda x: x['key']['subkey'], reverse=True)
print('50.', sorted_list)

# 51. Write a Python program to split a list every Nth element.
sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print('51.', [sample[i::3] for i in range(3)])

# 52. Write a Python program to compute the difference between two lists.
data1 =  ["red", "orange", "green", "blue", "white"]; data2 = ["black", "yellow", "green", "blue"]
print('52.', list(filter(lambda x: x not in data2, data1)) + list(filter(lambda x: x not in data1, data2)))

from collections import Counter
count1 = Counter(data1); count2 = Counter(data2)
print('  ', (count1-count2) + (count2-count1))

# 53. Write a Python program to create a list with infinite elements.
import itertools
c = itertools.count()
print(next(c))
print(next(c))
print(next(c))

# 55. Write a Python program to remove key values pairs from a list of dictionaries. 
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
new_list = [{k:v for k, v in dico.items() if k!= 'key1'} for dico in original_list]
print('55.', new_list)

# 56. Write a Python program to convert a string to a list.
import ast
a = "['Bonjour', 'monde']"
print('56.', ast.literal_eval(a))

# 57. Write a Python program to check whether all items of a list is equal to a given string.
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
print('57.', all(c == 'blue' for c in color1))
print(all(d == 'green' for d in color2))

# 58. Write a Python program to replace the last element in a list with another list.
color1 = ["green", "orange", "black", "white"]
new_c = ["purple","yellow"]
color1[-1:] = new_c
# color1.pop(-1); color1.extend(new_c)
print('58.', color1)

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
x = [(4, 1), (1, 2), (6, 0)]
print('60.', min(x, key=lambda n: n[1]))

# 61. Write a Python program to create a list of empty dictionaries.
print('61.', [{} for _ in range(3)])

# 62. Write a Python program to print a list of space-separated elements.
num = [1, 2, 3, 4, 5]
print('62.', *num)

# 63. Write a Python program to insert a given string at the beginning of all items in a list.
color1 = [1,2,3,4]
string = '#'
print('63.', [string+str(a) for a in color1])

# 64. Write a Python program to iterate over two lists simultaneously.
num = [1, 2, 3]
color = ['red', 'white', 'black']
print('64.', list(map(lambda x, y: str(x)+y, num, color)), list(zip(num, color)))

# 65. Write a Python program to access dictionary keys element by index.
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print('65.', list(num)[0])

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
a = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print('66.', max(a, key=sum))

# 67. Write a Python program to find all the values in a list are greater than a specified number.
list1 = [220, 330, 500]
list2 = [12, 17, 21]
print('67.', all(x>200 for x in list1), all(x>15 for x in list2))

# 68. Write a Python program to extend a list without append.
a = [10, 20, 30]; b = [11,12,13]
a[1:1] = b
print('68.', a)

