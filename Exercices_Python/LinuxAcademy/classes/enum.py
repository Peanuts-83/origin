import enum

class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for c in Countries:
    print(c.name, c.value)
print('name: ', Countries.Albania.name, ' value: ', Countries.Albania.value)

# 3. Write a Python program to display all the member name of an enum class ordered by their values.
class Countries(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for c in sorted(Countries):
    print(c.name)

# 4. Write a Python program to get all values from an enum class.
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for c in Countries:
    print(c.value)

# 5. Write a Python program to count the most common words in a dictionary.
words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
from collections import Counter
words_count = Counter(words)
words_count.most_common(4)

# 6. Write a Python program to find the class wise roll number from a tuple-of-tuples. 
from collections import defaultdict
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
def_dict = defaultdict(list)
for name, val in classes:
    def_dict[name].append(val)
print(def_dict)

# 7. Write a Python program to count the number of students of individual class.
dict_sum = Counter(name for name, num in classes)
print(dict_sum) 

# 9.
dict_c = {
    'Afghanistan' : 93,
    'Albania' : 355,
    'Algeria' : 213,
    'Andorra' : 376,
    'Angola' : 244,
    'Antarctica' : 672
}
from collections import OrderedDict
c = sorted(dict_c)
O_dict = OrderedDict(c)
for a, b in O_dict:
    print(a, b)
