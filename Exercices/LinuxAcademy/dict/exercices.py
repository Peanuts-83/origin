# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
from operator import itemgetter
d1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('1. Sort by value:', sorted(d1.items(), key=itemgetter(1)), sorted(d1.items(), key=itemgetter(1), reverse=True))

# 2. Write a Python script to add a key to a dictionary.
d1 = {0: 10, 1: 20}
d1[2]=30
print('2. Add to dict:', d1)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
{dic4.update(d) for d in (dic1,dic2,dic3)}
print('3. Concatenate:', dic4)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
d1 = {0: 10, 1: 20}
print('4. keys:',d1.keys())

# 5. Write a Python program to iterate over dictionaries using for loops.
d1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('5. Items:', end='')
for a,b in d1.items():
    print((a,b), end=' ')

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
print('\n6. Generate dict:', dict((x,x**2) for x in range(1,6)))

# 8. Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d1.update(d2)
print('8. Merge:', d1)

# 9. Write a Python program to iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3}
print('9. Iterate: ', end='') 
for a,b in d.items():
    print(f'{a} color is num {b}. ', end='')

# 10. Write a Python program to sum all the items in a dictionary.
print('\n10. Sum:', sum(d1.values()))

# 11. Write a Python program to multiply all the items in a dictionary.
val = 1
for key in d1:
    val *= d1[key]
print('11. Multiply:', val)

# 12. Write a Python program to remove a key from a dictionary.
del d1['y']
print('12. Remove:', d1)

# 13. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
print('13. Map lists:', dict(zip(keys, values)))

# 14. Write a Python program to sort a dictionary by key.
d = {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
print('14. Sorted:', dict(sorted(d.items())))
# for key in sorted(d):
#     print(f'{key}:{d[key]}', d)

# 15. Write a Python program to get the maximum and minimum value in a dictionary.
print('15. Max:', max(d1[key] for key in d1), 'Min:',min(d1[key] for key in d1))

# 16. Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'

test = dictObj()
print('16.', test.__dict__)

# 17. Write a Python program to remove duplicates from Dictionary.
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
temp = {}
for key, value in student_data.items():
    if value not in temp.values(): temp[key] = value
print('17. Remove duplicates:', temp)

# 18. Write a Python program to check a dictionary is empty or not
d2 = {}
def empty(d):
    if not bool(d): return True
    return False
print('18. Empty:', empty(d), empty(d2))

# 19. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for a, b in d1.items():
    if a in d2.keys():
        d1[a] += d2[a]
for a, b in d2.items():
    if a not in d1.keys():
        d1[a] = d2[a]
print('19. Sum of keys:', d1)

from collections import Counter
c = Counter(d1) + Counter(d2)
print('   ', c)

# 20. Write a Python program to print all unique values in a dictionary.
from collections import Counter
l1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
c = set(val for dic in l1 for val in dic.values())
print('20. Uniq values:',c)

# 21. Write a Python program to create and display all combinations of letters, 
# selecting each letter from a different key in a dictionary.
d1 = {'1':['a','b'], '2':['c','d']}
print('21. Combinations:', [a+b for a in d1['1'] for b in d1['2']])

# 22. Write a Python program to find the highest 3 values in a dictionary.
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted_dict = list(sorted(my_dict, key=my_dict.get, reverse=True))
print('22. 3 highest values:', sorted_dict[:3])

# 23. Write a Python program to combine values in python list of dictionaries.
d1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d2 = {}
for x in d1:
    if x['item'] not in d2: d2[x['item']]=x['amount']
    else: d2[x['item']]+=x['amount']
print('23. Combine values:', d2)

# 24. Write a Python program to create a dictionary from a string.
from collections import Counter
mot = 'w3resource'
c_mot = Counter(mot)
d1 = dict((key, val) for key, val in c_mot.items())
print('24. Dict from string:', d1)

# 25. Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print('25. Table by zip*:')
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

# 26. Write a Python program to count the values associated with key in a dictionary. 
l1 = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, 
{'id': 3, 'success': True, 'name': 'Alex'}]
a = sum(list(1 for x in l1 if x['success']==True))
print('26. Nber of True:', a)

# 27. Write a Python program to convert a list into a nested dictionary of keys.
l1 = [1, 2, 3, 4]
d1 = {}
for x in l1[::-1]:
    d1 = {x:d1}
print('27. Nested dict:', d1)

# 28. Write a Python program to sort a list alphabetically in a dictionary.
d1 = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
d2 =  dict((key,sorted(val)) for key,val in d1.items())
print('28. Sorted lists in dict:', d2)

# 29. Write a Python program to remove spaces from dictionary keys.
d1 = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d2 = dict((key.replace(' ',''), val) for key,val in d1.items() )
print('29. Remove spaces in keys:', d2)

# 30. Write a Python program to get the top three items in a shop.
d1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
l1 = sorted(list((key, val) for key,val in d1.items()), key=itemgetter(1), reverse=True )
print('30. Top 3:', l1[:3])

# 31. Write a Python program to get the key, value and item in a dictionary.
d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('31. Dict by array:')
print('key  value  count')
for count, (key, val) in enumerate(d1.items(),1):
    print(key,'   ',val,'   ',count)

# 34. Write a Python program to count number of items in a dictionary value that is a list.
d1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
print('34. Count values:', sum(map(len, d1.values())))

# 35. Write a Python program to sort Counter by value.
d1 = {'Math':81, 'Physics':83, 'Chemistry':87}
print('35. Sort by value:', sorted(d1.items(), key=itemgetter(1)))

# 36. Write a Python program to create a dictionary from two lists without losing duplicate values.
l1, l2 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
print('36. Dict from lists:', dict(zip(l1,l2)) )

from collections import defaultdict
temp = defaultdict(set)
for a,b in zip(l1,l2):
    temp[a].add(b)
print('    Values as set:  ',temp)

# 37. Write a Python program to replace dictionary values with their average.
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
def average(l):
    for x in l:
        a = x.pop('V')
        b = x.pop('VI')
        x['V+VI'] = (a+b)/2
    return l
print('37. Average:', average(student_details))

# 38. Write a Python program to match key values in two dictionaries.
d1, d2 = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
for (key,val) in set(d1.items()) & set(d2.items()):
    print('38. Common match:', (key,val))

# 39. Write a Python program to store a given dictionary in a json file.
import json
d1 = {'students': 
[{'firstName': 'Nikki', 'lastName': 'Roysden'}, 
{'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 
'teachers': 
[{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

with open('data.txt', 'w') as outfile:
    json.dump(d1, outfile, indent=4)
# Import JSON.
import json

with open('data.txt') as json_file:
    data = json.load(json_file)

print('39. JSON:',d1)

# 40. Write a Python program to create a dictionary of keys x, y, and z 
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
# Access the fifth value of each key from the dictionary.
d1 = {}; inc = 0
for letter in ['x','y','z']:
    inc += 10
    num = [n for n in range(1+inc,10+inc)]
    d1[letter] = num
print('40. Dict and values:', d1)
for key, val in d1.items():
    print(val[4])
    print(f'{key} has value {val}')

# 41. Write a Python program to drop empty Items from a given Dictionary. 
d1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
d2 = {key:val for key, val in d1.items() if val is not None}
print('41. Drop empty items:', d2)

# 42. Write a Python program to filter a dictionary based on values.
d1 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d2 = {key:val for key, val in d1.items() if val > 170}
print('42. Filter by value:', d2)

