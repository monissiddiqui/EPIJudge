from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    '''
    first sort the array. Then iterate through each number
    in the list, setting the current target to be t-A[i].
    This gives us the number to be the new
    '''
    A.sort()
    for a in A :
        i , j = 0,len(A)-1
        while i <= j :
            key = A[i] + A[j]
            if key == t - a:
                return  True
            elif key < t-a :
                i += 1
            else :
                j -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
