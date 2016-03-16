#!/usr/bin/env python3
#
# myqueue.py


class myQueue(list):
    def __init__(self):
        super().__init__()

    def dequeue(self):
        retval = self[0]
        del self[0]
        return retval

    def enqueue(self, x):
        self.append(x)

    def isempty(self):
        if len(self) > 1:
            return False
        return True

    def peek(self):
        return self[-1]

