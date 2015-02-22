#!/usr/bin/env python3

__author__ = 'tbates'
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                            help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()

    print("options:", options)
    print("arguments:", args)
main()