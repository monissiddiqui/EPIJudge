import functools
from typing import List
from collections import deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    steps = deque()
    MASK = 1 ^ 2
    def move_n_rings_from_to(n, f,t : int) :
        o = MASK ^ f ^ t
        if n == 1 :
            steps.append([f,t])
        else:
            m = len(steps)
            move_n_rings_from_to(n-1,f,o)
            m = len(steps) - m
            steps.append([f,t])
            # could do another recursive call to get top
            # n-1 elements back on the 
            steps.extend([
                [(steps[i][0]+o-f) % 3,(steps[i][1]+o-f) % 3] for i in range(-m-1,-1)
            ])
            # move_n_rings_from_to(n-1,o,t)
    move_n_rings_from_to(num_rings,0,1)
    return steps


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
