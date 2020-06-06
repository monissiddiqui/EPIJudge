from typing import List

from test_framework import generic_test


def find_maximum_subarray_greedy(A: List[int]) -> int:
    n = len(A)
    t = [[0]*n] * n
    '''
    An answer can be produced greedily by using a sliding window.
    Expand the window only if the current value is not larger than
    the current sum including the current value (if the current window 
    is negative in value) 
    '''
    currSum = 0
    maxSum = 0
    for a in A :
        currSum = max(a, a + currSum)
        maxSum = max(maxSum,currSum)
    return maxSum

def find_maximum_subarray(A: List[int]) -> int :
    '''
    Given a subarray A[0..k] where k < n, the maximum subarray value
    containing A[k] at the right end is S[k] minus the smallest subarray
    S[j] for j<= k.

    So what we can do as we iterate is to keep track of the current
    cumulative sum S[k] at index k<=n and keep track of what the minimum
    cumulative sum seen so far and then update the max to be the current
    max or S[k] - S[m] where S[m] is the minimum subarray so far.
    '''
    maxSum = 0
    minSum = 0
    cumSum = 0
    for a in A:
        cumSum += a
        minSum = min(minSum,cumSum)
        maxSum = max(maxSum,cumSum-minSum)
    return maxSum



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
