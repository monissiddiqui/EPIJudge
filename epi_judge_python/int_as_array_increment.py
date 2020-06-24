from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    i = len(A) -1
    while i >=0 and carry > 0 :
        carry,A[i] = (carry + A[i]) //10, (carry + A[i]) %10
        i -= 1
    return A if not carry else [carry] + A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
