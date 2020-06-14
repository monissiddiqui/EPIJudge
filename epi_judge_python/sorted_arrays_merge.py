from typing import List
import heapq
from queue import Queue
from collections import deque

from test_framework import generic_test


# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#
#     merged = deque([],sum([len(arr) for arr in sorted_arrays]))
#     minHeap = []
#     for i in range(len(sorted_arrays)) :
#         heapq.heappush(minHeap, (sorted_arrays[i][0],i))
#     indices = [1] * len(sorted_arrays)
#     while len(minHeap) :
#         val,iarr = minHeap[0]
#         if indices[iarr] < len(sorted_arrays[iarr]) :
#             heapq.heapreplace(minHeap,(sorted_arrays[iarr][indices[iarr]],iarr))
#             indices[iarr] += 1
#         else :
#             heapq.heappop(minHeap)
#         merged.append(val)
#
#     return list(merged)

# Redo problem
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [(l[0], i) for i, l in enumerate(sorted_arrays) if l]
    res = deque(maxlen=sum([len(l) for l in sorted_arrays]))
    heapq.heapify(heap)
    iOf = [1] * len(sorted_arrays)

    while heap:
        val, j = heap[0]
        heapq.heapreplace(heap,(sorted_arrays[j][iOf[j]], j)) if iOf[j] < len(sorted_arrays[j]) else heapq.heappop(heap)
        iOf[j] += 1
        res.append(val)

    return list(res)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
