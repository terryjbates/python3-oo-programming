#!/usr/bin/env python

class MyNum(object):
    def __init__(self, value=0):
        try:
            value = int(value)
        except ValueError:
            value = 0
        print('Calling __init__')
        self.val = value

    def increment(self):
        self.val = self.val + 1

dd = MyNum('hello')
dd.increment()