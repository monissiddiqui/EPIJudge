from typing import List

from test_framework import generic_test

import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    '''
    largest element is done in O(N). To get the top k elements a heap is needed, but we don't need
    all of the k elements in this case, so a heap may be unnecessary. Only one element needs to be
    returned.

    One thing that can be done is pivot the array and store all greater values to the right. If
    the resultant index of the pivot element is less than n-k, the kth largest is in the
    right subarray. If the pivot index is greater than n-k, than iterate on the left subarray.

    Now how is the pivot value selected? If it can be shown that the pivot vaue splits the array into halves
    every time, then the total time will be O(N), but we sould have to know the median of the array beforehand.
    If a random element is used, say the first element, then worst cases re reached when the array is
    sorted, since no elements will be rearranged when doing the pivots and it will take n-k steps and hence
    O(n^2) .

    '''
    l,u = 0,len(A) -1
    pidx = None
    while l <= u :
        pidx = random.randint(l,u)
        p = A[pidx]
        i = l
        j = l
        while j <= u :
            if A[j] <= p :
                if i < j:
                    A[i],A[j] = A[j], A[i]
                if A[i] == p :
                    pidx = i
                i +=1
            j += 1
        A[pidx],A[i-1] = A[i-1],A[pidx]
        if i-1 == len(A)-k :
            return p
        elif i-1 < len(A)-k :
            l = i
        else :
            u = i-2

    return A[pidx]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
