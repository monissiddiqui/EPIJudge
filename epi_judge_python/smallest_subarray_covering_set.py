import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

from collections import defaultdict

def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    i,j = 0,-1
    keywordCounts = defaultdict(lambda:0)
    minSubarray = Subarray(0,len(paragraph) -1)
    while j < len(paragraph) -1 or  len(keywordCounts) == len(keywords):
        if len(keywordCounts) < len(keywords)  :
            j += 1
            if paragraph[j] in keywords :
                keywordCounts[paragraph[j]] += 1
        else :
            if j-i < minSubarray.end - minSubarray.start :
                minSubarray = Subarray(i,j)
            if paragraph[i] in keywordCounts :
                keywordCounts[paragraph[i]] -= 1
                if keywordCounts[paragraph[i]] == 0 :
                    del keywordCounts[paragraph[i]]
            i += 1
    return minSubarray


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
