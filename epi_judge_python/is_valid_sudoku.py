from typing import List

from test_framework import generic_test

import itertools

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    m = len(partial_assignment)
    n = len(partial_assignment[0])
    # checking rows
    for i in range(m) :
        numSet = 0
        for j in partial_assignment[i] :
            if j == 0 : continue
            if (1 << j) & numSet :
                return False
            numSet |= (1 << j)

    # checking columns
    for j in range(n) :
        numSet = 0
        for i in range(m) :
            if partial_assignment[i][j] == 0 : continue
            if (1 << partial_assignment[i][j]) & numSet :
                return False
            numSet |= (1 << partial_assignment[i][j])

    # Checking squares
    for r in (1,4,7):
        for c in (1,4,7) :
            numSet = 0
            for i,j in itertools.product(*[[-1,0,1]]*2) :
                if partial_assignment[r+i][c+j] == 0: continue
                if (1 << partial_assignment[r+i][c+j]) & numSet :
                    return False
                numSet |= (1 << partial_assignment[r+i][c+j])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
