#!/usr/bin/env python3

import sys
import os




def main():
    word_count = 0
    line_count = 0
    char_count = 0

    with open('word_count.tst') as infile:
        for line in infile:
            line_count += 1
            word_list = line.split()
            word_count += len(word_list)
            for word in word_list:
                char_count += len(word)

    print "Lines: {0}\nWords: {1}\nChars:{2}".format(line_count,word_count,char_count)


if __name__ == "__main__":
    main()

