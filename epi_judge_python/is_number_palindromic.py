from test_framework import generic_test

from math import log10

def is_palindrome_number_comlicated(x: int) -> bool:
    y = 0
    if x < 0 or (x %10 == 0 and x > 0 ) : return False
    while x > y :
        y = y * 10 +  x % 10
        x //= 10
    return x == y or y // 10 == x

def is_palindrome_number(x: int) -> bool:
    y = 0
    n = x
    while n > 0 :
        y *= 10
        y += n % 10
        n //=  10
    return y == x



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number_comlicated  ))
