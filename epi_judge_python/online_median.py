from typing import Iterator, List

from test_framework import generic_test

import heapq
from collections import deque
from statistics import mean

def online_median(sequence: Iterator[int]) -> List[float]:
    first = next(sequence,None)
    if first is None : return []
    minHeap = [first]
    maxHeap = [-first]
    medians = deque([first])
    isOddElement = False
    for s in sequence:
        if s < -maxHeap[0] :
            if isOddElement :
                heapq.heappush(maxHeap,-s)
                heapq.heappush(minHeap,-maxHeap[0])
            else :
                -heapq.heapreplace(maxHeap,-s)
        elif s > minHeap[0] :
            if isOddElement :
                heapq.heappush(minHeap,s)
                heapq.heappush(maxHeap,-minHeap[0])
            else:
                heapq.heapreplace(minHeap,s)
        else :
            if isOddElement  :
                heapq.heappush(minHeap,s)
                heapq.heappush(maxHeap,-s)
            # otherwise in previous iteration tops of both heaps are equal, so new element is equal to
            # it and we can ignore it
        medians.append((-maxHeap[0]+minHeap[0])/2)
        isOddElement ^= True

    return list(medians)


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
