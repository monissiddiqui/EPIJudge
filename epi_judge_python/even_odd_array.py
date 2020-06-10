import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# # my solution
# def even_odd(A: List[int]) -> None:
#     ie = 0
#     io = len(A) -1
#     while ie < io :
#         if A[ie] % 2 == 0 :
#             ie += 1
#         elif A[io] % 2 == 1 :
#             io -= 1
#         else :
#             temp = A[ie]
#             A[ie] = A[io]
#             A[io] = temp
#             ie += 1
#             io -= 1
#     return A

# # Book solution
# def even_odd(A: List[int]) -> None:
#     ie = 0
#     io = len(A) - 1
#     while ie < io :
#         if A[ie] % 2 == 0 :
#             ie += 1
#         else :
#             temp = A[ie]
#             A[ie] = A[io]
#             A[io] = temp
#             io -= 1

# redo problem
def even_odd(A: List[int]) -> None:
    end = 0
    for i,a in enumerate(A) :
        if a % 2 == 0 :
            A[i], A[end] = A[end],A[i]
            end +=1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
