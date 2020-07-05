from typing import List

from test_framework import generic_test, test_utils

from collections import deque
from math import factorial

def permutations(A: List[int]) -> List[List[int]]:
    res = deque(maxlen=factorial(len(A)))
    for i in range(len(A)) :
        if len(A) == 1 :
            return [[A[0]]]
        res.extend([ [A[i]] + l for l in permutations(A[:i] + A[i+1:]) ])
    return list(res)

def permutations_faster(A: List[int]) -> List[List[int]]:
    n = len(A)
    remaining = set(A)
    stack = deque([],maxlen=n)
    res = deque([],maxlen = factorial(n))
    def appendPermutatins() -> None :
        if len(stack) == n :
            res.append(list(stack))
            return
        for i in list(remaining) :
            stack.append(i)
            remaining.remove(i)
            appendPermutatins()
            remaining.add(i)
            stack.pop()
    appendPermutatins()
    return list(res)

'''
uses no additional space by rearranging the array
'''
def permutations_fastest(A : List[int]) -> List[List[int]] :
    n = len(A)
    res = deque([],maxlen=factorial(n))
    def appendPermutation(i : int) -> None :
        if i == n -1:
            res.append(A.copy())
        for j in range(i , n) :
            A[i], A[j] = A[j], A[i]
            appendPermutation(i +1)
            A[i], A[j] = A[j], A[i]
    appendPermutation(0)
    return list(res)

'''
Alternative approach 
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations_fastest,
                                       test_utils.unordered_compare))
