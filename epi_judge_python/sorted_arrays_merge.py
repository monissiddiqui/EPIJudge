from typing import List
import heapq
from queue import Queue
from collections import deque

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    merged = deque([],sum([len(arr) for arr in sorted_arrays]))
    minHeap = []
    for i in range(len(sorted_arrays)) :
        heapq.heappush(minHeap, (sorted_arrays[i][0],i))
    indices = [1] * len(sorted_arrays)
    while len(minHeap) :
        val,iarr = minHeap[0]
        if indices[iarr] < len(sorted_arrays[iarr]) :
            heapq.heapreplace(minHeap,(sorted_arrays[iarr][indices[iarr]],iarr))
            indices[iarr] += 1
        else :
            heapq.heappop(minHeap)
        merged.append(val)

    return list(merged)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
