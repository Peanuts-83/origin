# 1. Write a Python class to convert an integer to a roman numeral.
class IntToRoman:
    """
    Convert an int to a roman numeral.
    """
    def converter(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += roman[i]
                num -= val[i]
            i += 1
        return roman_num

print('1.', IntToRoman().converter(18))

# 2. Write a Python class to convert a roman numeral to an integer.
class RomanToInt:
    def converter(self,roman_num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_list = []
        num = 0
        while roman_num != '':
            for n in roman:
                if n in roman_num[:len(n)]:
                    roman_list.append(n)
                    roman_num = roman_num.replace(n,'',1)
                    num += val[roman.index(n)]
        return num
print('2.', RomanToInt().converter('MDCCLXXXIX'))

# 3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", 
# "({[)]" and "{{{" are invalid.
class parentheses:
    def validity(self, string):
        counter = 0
        for n in string:
            counter += 1 if n in '([{' else -1
            if n == ')':
                if string[string.index(n)-1] != '(':
                    return False
            elif n == ']':
                if string[string.index(n)-1] != '[':
                    return False
            elif n == '}':
                if string[string.index(n)-1] != '{':
                    return False
        if counter == 0:
            return True
        else:
            return False
print('3.', parentheses().validity('([][()]{})'))

# 4. Write a Python class to get all possible unique subsets from a set of distinct integers.
class py_solution:
    def sub_sets(self, sub):
        return self.subsetsRecur([], sorted(sub))

    def subsetsRecur(self, current, sub):
        if sub:
            return self.subsetsRecur(current, sub[1:]) + self.subsetsRecur(current + [sub[0]], sub[1:])
        return [current]
print('4.', py_solution().sub_sets([4, 5, 6]))

class Subsets:
    def sub(self,l):
        sb = [[]]
        for i in l:
            for j in range(len(sb)):
                sb.append(sb[j]+[i])
        return sb
print('  ',Subsets().sub([4, 5, 6]))

# 5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array 
# whose sum equals a specific target number.
class py_solution:
    def sum_pair(self, numbers, target):
        for x in numbers:
            for y in range(len(numbers)):
                if x+numbers[y]==target: pair = (x, numbers[y]) 
        return pair

print('5.', py_solution().sum_pair([10,20,10,40,50,60,70], 110))

# 6. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
from itertools import combinations
class py_solution:
    def equals_0(self, numbers):
        return [comb for comb in combinations(numbers, 3) if sum(comb)==0]
print('6.', py_solution().equals_0([-25, -10, -7, -3, 2, 4, 8, 10]))

# 7. Write a Python class to implement pow(x, n).
class py_solution:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        return self.x**self.n
print('7.', py_solution(5,3).pow())

# 8. Write a Python class to reverse a string word by word.
class py_solution:
    def __init__(self, string):
        self.string = string
    def reverse(self):
        return ' '.join((self.string.split()) [::-1])
    def reverse2(self):
        return ' '.join(reversed(self.string.split()))
print('8.', py_solution('Python .py').reverse(), py_solution('Python .py').reverse2())

# 9. Write a Python class which has two methods get_String and print_String. get_String accept a string 
# from the user and print_String print the string in upper case.
class my_String:
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.string = input()
    def print_String(self):
        print(self.string.upper())
print('9. ', end='')
standard_input = 'w3ressouces'
plop = my_String()
plop.get_String()
plop.print_String()

# 10. Write a Python class named Rectangle constructed by a length and width and a method 
# which will compute the area of a rectangle.
print('10.')
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        surf = []
        for n in range(self.height):
            print('*'*self.width)
Rectangle(8,5).area()

# 11. Write a Python class named Circle constructed by a radius 
# and two methods which will compute the area and the perimeter of a circle.
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi*self.radius**2
    def perimeter(self):
        return 2*pi*self.radius
print(f'11. Circle with radius(8) has area:{round(Circle(8).area(),2)} and perimeter:{round(Circle(8).perimeter(),2)}')

# 12. Write a Python program to get the class name of an instance in Python.
class GetClass:
    def __init__(self, instance):
        self.instance = instance
    def __repr__(self):
        return f'The class is {type(self.instance).__name__}'
c1 = Circle(5)
print(GetClass(c1))
