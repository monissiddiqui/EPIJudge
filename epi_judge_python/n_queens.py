from typing import List

from test_framework import generic_test

from collections import deque

def n_queens(n: int) -> List[List[int]]:
    if n == 0 : return []
    remainingCols = set(range(n)) # c
    remainingLRDiags = set(range(-n,n))  # c - r
    remainingRLDiags = set(range(0,2*n-1)) # c + r

    currentQueens = deque([],maxlen=n)
    successfulPlacements = deque([])

    def findRemainingPlacementsFromRow(r: int) :
        if len(currentQueens) == n :
            successfulPlacements.append(list(currentQueens))
        for c in list(remainingCols) :
            if c-r in remainingLRDiags and c+r in remainingRLDiags :
                currentQueens.append(c)
                remainingRLDiags.remove(c+r)
                remainingLRDiags.remove(c-r)
                remainingCols.remove(c)
                findRemainingPlacementsFromRow(r+1)
                remainingRLDiags.add(c+r)
                remainingLRDiags.add(c-r)
                remainingCols.add(c)
                currentQueens.pop()

    findRemainingPlacementsFromRow(0)
    return list(successfulPlacements)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
