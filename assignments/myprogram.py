#!/usr/bin/env python3

import sys

#################################
# in a file called myprogram.py #
#################################

def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError("{0} is not a valid integer".format(x))
    var = x * 2
    return var


if __name__ == '__main__':
    input_val = sys.argv[1]

    doubled_val = doubleit(input_val)
    print("The value of {0} is {1}".format(input_val, doubled_val))
