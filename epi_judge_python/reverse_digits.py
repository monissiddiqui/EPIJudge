from test_framework import generic_test


def reverse(x: int) -> int:
    sign = 1
    if x <0 :
        sign = -1
        x = -x
    y = 0
    while x > 0 :
        y = 10*y + x%10
        x //= 10
    return sign*y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
