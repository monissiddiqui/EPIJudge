from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s: str) -> bool:
    charCounts = Counter(s)
    oddCountFound = False
    for count in charCounts.values() :
        if count % 2 == 1 :
            if oddCountFound :
                return False
            oddCountFound = True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
