from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

import itertools

def find_missing_element(stream: Iterator[int]) -> int:

    counter = [0] * (1<<16)
    MASK = 0xFFFF0000
    stream,stream_copy = itertools.tee(stream,2)

    for ip in stream :
        counter[(ip & MASK) >> 16] += 1

    MS_HALF = 0
    for i,c in enumerate(counter) :
        if c < 1<<16 :
            MS_HALF = i << 16
            break
    counter = [0] * (1<<16)
    FILTER_MASK = MASK
    MASK = 0xFFFF
    for ip in stream_copy :
        if FILTER_MASK & ip == MS_HALF :
            counter[ip & MASK] += 1

    for lower_half,count in enumerate(counter) :
        if count == 0 :
            return MS_HALF | lower_half
    return -1
def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))    
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
