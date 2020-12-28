# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name

def split_name(name):
    name = name.split(' ')
    first_name = name[0]
    last_name = ' '.join(name[1:])
    return {
        'first_name': first_name,
        'last_name': last_name,
    }
assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# 3) Write an `is_palindrome` function to check if a nam is a palindrome (reads the same from left-to-right and right-to-left)
def is_palindrome(name):
    if type(name) is str:
        if name == ''.join(reversed(name)):
            return True
        else:
            return False
    elif type(name) is int:
        if name == int(''.join(reversed(str(name)))):
            return True
        else:
            return False

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
def build_list(k,*args):
        try:
            return [k for _ in range(args[0])]
        except IndexError:
            return [k]

assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
