#! /usr/bin/env python3.7

sudo1 = "295743861\
        431865927\
        876192543\
        387459216\
        612387495\
        549216738\
        763524189\
        928671354\
        154938672"
sudo2 = "195743862\
        431865927\
        876192543\
        387459216\
        612387495\
        549216738\
        763525189\
        928671354\
        254938671"

ref = [i for i in range(1,10)]
for i in sudo1.split():
    if ref != sorted([int(i) for i in list(i)]):
        print('no')
        exit()
print('yes')
print()
for i in sudo2.split():
    if ref != sorted([int(i) for i in list(i)]):
        print('no',)
        exit()
print('yes')