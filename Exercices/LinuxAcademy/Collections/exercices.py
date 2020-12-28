# 1. Write a Python program that iterate over elements repeating each as many times as its count.
from collections import Counter
liste = ['p', 'p', 'p', 'p', 'q', 'q']
c = Counter(a=5, b=3, c=1)
print('1.', Counter(liste), list(c.elements()))

# 2. Write a Python program to find the most common elements and their counts of a specified text.
from collections import Counter
string ='lkseropewdssafsdfafkpwe'
cnt = Counter(string)
print('2.', cnt.most_common(3))

# 3. Write a Python program to create a new deque with three items and iterate over the deque's elements.
from collections import deque
deq = deque('aei')
deq.appendleft('x')
deq.popleft()
deq.append('x')
deq.append('x')
print('3.', deq, end=' ')
deq.reverse()
print('reversed:', deq, '- x count:', deq.count('x'))
for n in deq:
    print('  ',n)

# 4. Write a Python program to find the occurrences of 10 most common words in a given text.
from collections import Counter
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
text = text.split()
cnt = Counter(text)
print('4.', cnt.most_common(10))

# 5. Write a Python program that accept some words and count the number of distinct words. 
# Print the number of distinct words and number of occurrences 
# for each distinct word according to their appearance.
from collections import Counter
standard_input = 'Hello word I got to go in word to go on word'
text = input('Some text: ')
cnt = Counter(text.split())
print('5.', cnt.most_common())

# 8. Write a Python program to create a deque from an existing iterable object.
from collections import deque
tuple = (2, 4, 6)
deq = deque(tuple)
print('8.', deq)

# 9. Write a Python program to add more number of elements to a deque object from an iterable object.
from collections import deque
deq = deque([2, 4, 6, 8, 10])
deq2 = ([])
for n in range(12,21,2):
    deq2.append(n)
deq.extend(deq2)
print('9.', deq2, deq)

# 10. Write a Python program to remove all the elements of a given deque object.
from collections import deque
deq = deque([2, 4, 6, 8, 10])
deq.clear()
print('10.', deq)

# 11. Write a Python program to copy of a deque object and verify the shallow copying process.
from collections import deque
deq = deque([2, 4, 6, 8, 10])
deq2 = deq.copy()
print('11.', deq, deq2)

# 12. Write a Python program to count the number of times a specific element presents in a deque object.
from collections import deque
text = 'Hello word I got to go in word to go on word'
deq = deque(text)
print(f"12. '{text}' counts {deq.count('o')} 'o'.")

# 13. Write a Python program to rotate a Deque Object specified number (positive) of times.
from collections import deque
deq = deque([2, 4, 6, 8, 10])
deq1 = deq.copy()
deq1.rotate(1)
deq2 = deq.copy()
deq2.rotate(-3)
print('13.', deq, 'rotate 1:', deq1, 'rotate -3:', deq2)

# 15. Write a Python program to find the most common element of a given list.
from collections import Counter
text = 'Hello word I got to go in word to go on word'
cnt = Counter(text.split())
print('15.', cnt.most_common(1)[0][0])

# 16. Write a Python program to perform Counter arithmetic and set operations for aggregating results.
from collections import Counter
c1 = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
c2 = Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1})
cnt = c1 + c2
cnt2 = c1 - c2
cnt3 = c1 & c2
cnt4 = c1 | c2
print(f"16. C1 {c1} / C2 {c2}\n   Addition: {cnt}\n   \
Substract: {cnt2}\n   Intersect: {cnt3}\n   Union: {cnt4}")

# 17. defaultdict # creating keys on the fly, return 0 for non existing key.
from collections import defaultdict
def_dict = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for i in names_list:
    def_dict[i] += 1
print('17.', def_dict, def_dict['Jules'], def_dict['Georges'])

# 18. OrderedDict # keys maintained in the order in which they are inserted.
from collections import OrderedDict, Counter
letter_list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(letter_list)

