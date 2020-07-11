import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from itertools import product

def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    rowSets = [set(range(1,10)) for _ in range(9)]
    columnSets = [set(range(1,10)) for _ in range(9)]
    boxSets = [set(range(1,10)) for _ in range(9)]
    for r in range(9):
        for c in range(9) :
            if partial_assignment[r][c] != 0 :
                b = 3 * (r // 3) + (c//3)
                val = partial_assignment[r][c]
                rowSets[r].remove(val)
                columnSets[c].remove(val)
                boxSets[b].remove(val)
    count = [0]
    def setNumber(r: int, c : int) -> bool :
        nonlocal count
        print(count)
        count[0] += 1
        b = 3* (r//3) + (c//3)
        if partial_assignment[r][c] != 0 :
            return True
        for val in range(1,10) :#rowSets[r] & columnSets[c] & boxSets[b] :
            if val not in rowSets[r] & columnSets[c] & boxSets[b] :
                continue
            partial_assignment[r][c] = val
            rowSets[r].remove(val)
            columnSets[c].remove(val)
            boxSets[b].remove(val)
            isBadValue = False
            for i in range(9) :
                if i != r :
                    if not setNumber(i,c) :
                        isBadValue = True
                        break
                if i != c :
                    if not setNumber(r,i) :
                        isBadValue = True
                        break
            if isBadValue :
                partial_assignment[r][c] = 0
                rowSets[r].add(val)
                columnSets[c].add(val)
                boxSets[b].add(val)
            else :
                break
        return partial_assignment[r][c] != 0
    return all(setNumber(r,c) for r,c in product(range(9),repeat=2))


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
