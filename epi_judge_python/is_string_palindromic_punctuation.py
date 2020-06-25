from test_framework import generic_test

import string

def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) -1
    permissible = set(string.ascii_letters) | set(string.digits)
    while i < j :
        if s[i] not in permissible :
            i +=1
        elif s[j] not in permissible :
            j -= 1
        elif s[i].lower() != s[j].lower() :
            return False
        else:
            j-=1
            i+=1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
