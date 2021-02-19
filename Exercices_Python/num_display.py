numbers =  [('###   # ### ### # # ### ### ### ### ### '),
            ('# #   #   #   # # # #   #     # # # # # '),
            ('# #   # ### ### ### ### ###   # ### ### '),
            ('# #   # #     #   #   # # #   # # #   # '),
            ('###   # ### ###   # ### ###   # ### ### ')]

def convert_num(u_n):
    for i in range(5):
        print()
        for j in u_n:
            print(numbers[i][int(j)*4 : int(j)*4+4], end="")
    print()

while 1:
    user_num = input("Enter nums : ")
    user_num = list(user_num)
    convert_num(user_num)