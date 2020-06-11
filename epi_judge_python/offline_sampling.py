import functools
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

from random import randrange

def random_sampling(k: int, A: List[int]) -> None:
    '''
    All subsets should be equally likely. If there are N choose k subsets and each of them
    should be equally likely. This means that each subset has an overall likelihood of
    1/(math.comb(n,k) = (k*(k-1)*...*2*1/(n*(n-1)*...*(n-k+2)*(n-k+1).

    Assuming each element from the array is chosen iteratively and independently from the previous
    elements selected, a random subset can be constructed as follows:

    Amongst the first n elements, k will need to be selected and each element is equally likely so

    Then once that element is selected, any one of the remaining elements is equally likely to
    selected as the next element in the array.
    '''

    i = 0
    for i in range(k) :
        r = randrange(i,len(A))
        A[i], A[r] = A[r], A[i]

@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
