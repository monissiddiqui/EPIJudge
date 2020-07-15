from typing import List

from test_framework import generic_test, test_utils

from collections import deque
import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k == 0 : return []
    kHeap = [(-A[0],0)]
    res = [0] * k
    for i in range(k) :
        p = kHeap[0][1]
        res[i] = A[p]
        l =2*p + 1
        if l < len(A) :
            heapq.heapreplace(kHeap,(-A[l],l))
            if l+1 < len(A) :
                heapq.heappush(kHeap,(-A[l+1],l+1))
        else :
            heapq.heappop(kHeap)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
