#!/usr/bin/env python
import sys
import os
from myThread import MyThread


NUM_OF_THREADS = 4


def findall(p, s):
    """Yields all the positions of the pattern p in the string s."""
    i = s.find(p)
    while i != -1:
        print("Found {}".format(p))
        yield i
        i = s.find(p, i+1)


def process_file(filename)
    print("Total file size in bytes: {}".format(total_size))
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            for i in findall(word_to_search, line):
                print(index + 1, i)
                print(line.strip())
                print()
            #print(line.strip())


def main():
    try:
        print(sys.argv[1])
        filename = sys.argv[1]
        word_to_search = sys.argv[2]
        print(word_to_search)
    except IndexError:
        print("Usage: ex_18_4.py <filename> <word>")
        sys.exit()
    total_size = os.path.getsize(filename)
    funcs = [process_file]
    nfuncs = range(len(funcs))
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops),
            funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()





if __name__ == "__main__":
    main()