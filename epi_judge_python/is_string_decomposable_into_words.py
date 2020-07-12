import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import deque

def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    decomposition = deque([],maxlen=len(domain))
    visited = set()
    def searchForWordFrom(i : int) -> bool :
        if i == len(domain) : return True
        if i in visited : return False
        visited.add(i)
        j = i +1
        while j <= len(domain) :
            decomposition.append(domain[i:j])
            if domain[i:j] in dictionary and searchForWordFrom(j) :
                return True
            decomposition.pop()
            j+=1
        return False
    searchForWordFrom(0)
    return list(decomposition)

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
