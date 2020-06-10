import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# # Solution 1 by doing two pivots one for < and one for ==
# def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
#     pivot = A[pivot_index]
#     # first partition by < and >= pivot
#     il = 0
#     ige = len(A) - 1
#     while il < ige:
#         if A[il] < pivot:
#             il += 1
#         else:
#             temp = A[il]
#             A[il] = A[ige]
#             A[ige] = temp
#             ige -= 1
#
#     # then the rest of the array is >= pivot, so not parition by = and > than pivot
#     ie = il + 1 if A[il] < pivot else il
#     ig = len(A) - 1
#     while ie < ig:
#         if A[ie] == pivot:
#             ie += 1
#         else:
#             temp = A[ie]
#             A[ie] = A[ig]
#             A[ig] = temp
#             ig -= 1
#     return

# Solution 2 by doing one pivot and passing over values that are ==
# def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
#     pivot = A[pivot_index]
#     # first partition by < and >= pivot
#     il = 0
#     curr = 0
#     ig = len(A) -1
#     while curr <= ig:
#         if A[curr] < pivot:
#             temp = A[il]
#             A[il] = A[curr]
#             A[curr] = temp
#             il += 1
#             curr += 1
#         elif A[curr] > pivot:
#             temp = A[curr]
#             A[curr] = A[ig]
#             A[ig] = temp
#             ig -= 1
#         else :
#             curr += 1
#     return

# REDO
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    ltNext = 0
    gtNext = len(A) -1
    curr = 0
    while curr <= gtNext :
        if A[curr] < pivot :
            if curr != ltNext :
                A[curr],A[ltNext] = A[ltNext], A[curr]
            ltNext += 1
            curr += 1
        elif A[curr] > pivot :
            A[curr], A[gtNext] = A[gtNext], A[curr]
            gtNext -= 1
        else :
            curr +=1

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
