#!/usr/bin/env python
"""Create custom exit function."""

import sys

prev_exit_func = getattr(sys, 'exitfunc', None)

def my_exit_func(old_exit=prev_exit_func):
    print("Exiting now MothaFuckaaaa.")
    if not old_exit and callable(old_exit):
        old_exit()

sys.exitfunc = my_exit_func