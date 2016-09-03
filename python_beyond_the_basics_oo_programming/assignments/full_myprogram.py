#!/usr/bin/env python

import sys

#################################
# in a file called full_myprogram.py #
#################################

def doubleit(x):
    var = x * 2
    return var

if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print("The value of {0} is {1}".format(input_val, doubled_val))

####################################
# in a file called test_program.py #
####################################
import myprogram

def test_doublelit():
    assert full_myprogram.doubleit(10) == 20
