from test_framework import generic_test
from collections import Counter


# def is_letter_constructible_from_magazine(letter_text: str,
#                                           magazine_text: str) -> bool:
#     lCount = Counter(letter_text)
#     for s in magazine_text :
#         if s in lCount:
#             lCount[s] -= 1
#         if lCount[s] == 0 :
#             del lCount[s]
#             if not lCount :
#                 return True
#     return not lCount
#
# def is_letter_constructible_from_magazine_pythonic(letter_text: str,
#                                           magazine_text: str) -> bool:
#     return not (Counter(letter_text) - Counter(magazine_text))

# Redo problem
def is_letter_constructible_from_magazine(letter_text: str,
                                              magazine_text: str) -> bool:
    letterCount = Counter(letter_text)
    for c in magazine_text :
        if c in letterCount :
            letterCount[c] -= 1
            if letterCount[c] == 0 :
                del letterCount[c]
            if not letterCount :
                return True
    return not letterCount


def is_letter_constructible_from_magazine_python(letter_text: str,
                                          magazine_text: str) -> bool:
    return not Counter(letter_text) - Counter(magazine_text)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
