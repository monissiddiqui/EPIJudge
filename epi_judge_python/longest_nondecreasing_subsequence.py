from typing import List, Deque

from test_framework import generic_test

from collections import deque

from bisect import bisect

def longest_nondecreasing_subsequence_length_dp(A: List[int]) -> int:
    max_nds = [1]*len(A)
    for j in range(1,len(A)) :
        for i in range(j)  :
            if A[i] <= A[j] and max_nds[i] >= max_nds[j] :
                max_nds[j] = max_nds[i] +1
    return max(max_nds)

def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    if len(A) ==0 : return []
    t : Deque[int] = deque([],maxlen=len(A))
    for a in A :
        i = bisect(t,a)
        print(i,a)
        if i == len(t) :
            t.append(a)
        else :
            t[i] = a
        print(t)
    return len(t)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
