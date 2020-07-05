from test_framework import generic_test

from math import comb

def number_of_ways_efficient(n: int, m: int) -> int:
    return comb(m+n-2,m-1)

def number_of_ways(n: int, m: int) -> int:
    k = min(m,n)
    t = [1] * k
    for _ in range(1,max(m,n)) :
        for j in range(1,k) :
            t[j] += t[j-1]
    return t[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
