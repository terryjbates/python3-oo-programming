#!/usr/bin/env python3
__author__ = 'tbates'

import sys

def main():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))
main()
