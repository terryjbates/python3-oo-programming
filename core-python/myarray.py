#!/usr/bin/env python3
#
# myarray.py

from mystack import myStack
from myqueue import myQueue


class myArray(myStack, myQueue):

    def shift(self):
        super().dequeue()

    def unshift(self, x):
        self.insert(0, x)