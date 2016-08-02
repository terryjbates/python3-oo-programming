#!/usr/bin/env python

from myThread import MyThread
from time import ctime, sleep
from timer import timing_decorator as timing_deco


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x-1)


def sum(x):
    sleep(0.1)
    print("x is {}".format(x))
    if x < 2:
        return 1
    return x + sum(x-1)


@timing_deco
def single_thread(funcs, nfuncs):
    print("*** SINGLE THREAD")
    for i in nfuncs:
        print(funcs[i](n))

@timing_deco
def multi_thread(funcs,nfuncs):
    print("*** MULTI THREAD")
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], n, funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())


def main():
    nfuncs = range(len(funcs))
    single_thread(funcs, nfuncs)
    multi_thread(funcs, nfuncs)
    print("all DONE")

if __name__ == "__main__":
    funcs = [fib, fac, sum]
    n = 12
    main()