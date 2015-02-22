#! /usr/bin/env python3.1
import fileinput
def main():
    for line in fileinput.input():
        if line[:2] != '##':
            print(line, end=" ")
main()
