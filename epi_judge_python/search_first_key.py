from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l, r = 0, len(A) -1
    while l <= r :
        m = l + (r-l) // 2
        if k < A[m] :
            r = m - 1
        elif A[m] < k :
            l = m + 1
        else :
            r = m
            if l == r :
                return r
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
