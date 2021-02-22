#! /usr/bin/env python3.7

class QueueError(LookupError):  # Choose base class for the new exception.
    def __init__(self):
        print("Queue error")

class Queue:
    def __init__(self):
        self.__lst = []

    def put(self, elem):
        self.__lst.insert(0,elem)
        print('putting ',elem)

    def get(self):
        x = self.__lst.pop()
        return x


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    er = QueueError()
