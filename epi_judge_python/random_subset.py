import functools
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

from random import randrange

def random_subset(n: int, k: int) -> List[int]:
    if k > n//2 : return list(set(range(n))-set(random_subset(n,n-k)))
    i = 0
    nums = list(range(n))
    for i in range(k):
        j = randrange(n-i) + i
        nums[i], nums[j] = nums[j], nums[i]
    return nums[:k]

def random_subset_efficient_space(n :int, k :int) -> List[int] :
    # if k > n// 2 : return random_subset_efficient_space(n,n-k)
    selected = {}
    for i in range(k) :
        if i not in selected :
            selected[i] = i
        j = randrange(i,n)
        if j not in selected :
            selected[j] = j
        selected[j],selected[i] = selected[i],selected[j]
    return [selected[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset_efficient_space(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
