from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    char,count = "",0
    for c in stream:
        if count == 0 :
            char = c
        if c != char :
            count -=1
        else:
            count += 1
    return char

def majority_search_redo(stream: Iterator[str]) -> str:
    counter = 0
    majorityElement = None
    for s in stream :
        if not counter :
            majorityElement = s
            counter += 1
        elif s == majorityElement :
            counter += 1
        else :
            counter -= 1
    return majorityElement

def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
