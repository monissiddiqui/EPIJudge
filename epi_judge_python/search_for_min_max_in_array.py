import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

from random import randrange

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max_random(A: List[int]) -> MinMax:
    if len(A) == 0: return None
    if len(A) == 1 : return MinMax(A[0],A[0])
    min,max = (A[0],A[1]) if A[0] <= A[1] else (A[1],A[0])
    for i in range(2,len(A)) :
        checkMinFirst = randrange(2)
        if checkMinFirst :
            if A[i] <= min :
                min = A[i]
            elif A[i] > max :
                max = A[i]
        else :
            if A[i] >= max :
                max = A[i]
            elif A[i] < min :
                min = A[i]
    return MinMax(min, max)

def find_min_max(A: List[int]) -> MinMax:
    minimum,maximum = A[-1],A[-1]
    for j in range(1,len(A),2) :
        s,b = (j-1,j) if A[j-1] < A[j] else (j, j-1)
        minimum = min(A[s],minimum)
        maximum = max(A[b],maximum)
    return MinMax(minimum,maximum)

def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
