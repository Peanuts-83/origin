import re

# 1. Write a Python program to check that a string contains only a certain set of characters
def check_txt(txt):
    #pattern = re.compile('[^a-zA-Z0-9.]')
    #test = pattern.search(txt)
    test = re.search('[^a-zA-Z0-9.]', txt)      # [] for interval // ^ for not in []
    return not bool(test)

print("[] for interval // ^ for not in []:", check_txt('azerty35.'), check_txt('#8/'))

# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
def check_ab(txt):
    test = re.search('^ab*',txt)    # ^ for begin with a // * for 0 or more b
    return bool(test)

print("* for 0 or more b:", check_ab('bacb'), check_ab('abb'))

# 3. Write a Python program that matches a string that has an a followed by one or more b's.
def check_ab(txt):
    test = re.search('ab+',txt)    # + for 1 or more b
    return bool(test)

print("+ for 1 or more b:", check_ab('bacb'), check_ab('acbb'), check_ab('cbabb'))

# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
def check_ab(txt):
    test = re.search('ab?',txt)    # ? for 0 or 1 b
    return bool(test)

print("? for 0 or 1 b:", check_ab('bacb'), check_ab('cbb'), check_ab('cbabb'))

# 5. Write a Python program that matches a string that has an a followed by three 'b'.
def check_ab(txt):
    test = re.search('ab{3}',txt)    # {3} for last letter repeated 3 times
    return bool(test)

print("{3} for last letter repeated 3 times:", check_ab('bacb'), check_ab('cbb'), check_ab('cbabbb'))

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def check_ab(txt):
    test = re.search('ab{2,3}',txt)    # {2,3} for last letter repeated 2 or 3 times
    return bool(test)

print("{2,3} for last letter repeated 2 or 3 times:", check_ab('babb'), check_ab('cbb'), check_ab('cbabbb'))

# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
def check_low(txt):
    test = re.search('[a-z]_[a-z]', txt)    
    return bool(test)

print("[a-z]_[a-z]:", check_low('sasa_hzdbhz'), check_low('sasZ_hzdbhz'))

# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def check_up(txt):
    test = re.search('[^A-Z][A-Z]_[a-z]+', txt)    
    return bool(test)

print("[^A-Z][A-Z]_[a-z]+ // 1 Upper + _ + lowers:", check_up('sasa_hzdbhz'), check_up('sasZ_hzdbhz'))

# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def check_ab(txt):
    test = re.search('^[aA][a-zA-Z0-9]*[bB]$', txt)
    return bool(test)

print('^[aA][a-zA-Z0-9]*[bB]$ begin with a ends with b:', check_ab('Afsfdb'), check_ab('AfsfdbC'))

# 10. Write a Python program that matches a word at the beginning of a string.
def check_word(txt):
    test = re.search('^(hello)', txt, flags=re.IGNORECASE)
    return bool(test)

print("flags=re.IGNORECASE ^(hello) begin with hello:", check_word('Hello world!'))

# 11. Write a Python program that matches a word at the end of string, with optional punctuation.
def check_end(txt):
    pattern = re.compile('\w+\S?$')
    test = pattern.search(txt)
    return bool(test)

print('\w for a word +\S?$ for 0 or 1 punctuation at end:', check_end('Comin the night!'), check_end('Comin the night! '))

# 12. Write a Python program that matches a word containing 'z'.
def check_z(txt):
    test = re.search('z', txt, flags=re.I)
    return bool(test)

print('search for a letter, flags=re.I for IgnoreCase:', check_z('aZpata'), check_z('bouliz'))

# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
def check_z(txt):
    test = re.search('^[^z].*[^z]$', txt, flags=re.I)
    return bool(test)

print('^[^z].*[^z]$ no z at begining or end, . for 0 or any char in the middle:', check_z('Zapata'), check_z('bouZli'))

# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
def check_uplow(txt):
    test = re.search('[^a-z0-9_]', txt, flags=re.I)
    return not bool(test)

print('[^a-z0-9_] not letter or num or _:', check_uplow('AZERTYderer@98'))

# 15. Write a Python program where a string will start with a specific number.
def check_num(txt):
    test = re.search('^5', txt)
    return bool(test)

print(check_num('5-1298'), check_num('7-1298'))

# 16. Write a Python program to remove leading zeros from an IP address.
def del_zeros(ip):
    sel = re.search('^0*', ip)
    new_ip = ip[sel.end():]
    return new_ip

print('ip[sel.end():] start() and end() to get index of found expr:', del_zeros('00000530832'))

# 16bis.
def del_zeros2(ip):
    ip = re.sub('\.0*', '.', ip)
    return ip

print("* re.sub('\.0*', '.', ip) sub for substitute:", del_zeros2('192.168.020.0094'))

# 17. Write a Python program to check for a number at the end of a string.
def check_num_end(txt):
    test = re.search('[0-9]$', txt)
    return bool(test)

print('num at end of string:', check_num_end('azerty8'))

# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. 
def check_num_len(txt):
    test = re.findall('[0-9]{1,3}', txt)
    test = [n for n in test]
    return test

print("* re.findall('[0-9]{1,3}', txt) findall for any instances:", check_num_len('aze 1857 54azer'))

# 19. Write a Python program to search some literals strings in a string.
def check_word(w):
    test = re.search(w, 'The quick brown fox jumps over the lazy dog.')
    return bool(test)

print('check word fox:', check_word('fox'), '/horse:', check_word('horse'), '/dog:', check_word('dog'))

# 20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
def check_loc(w, txt):
    print('* re.finditer group() start() end():', end=' ')
    for n in re.finditer(w, txt, flags=re.I):
        print(n.group(), f'{n.start()}:{n.end()}', end=' /')

check_loc('the', 'The quick brown fox jumps over the lazy dog.')

# 21. Write a Python program to find the substrings within a string.
print()
check_loc('exercises', 'Python exercises, PHP exercises, C# exercises')

# 23. Write a Python program to replace whitespaces with an underscore and vice versa. 
def sub_ws(txt):
    txt = re.sub('_', '*', txt)
    txt = re.sub(' ', '_', txt)
    return re.sub('\*', ' ', txt)

print('\n* re.sub:', sub_ws('Write a Python program to replace whitespaces with an_underscore_and_vice_versa.'))

# 24. Write a Python program to extract year, month and date from an url.
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
def check_date(txt):
    match = re.search('\d{4}/\d{1,2}/\d{1,2}', txt)
    return f"{match.group()} /pos in string > {match.start()}:{match.end()}"

print('find date in url (\d for numeral):', check_date(url1))

# 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
def date_convert(date):
    return re.sub('(\d{4})/(\d{1,2})/(\d{1,2})', '\\3/\\2/\\1', date)

print('call element () by number \\1 \\2 etc... to reverse date // 2021/12/5', date_convert('2021/12/5'))

# 26. Write a Python program to match if two words from a list of words starting with letter 'P'.
print('* re.match \W opposite to \w, two words begin with p: ', end='')
def check_P(pair_list):
    for n in pair_list:
        test = re.match('^(p\w+)\W(p\w+)$', n, flags=re.I)
        if test:
            print(test.group(), end=', ')
        else:
            print('None', end =', ')
        
check_P(['Pala pinto','Mina Tala','punto Pata'])

# 27. Write a Python program to separate and print the numbers of a given string.
print('\n* re.findall /extract nums in string:', end=' ')
def check_nums(txt):
    for n in re.findall('\d+', txt):
        print(n, end=', ')

check_nums('aze7rt89u2301io1p')

# 28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
print("\n* re.findall('[ae]\w+', txt, flags=re.I) /any word begin with a or e:", end=' ')
def check_ae(txt):
    for n in re.findall('[ae]\w+', txt, flags=re.I):
        print(n, end=', ')

check_ae('Aasas, sdd ertrtf qsdt asds eaef.')

# 29. Write a Python program to separate and print the numbers and their position of a given string. 
print('\n* re.finditer /locate any num:', end=' ')
def locate_num(txt):
    for n in re.finditer('\d+', txt):
        print(f'{n.group()} at pos {n.start()}:{n.end()}', end=', ')

locate_num('azeeze898qaszdfd32qsd3.x75@+')

# 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
def road_abr(txt):
    return re.sub('road', 'Rd', txt, flags=re.I)

print('\n* re.sub / Road >> Rd:', road_abr('Lincoln Thomas, 16 Abbey Road, London south.'))

# 31. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def place_colon(txt):
    return re.sub('[ ,.]', ':', txt)

print("* re.sub('[ ,.]', ':':", place_colon('The wizzard, full of joy, lies continuously.'))

# 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon. 
def place_colon(txt):
    return re.sub('[ ,.]', ':', txt, 2)

print("* re.sub('[ ,.]', ':', txt, 2) same but only 2 times:", place_colon('The wizzard, full of joy, lies continuously.'))

# 34. Write a Python program to find all three, four, five characters long words in a string.
print("* re.findall(r'\\b\w{3,5}\\b', txt) /\\b for begin and end of a world:", end=' ')
def five_long(txt):
    for n in re.findall(r'\b\w{3,5}\b', txt):
        print(n, end=', ')

five_long('asq azer aztry qsdfg kj h lkjkl')
print()

# 35. Write a Python program to find all words which are at least 4 characters long in a string.
print("* re.findall(r'\\b\w{4,}\\b', txt) /{4,} mean 4 or more:", end=' ')
def five_long(txt):
    for n in re.findall(r'\b\w{4,}\b', txt):
        print(n, end=', ')

five_long('asq azer aztry qsdfg kj h lkjklihjgjfhfd')
print()

# 36. Write a python program to convert camel case string to snake case string.
def camel_to_snake(txt):
    txt = re.sub('(.)([A-Z]\w+)', r'\1_\2', txt).lower()
    return txt

print("* re.sub('(.)([A-Z]\w+)', r'\\1_\\2', txt).lower() /PythonExercices:", camel_to_snake('PythonExercices'))

# 37. Write a python program to convert snake case string to camel case string.
def snake_to_camel(txt):
    return ''.join(x.capitalize() for x in txt.split('_'))

print("''.join(x.capitalize() for x in txt.split('_')) /python_exercices:", snake_to_camel('python_exercices'))

# 38. Write a Python program to extract values between quotation marks of a string. 
def quotes(txt):
    return re.findall('\w+', txt)

print("* re.findall('\w+', txt) :", quotes('"Python", "PHP", "Java"'))

# 39. Write a Python program to remove multiple spaces in a string.
def remove_spaces(txt):
    return re.sub(' +', ' ', txt)

print("* re.sub(' +', ' ', txt) / remove multispaces:", remove_spaces('qsdqsd      sdqsdqsd            qssd'))

# 41. Write a Python program to remove everything except alphanumeric characters from a string.
def only_alpha(txt):
    return re.sub('[^\w]*', '', txt)

print("* re.sub('[^\w]*', '', txt) /remove non-alpha:", only_alpha('@azddg56465___--++*/lkjfsdr("'))

# 42. Write a Python program to find urls in a string.
def find_url(txt):
    return re.findall('http[s]?://[wwww]?.\w+.\w{2,3}', txt)

print("* re.findall('http[s]?://[wwww]?.\w+.\w{2,3}', txt) / find url:", find_url('<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'))

# 43. Write a Python program to split a string at uppercase letters
def split_upper(txt):
    return re.findall('[A-Z][a-z]*', txt)

print("* re.findall('[A-Z][a-z]*', txt) /split by uppers:", split_upper('AzertyUiopQsdfGhJkll'))

# 45. Write a Python program to remove the ANSI escape sequences from a string.
def rem_ansi(txt):
    return re.sub('\u001b\[[\d\w]{2}m*', '***', txt)

print("* re.sub /replace ANSI with ***:", rem_ansi('\u001b[31mHelloWorld\u001b[0m'))

# 46. Write a Python program to find all adverbs and their positions in a given sentence.
print("* re.finditer('\w+ly', txt) /find adverbs:", end=' ')
def find_adverb(txt):
    for n in re.finditer('\w+ly', txt):
        print(f'{n.group()} at pos {n.start()}:{n.end()}', end=', ')

find_adverb('I now see clearly you eated mostly the whole meat!')

# 47. Write a Python program to split a string with multiple delimiters.
print()
def delimiters(delim, txt):
    return re.split(delim, txt)

print("* re.split /with multiple delimiters:", delimiters(',|\n|\*', 'The delimiters, usually\n when appl*ied, can slice hard!'))

# 48. Write a Python program to check a decimal with a precision of 2. 
def decimal(num):
    test = re.search('^\d+(\.\d{0,2})?$', num)
    return bool(test)

print("re.search('^\d+(\.\d{0,2})?$' /decimal with precision of 2 max:", decimal('12.32'), decimal('15.321'))

# 49. Write a Python program to remove words from a string of length between 1 and a given number.
def rem_words(n, txt):
    return re.sub('\w+', '', txt, n)

print("* re.sub('\w+', '', txt, n) /remove n words:", rem_words(4, 'Write a Python program to remove words'))

def rem_words2(txt):
    return re.sub(r'\W*\b\w{1,3}\b', '', txt)

print("* re.sub(r'\W*\\b\w{1,3}\\b', '', txt) /remove words len{1,3}:", rem_words2('Write a Python program to remove words'))

# 50. Write a Python program to remove the parenthesis area in a string. 
print("* re.sub('\(.*\)', '' /remove content of ():", end=' ')
Sample_data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
def rem_parent(txt):
    for n in txt:
        print(re.sub('\(.*\)', '', n), end=', ')

rem_parent(Sample_data)
print()

# 51. Write a Python program to insert spaces between words starting with capital letters.
def insert_space(txt):
    return re.sub('(\w)([A-Z])', r'\1 \2', txt)

print("* re.sub('(\w)([A-Z])', r'\\1 \\2' /insert space before upper:", insert_space('AlohaMisterPresident!'))

"""
52. Write a Python program that reads a given expression and evaluates it.
Terms and conditions:
The expression consists of numerical values, operators and parentheses, and the ends with '='.
The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
When two operators have the same precedence, they are applied to left to right.
You may assume that there is no division by zero.
All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.
-1 ? 10 9 = intermediate results of computation = 10 9
"""
import re

class c(int):
    def __add__(self,n):
        return c(int(self)+int(n))
    def __sub__(self,n):
        return c(int(self)-int(n))
    def __mul__(self,n):
        return c(int(self)*int(n))
    def __truediv__(self,n):
        return c(int(int(self)/int(n)))

inp = '9*(2+4)-(6*2)/10'
print('* eval maths:', inp, end=' ')
print('=', eval(re.sub(r'(\d+)',r'c(\1)',inp)))

# 53. Write a Python program to remove lowercase substrings from a given string.
rem_low = lambda txt: re.sub('[a-z]', '', txt)
print("* lambda txt: re.sub('[a-z]', '', txt) //remove lower:", rem_low('AZERTYqsdfgWXCvvbN?.;kijJK'))

