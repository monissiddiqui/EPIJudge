from typing import List

from test_framework import generic_test


# def find_nearest_repetition(paragraph: List[str]) -> int:
#     minDistance = float("inf")
#     mostRecentLocation = {}
#     for i,word in enumerate(paragraph) :
#         if word in mostRecentLocation :
#             minDistance = min(i-mostRecentLocation[word], minDistance)
#         mostRecentLocation[word] = i
#
#     return minDistance if minDistance < float("inf") else -1

def find_nearest_repetition(paragraph: List[str]) -> int:
    lastOccurance = {}
    minDistance = float("inf")
    for i,word in enumerate(paragraph) :
        if word in lastOccurance :
            minDistance = min(i - lastOccurance[word],minDistance)
        lastOccurance[word] = i
    return minDistance if minDistance < float("inf") else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
