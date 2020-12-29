# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).
nums_5_7 = [n for n in range(1500, 2701) if n%7==0 and n%5==0]
print('1.', nums_5_7)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
def conversion(str):
    temp_unit = str.split('°')
    temp = int(temp_unit[0])
    unit = temp_unit[1]
    if unit == 'C':
        res = round((temp*9/5) + 32, 2)
        return f'{str} is {res}°F'
    elif unit == 'F':
        res = round((temp*5/9) - 32, 2)
        return f'{str} is {res}°C'
print('2.', conversion('15°C'), conversion('-20°F'))

# 3. Write a Python program to guess a number between 1 to 9.
# import random
# guess, a = random.randint(0,9), 10
# while a != guess:
#     a = int(input('Choisi un nbre entre 0 et 9:'))
#     print(a, guess)
# print('Trouvé!')

# 4. Write a Python program to construct the following pattern, using a nested for loop.
print('4.')
for i in range(1,10):
    if i < 5:
        a = '*'*i
        print(a)
    else:
        a = '*'*(5-(i-5))
        print(a)

# 5. Write a Python program that accepts a word from the user and reverse it.
rev_str = lambda x: ''.join(list(reversed(x)))
print('5.', rev_str('azerty'))

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = len(list(filter(lambda x: x%2==0, numbers)))
odd = len(list(filter(lambda x: x%2!=0, numbers)))
print(f"6. There're {even} even nbers and {odd} odd nbers in {numbers}.")

# 7. Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
res = list(map(lambda x: f'{x} is {type(x)} type.', datalist))
print('7.')
for n in res:
    print('  ',n)

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
print('8.', list(filter(lambda x: x!=3 and x!=6, range(7))))

# 9. Write a Python program to get the Fibonacci series between 0 to 50.
import itertools as it
def fibo():
    x, y = 0, 1
    yield x
    while True:
        yield y
        x, y = y , y+x
res = list(filter(lambda x: x<50, (it.islice(fibo(), 20))))
print('9.', res)

x, y = 0, 1
while y<50:
    print('  ',y)
    x, y = y, x+y

# 10. Write a Python program which iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
fizzbuzz = []
for i in range(1,51):
    if i%3==0 and i%5==0:
        fizzbuzz.append('Fizzbuzz')
    elif i%3==0:
        fizzbuzz.append('Fizz')
    elif i%5==0:
        fizzbuzz.append('Buzz')
    else:
        fizzbuzz.append(i)
print('10.', fizzbuzz)

# 11. Write a Python program which takes two digits m (row) and n (column) as input 
# and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
import numpy as np
def array(a,b):
    row, col = [n for n in range(a)], [n for n in range(b)]
    row_array = ([])
    for n in col:
        row_array = np.hstack((row_array, list(map(lambda x: x*n, row))))
    array = row_array.reshape(b,a)
    return array
print('11.')
print(array(10,6))

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) 
# as input and prints the lines as output (all characters in lower case).
a = input('write something: ')
while a != '':
    print(a.lower(), end=' / ')
    print(a.upper())
    a = input('write something: ')

# 13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and print the numbers that are divisible by 5 in a comma separated sequence.
bin_str = '0001','0010','0011','0100','0101','0110','0111'
res = list(filter(lambda x: int(x,2)%5 == 0, bin_str))
print('13.', res)

# 14. Write a Python program that accepts a string and calculate the number of digits and letters.
sample = 'Python 3.2'
digit = len(list(filter(lambda x: x.isdigit(), sample)))
letter = len(list(filter(lambda x: x.isalpha(), sample)))
print('14.', f"Count {digit} digits and {letter} letters in '{sample}'.")

# 15. Write a Python program to check the validity of password input by users.
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
import re
password = input('Enter a valid password: ')
x = True
while x:
    if 6 > len(password) > 16:
        break
    if not re.search('[a-z]', password):
        break
    if not re.search('[A-Z]', password):
        break
    if not re.search('[0-9]', password):
        break
    if not re.search('[$#@]', password):
        break
    else:
        print('password ok.')
        x = False
        break
if x:
    print('Invalid password.')
    
# 16. Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence.
import re
num_list = [n for n in range(100, 401)]
res = list(filter(lambda x: not re.search('1|3|5|7|9', str(x)), num_list))
print('16.', res)

# 31. Write a Python program to calculate a dog's age in dog's years.
dog_age = 15
human_age = sum([10.5 if n<3 else 4 for n in range(1, dog_age)])
print('31.', human_age)

# 32. Write a Python program to check whether an alphabet is a vowel or consonant.
def letter_det(lett):
    if lett in 'a,e,i,o,u,y':
        return 'vowell'
    else:
        return 'consonant'
print(f"32. 'e' is a {letter_det('e')}, 'k' is a {letter_det('k')}")

# 33. Write a Python program to convert month name to a number of days. 
month_dict = {'28/29' : ('February'), 
    '31' : ('January', 'March', 'May', 'July', 'August', 'October', 'December'),
    '30' : ('April', 'June', 'September', 'November', 'December')}
def num_month(month):
    for n in month_dict:
        if month in month_dict[n]:
            return n
print('33. May is', num_month('May'), 'days.')

# 34. Write a Python program to sum of two given integers. 
# However, if the sum is between 15 to 20 it will return 20.
def summing(x,y):
    result = x+y
    if 15 <= result <= 20:
        return '20'
    else:
        return result
print('34.', summing(5,8), summing(10,5), summing(18,7))

# 35. Write a Python program to check a string represent an integer or not.
def int_det(string):
    if string.isdigit():
        return True
    else:
        return False
print('35.', int_det('Python'))

# 36. Write a Python program to check a triangle is equilateral, 
# isosceles or scalene.
def triangle(a,b,c):
    if a==b==c:
        return 'Equilateral'
    elif a==b or a==c or b==c:
        return 'Isoscele'
    else:
        return 'Scalene'
print('36.', triangle(5,8,7))

# 41. Write a Python program to get next day of a given date.
import datetime as dt
def add_date(y,m,d):
    return dt.datetime(y, m, d) + dt.timedelta(days=1)
print('41.', add_date(2021,2,28))

