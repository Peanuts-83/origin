# ### Generator #############
# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row

# ### generator in for loop
# csv_gen = csv_reader("LinuxAcademy/test.txt")
# row_count = 0
# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")

# ### generator comprehension
# csv_gen = (row for row in open('LinuxAcademy/test.txt'))
# row_count = 0
# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")

# ### Palindrome generator #############
# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0

#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10

#     if num == reversed_num:
#         return num
#     else:
#         return False

# for i in range(150):
#     pal = is_palindrome(i)
#     if pal:
#         print(pal)

### Palindrome generator advanced ########
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 10:
        pal_gen.close()
    pal_gen.send(10 ** (digits))