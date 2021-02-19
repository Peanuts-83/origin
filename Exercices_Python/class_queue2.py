#! /usr/bin/env python3.7

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.counter = 0

    def put(self, elem):
        Queue.put(self,elem)
        self.counter += 1

    def get(self):
        issue = Queue.get(self)
        self.counter -= 1
        return issue

    def isempty(self):
        if self.counter == 0:
            val = True
        else:
            val = False
        return val

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
print(que.__dict__)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
