#!/usr/bin/env python3

import pdb


def doubleval(argsum, val):
    argsum = 0
    newval = argsum + val
    return newval

#pdb.set_trace()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0

for val in values:
    mysum = doubleval(mysum, val)

print(mysum)