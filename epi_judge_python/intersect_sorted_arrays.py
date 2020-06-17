from typing import List
from bisect import bisect
from collections import deque
from math import log2

from test_framework import generic_test

# def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
#
#     if not (A and B) :
#         return []
#     smaller, larger = (A, B) if len(A) <= len(B) else (B,A)
#     if len(smaller) * (log2(len(B)) + 0.00001) < len(larger) :
#         return intersect_two_sorted_arrays_skewed_sizes(smaller,larger)
#     else :
#         return intersect_two_sorted_arrays_similar_sizes(smaller,larger)
#
# def intersect_two_sorted_arrays_skewed_sizes(A: List[int], B: List[int]) -> List[int]:
#     j = 0
#     result = deque(maxlen=len(A))
#     for i in range(len(A)) :
#         j = bisect(B,A[i],lo=j) - 1
#         if j == len(B): return result
#         elif j < 0 :
#             j = 0
#             continue
#         if A[i] == B[j] and (not result or result[-1] != A[i]) :
#             result.append(A[i])
#     return list(result)
#
# def intersect_two_sorted_arrays_similar_sizes(A: List[int], B: List[int]) -> List[int]:
#     result = deque(maxlen=min(len(A),len(B)))
#     i, j = 0,0
#     while i < len(A) and j < len(B) :
#         if A[i] == B[j] :
#             if not result or result[-1] != A[i] :
#                 result.append(A[i])
#             i += 1
#             j += 1
#         elif A[i] < B[j] :
#             i += 1
#         else :
#             j += 1
#     return list(result)
#
# def intersect_two_sorted_arrays_pythonic(A: List[int], B: List[int]) -> List[int]:
#     return sorted(list(set(A) & set(B)))

# redo problem
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    s,l = (A,B) if len(A) <= len(B) else (B,A)
    if len(s) == 0 :
        return []
    l.sort()
    ret = deque([],maxlen=len(s))
    i = 0
    for x in s :
        if ret and ret[-1] == x : continue
        i = bisect(l,x,lo=i)
        if l[i-1] == x :
            ret.append(x)
    return list(ret)

def intersect_two_sorted_arrays_pythonic(A: List[int], B: List[int]) -> List[int]:
    return sorted(list(set(B) & set(A)))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays_pythonic))
