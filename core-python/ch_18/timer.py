# Import timings

import time


class Timer(object):
    def __init__(self, verbose=True):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)


def timing_decorator(func):
    def func_wrapper(*args, **kwargs):
        with Timer() as t:
            query_results = func(*args, **kwargs)
        print('Elapsed time to process query: {0}'.format(t.secs))
        return query_results

    return func_wrapper
