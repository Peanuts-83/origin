# 1. Write a Python program to triple all numbers of a given list of integers. Use Python map.
nums = (1, 2, 3, 4, 5, 6, 7)
triple = list(map(lambda x: x*3, nums))
print('1.', triple)

# 2. Write a Python program to add three given lists using Python map and lambda.
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
sum_nums = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))
print('2.', sum_nums)

# 3. Write a Python program to listify the list of given strings individually using Python map.
color = ['Red', 'Blue', 'Black', 'White', 'Pink']
listify = list(map(lambda x: list(x), color))
print('3.', listify)

# 4. Write a Python program to create a list containing 
# the power of said number in bases raised to the corresponding 
# number in the index using Python map.
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
power = list(map(lambda x, y: x**y, bases_num, index))
print('4.', power)

# 5. Write a Python program to square the elements of a list using map() function.
def squarer(liste):
    return list(map(lambda x: x**2, liste))
print('5.', squarer([4, 5, 2, 9]))

# 6. Write a Python program to convert all the characters in uppercase and lowercase 
# and eliminate duplicate letters from a given sequence. Use map() function
def conv_string(string):
    str_set = set(string.lower())
    return sorted(set(map(lambda x: (x.upper(), x), str_set)), key=lambda x: x[0].lower())
print('6.', conv_string('AHJSUhzauehqsAAQSJOEEzeqskfmnhiqa'))

# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function.
def comp_list(list1, list2):
    return list(map(lambda x, y: (x+y, x-y), list1, list2))
print('7.', comp_list([6, 5, 3, 9], [0, 1, 7, 7]))

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
def list_tup(list1, tuple1):
    list_str = list(map(lambda x: str(x), list1))
    tup_str = list(map(lambda x: str(x), tuple1))
    return list_str, tup_str
print('8.', list_tup([1, 2, 3, 4], (0, 1, 2, 3)))

# 9. Write a Python program to create a new list taking specific elements from a tuple 
# and convert a string value to integer.
student_data  = [('Alberto Franco','15/05/2002','35kg'), 
('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), 
('Eesha Hinton','25/09/1998', '35kg')]
name = list(map(lambda x: x[0], student_data))
date = list(map(lambda x: x[1], student_data))
weight = list(map(lambda x: int(x[2][:2]), student_data))
print(f'9. students name: {name} \n   students birthday: {date} \n   students weight: {weight}')

# 10. Write a Python program to compute the square of first N Fibonacci numbers, 
# using map function and generate a list of the numbers.
import itertools as it
n=10
def fibo():
    x, y = 0, 1
    yield x
    while True:
        yield y
        x, y = y, x+y
fibo_list = list(it.islice(fibo(), n))
square = lambda x: x**2
print('10.', list(map(square, fibo_list)))

