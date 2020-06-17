from typing import List

from test_framework import generic_test, test_utils

from collections import defaultdict

def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagramGroups = defaultdict(lambda : [])
    for word in dictionary :
        anagramGroups[''.join(sorted(word))].append(word)
    return [group for group in anagramGroups.values() if len(group) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
