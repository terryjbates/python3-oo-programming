#!/usr/bin/env python3

def tupleVarArg(arg1, arg2='defaultB', *theRest):
    "Display regular args and no-keyword variable args."
    print('formal arg 1: ', arg1)
    print('formal arg 2:', arg2)
    for extra_arg in theRest:
        print('another arg:', extra_arg)
