from typing import Iterator, List

from test_framework import generic_test

import heapq
from collections import deque

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # only need a window of k + 1 elements to sort the array since for any element v at index j >= k,
    # it is possible for j to be anywhere in the interval of indices [j-k,j+k] in the sorted array.
    # Thus keeping a heap size of k+1 will be a sufficiently large enough window to cover all of v's
    # possible positions
    val = None
    heap = deque()
    for _ in range(k+1) :
        val = next(sequence,None)
        if val is None : break
        heap.append(val)
    if not heap: return []
    heap = list(heap)
    heapq.heapify(heap)

    res = deque()
    for val in sequence :
        res.append(heapq.heapreplace(heap,val))
    while heap :
        res.append(heapq.heappop(heap))
    return list(res)


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
