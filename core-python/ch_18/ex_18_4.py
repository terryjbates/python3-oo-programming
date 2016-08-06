#!/usr/bin/env python
import sys
import os
from myThread import MyThread


NUM_OF_THREADS = 4
SEARCH_TERM = 'exquisite'


def findall(search_term, input_line):
    """Yields all the positions of the pattern p in the string s."""
    #print("search_term: {}".format(search_term.strip()))
    #print("input_line: {}".format(input_line))
    result = input_line.find(search_term)

    while result != -1:
        print("Found {}".format(search_term))
        yield result
        result = input_line.find(search_term, result+1)


def process_file(filename, shard_num, end_offset, search_term=SEARCH_TERM):
    with open(filename, 'r') as f:
        f.seek(shard_num * NUM_OF_THREADS)

        for index, line in enumerate(f):
            #print("line: {}".format(line.strip()))
            for i in findall(search_term, line):
                print("Line: {} Pos: {}".format(index + 1, i))
                print(line.strip())
                print()

def get_partitions(file_size, num_of_shards):
    """Return a dict of shards, shard number for key, tuple of offsets for value."""
    shard_dict = {}
    shard_size = file_size / num_of_shards
    for index, shard in enumerate(range(num_of_shards)):
        start_offset = index * shard_size
        end_offset = start_offset + shard_size - 1
        shard_dict[index] = end_offset
    return shard_dict


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
    partitions = get_partitions(total_size, NUM_OF_THREADS)
    funcs = [process_file]
    nfuncs = range(len(funcs))
    threads = []
    for i in nfuncs:
        for shard_index, end_offset in partitions.items():
            t = MyThread(funcs[i], (filename, shard_index, end_offset, word_to_search),
                funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()





if __name__ == "__main__":
    main()