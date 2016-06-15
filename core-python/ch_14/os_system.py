#!/usr/bin/env python
"""Use subprocess to call a program."""
import subprocess
import sys
from my_exit_func import my_exit_func as my_exit_func
sys.exitfunc = my_exit_func

COMMAND = '/bin/ls'


if __name__ == "__main__":
    subprocess.call([COMMAND, '.'], shell=False)
