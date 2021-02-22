#! /usr/bin/env python3.7

"""tada = ['12','13','14']
if set(['12','14','13']).issubset(tada) \
    or ('23'and'24') in tada:
  print("yes")
else:
  print("no")
for i in tada:
  print(i)

board = ["1","2","X","4","X","6","7","8","9"]
X_fields = []
counter = -1
for i in board:
	counter += 1
	print(i)
	x = counter%3 +1
	y = counter//3 +1
	print("^",x,y)
	if i == "X":
		if (x,y) not in X_fields:
			X_fields.append((x,y))
print(X_fields)"""

numbers =  [('  # ### ### # # ### ### ### ### ### ###'),
            ('  #   #   # # # #   #     # # # # # # #'),
            ('  # ### ### ### ### ###   # ### ### # #'),
            ('  # #     #   #   # # #   # # #   # # #'),
            ('  # ### ###   # ### ###   # ### ### ###')]

choice = '4'
for n in range(5):
	for i in choice:
		print(numbers[n][(int(i)*3)+1:(int(i)*3)+5])