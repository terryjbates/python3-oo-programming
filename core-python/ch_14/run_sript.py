#!/usr/bin/env python
"""Run other python scripts."""

import sys
import os


def main(argv):
    with open(argv[1]) as script:
        exec(script.read())


def usage():
    print("At least 2 args (incl. cmd name).")
    print("usage: run_script.py arg1 arg2 [arg3... ]")
    sys.exit(1)

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        usage()
    main(sys.argv)
     