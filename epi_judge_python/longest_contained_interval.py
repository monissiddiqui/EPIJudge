from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    intervalSizes = {}
    maxSize = 0
    for a in A  :
        if a not in intervalSizes:
            intervalSizes[a] = a
            left,right = a,a
            if a-1 in intervalSizes :
                left = intervalSizes[a-1]
            if a +1 in intervalSizes :
                right  = intervalSizes[a+1]
            intervalSizes[right] = left
            intervalSizes[left] = right
            maxSize = max(right-left+1,maxSize)
    return maxSize

def longest_contained_range_with_removals(A: List[int]) -> int:
    elems = set(A)

    maxSize = 0
    while elems :
        a = elems.pop()
        count = 1
        l = a -1
        while l  in elems :
            elems.remove(l)
            l -=1
            count += 1
        u = a+1
        while u in elems :
            elems.remove(u)
            u += 1
            count += 1
        maxSize = max(maxSize,count)
    return maxSize


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
