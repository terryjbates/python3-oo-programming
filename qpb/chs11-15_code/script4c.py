#! /usr/bin/env python3.1
import fileinput, glob, sys, os
def main():
    if os.name == 'nt':
        if sys.path[0]: os.chdir(sys.path[0])      #A
            sys.argv[1:] = glob.glob(input("Name of input file:"))
            sys.stdout = open(input("Name of output file:"),'w') #B
            for line in fileinput.input():
               if line[:2] != '##':
                   print(line, end="")
main()
