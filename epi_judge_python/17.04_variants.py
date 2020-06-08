from typing import List

from test_framework import generic_test

'''
VARIANT 1
So1ve the same problem when the three elements must be distinct.
For example, if A = (5,2,3,4,3) and f = 9, then A[2] + A[2] + A[2]
is not acceptable, A[2] + A[2] + A[4]is not acceptable, but
A[1] + Al2l + A[3] and A[1] + A[3] + A[4] are acceptable.

VARIANT 2
Solve the same problem when k, the number of elements to sum,
is an additional input.

VARIANT 3
Write a program that takes as input an array of integers A and
an integer T, and returns a 3-tuple (A[p],A[q],A[r]) where p,q,r
are all distinct, minimizing [T - (A[p] + A[q] + A[r]), and
A[p] <= A[r] <= A[s]

VARIANT 4
Write a program that takes as input an array of integers A and an
integer T, and returns the number of 3-tuples (p,q,r) such that
A[p] + A[q] + A[r] <= T and A[p] <= A[q] <= A[r].

'''

'''
Variant 1
'''
def has_three_sum_distinct(A: List[int], t: int) -> bool:
    '''
    first sort the array. Then iterate through each number
    in the list, setting the current target to be t-A[i].
    then shrink the sorted array's ends untill the ends
    add up to the target. If there any of the ends
    are the same as the target's complement, then
    shring the ends accordingly.
    '''
    A.sort()
    for a in A :
        i , j = 0,len(A)-1
        while i <= j :
            if A[i] == A[j] :
                break
            elif A[i] == a :
                i += 1
                continue
            elif A[j] :
                j -= 1
                continue
            key = A[i] + A[j]
            if key == t - a:
                return  True
            elif key < t-a :
                i += 1
            else :
                j -= 1
    return False

'''
Variant 2 
there could be a O(n^(k-3)) structure to store the possible sums and then use the 
3 sum algorithm to compute against the target sums 
'''

'''
Variant 3
store the 3 tuples as we find a new minimum and store p,q,r in sorted order
'''

'''
Variant 4

do the same thing as the original problem but only increase the count if the 
inequality holds
'''

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum_distinct))
