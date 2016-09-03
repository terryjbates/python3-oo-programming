#!/usr/bin/env python

class MaxSizeList(object):
    def __init__(self, size):
        self.list = []
        self.size = size

    def push(self, input_val):
        if len(self.list) < self.size:
            self.list.append(input_val)

    def get_list(self):
        return self.list


a = MaxSizeList(3)
a.push("hey")
a.push("is")
a.push("fork")
a.push("horses")
a.push("fartknocker")

print(a.list)

