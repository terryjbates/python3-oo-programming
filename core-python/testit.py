#!/usr/bin/env python3


def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, diag)
    return result


def test():
    funcs = (int, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print('-' * 20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print("{}({}) = {}".format(eachFunc.__name__, eachVal, retval[1]))
            else:
                print("{}({}) = FAILED".format(eachFunc.__name__, eachVal))


if __name__ == "__main__":
    test()