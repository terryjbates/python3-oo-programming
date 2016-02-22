#!/usr/bin/env python3
# __author__ = 'tbates'

import fileinput

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<start of file {0}>".format(fileinput.filename()))
        print(line.strip())

if __name__ == '__main__':
    main()
