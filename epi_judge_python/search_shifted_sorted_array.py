from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    l,r = 0, len(A) -1
    m = 0
    while l <= r :
        m = (l+r)//2
        if (m >0 and A[m-1] > A[m]) :
            return m
        elif A[r] < A[m] :
            l = m+1
        else :
            r = m-1
    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
