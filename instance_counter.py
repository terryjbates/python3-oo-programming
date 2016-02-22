#!/usr/bin/env python

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(12)
c = InstanceCounter(17)

for obj in (a, b, c):
    print ("val of obj: {}".format(obj.get_val()))
    print ("count: {}".format(obj.get_count()))