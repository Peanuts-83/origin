#! /usr/bin/env python3.7

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)
        print('push : ', val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        print('pop : ', val)
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def get_counter(self):
        print('counter : ',self.__count)

    def pop(self):
        self.__count += Stack.pop(self)
	    

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
