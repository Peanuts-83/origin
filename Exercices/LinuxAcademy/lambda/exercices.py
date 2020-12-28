# 1. Write a Python program to create a lambda function that adds 15 
# to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y 
# and print the result.
func_add = lambda x: x+15
func_mul = lambda x, y: x*y

assert func_add(5) == 20, f"Expected 'func_add(5)' to equal '20' but received '{func_add(5)}'"
assert func_mul(5, 2) == 10, f"Expected 'func_mul(5, 2)' to equal '10' but received '{func_mul(5, 2)}'"

# 2. Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
import random
func_mul2 = lambda x: x*random.randrange(10)
# random.getstate()
# assert func_mul2(12) == 12*random.setstate(), f"Expected 'func_mul2(12)' to equal '{12*random.setstate()}' but received '{func_mul2(12)}'"

# 3. Write a Python program to sort a list of tuples using Lambda.
tuple = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sort_tuple = sorted(tuple, key=lambda d: d[1])
print('3.',sort_tuple)

#4. Write a Python program to sort a list of dictionaries using Lambda.
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
brand = sorted(models, key=lambda d: d['make']); model = sorted(models, key=lambda d: int(d['model'])); color = sorted(models, key=lambda d: d['color'])
print(f"4. brand: {brand}\nmoddel: {model}\ncolor: {color}")

#5. Write a Python program to filter a list of integers using Lambda.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda n: n%2 == 0, nums))
print('5.',even)

#6. Write a Python program to square and cube every number in a given list of integers using Lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squ_cub = list(map(lambda n: (n**2, n**3), nums))
print('6.',squ_cub)

#7. Write a Python program to find if a given string starts with a given character using Lambda
start_with = lambda x: True if x.startswith('P') else False
print('7.', 'Python:', start_with('Python'), '\n   Hermione:', start_with('Hermione') )

#8. Write a Python program to extract year, month, date and time using Lambda.
import datetime
now = datetime.datetime.now()
print('8.', now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print('  ',year(now), '\n  ', month(now), '\n  ', day(now), '\n  ', time(now))

#9. Write a Python program to check whether a given string is number or not using Lambda.
check_num = lambda x: x.replace('.','',1).isdigit()
print('9.', check_num('0.3'), check_num('A38'), check_num('1897.3'))

#10. Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
fibo = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])
print('10.', fibo(5), fibo(10))

#11. Write a Python program to find intersection of two given arrays using Lambda.
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
inters = list(filter(lambda x: x in array_nums2, array_nums1))
print('11.', inters)

#12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
array_nums.sort(key=lambda x: 0 if x == 0 else -1/x)
print('12.', array_nums)

#13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x%2 == 0, array_nums))
odd_nums = list(filter(lambda x: x%2 != 0, array_nums))
print(f"13. There're {len(even_nums)} even numbers and {len(odd_nums)} odd numbers in {array_nums} list.")

#14. Write a Python program to find the values of length six in a given list using Lambda.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
val_6 = filter(lambda x: len(x) == 6, weekdays)
for d in val_6:
    print('14.', d)

#15. Write a Python program to add two given lists using map and lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums = list(map(lambda x,y: x + y, nums1, nums2))
numssum = nums1 + nums2
print('15.', nums, numssum)

#16. Write a Python program to find the second lowest grade of any student(s) 
# from the given names and grades of each student using lists and lambda. 
# Input number of students, names and grades of each student.
# n = int(input('Nber of students: '))
# print(n)
# liste = []
# for _ in range(n):
#     name = input('Name: ')
#     grade = input('Grade: ')
#     liste.append((name, grade))
# print(liste)
# grade_list = sorted(list({n[1] for n in liste}))
# scnd_grade = list(filter(lambda x: x[1] == grade_list[1], liste))
# print(f"The second lower grade is grade {grade_list[1]}.\nThe name is: {scnd_grade[0][0]}")

#17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
selection = list(filter(lambda x: x%19 == 0 or x%13 == 0, nums))
print('17.', selection)

#18. Write a Python program to find palindromes in a given list of strings using Lambda.
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
res = list(filter(lambda x: (x == ''.join(reversed(x))), texts))
print('18.', res)

#19. Write a Python program to find all anagrams of a string in a given list of strings using lambda.
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = 'abcd'
idem = list(filter(lambda x: Counter(x)==Counter(str) ,texts))
print('19.', idem)

#20. Write a Python program to find the numbers of a given string and store them in a list, 
# display the numbers which are bigger than the length of the list in sorted form. 
# Use lambda function to solve the problem
str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
str1_list = list(filter(lambda x: x.isdigit(), str1.split(' ')))
nums = list(filter(lambda x: int(x) > len(str1_list), str1_list))
print('20.', str1_list, nums)

#21. Write a Python program that multiply each number of given list with a given number using lambda function. 
# Print the result.
nums = [2, 4, 6, 9 , 11]
n = 2
print('21.', list(map(lambda x: x*n, nums)))

#22. Write a Python program that sum the length of the names of a given list of names after removing 
# the names that starts with an lowercase letter. Use lambda function
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
upper_names = list(filter(lambda x: x[0].isupper(), sample_names))
print('22.', sum(map(lambda x: len(x), upper_names)))

#23. Write a Python program to calculate the sum of the positive and negative numbers 
# of a given list of numbers using lambda function.
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
pos = filter(lambda x: x>0, nums); neg = filter(lambda x: x<0, nums)
print('23. Sum of positives:', sum(pos), ' Sum of negatives:', sum(neg))

#24. Write a Python program to find numbers within a given range 
# where every number is divisible by every digit it contains.
def div_num(start_num, end_num):
    return [n for n in range(start_num, end_num+1) if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
    # return [n for n in range(1,x+1) if not any(map(lambda y: int(y)==0 or n%int(y)!=0, str(n)))]
print('24.', div_num(1,15))

#25. Write a Python program to create the next bigger number by rearranging the digits of a given number.
def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
print('25.', rearrange_bigger(15458))