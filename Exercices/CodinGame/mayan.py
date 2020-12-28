# Operation map
do_op = {'+':(lambda a,b:a+b),'*':(lambda a,b:a*b),'-':(lambda a,b:a-b),'/':(lambda a,b:a//b)}

# We get the numeral dimensions
w, h = [int(i) for i in input().split()]

# We store the numerals
lines = [input() for _ in range(h)]
numerals = ["\n".join([line[n*w:n*w+w] for line in lines]) for n in range(20)]

# We create a map to read digits
from_mayan = {str:n for (n, str) in enumerate(numerals)}

# Returns the value of a multiple digits number
def get_number():
    ans = 0
    for _ in range(int(input()) // h):
        ans = ans * 20 + from_mayan["\n".join([input() for _ in range(h)])]
    return ans

# Prints a given number in mayan
def print_mayan(x):
    if (x >= 20):
        print_mayan(x // 20)
    print(numerals[x % 20])

# Read the two numbers, compute the result and print it
a, b = get_number(), get_number()
print_mayan(do_op[input()](a, b))