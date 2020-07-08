from test_framework import generic_test

import math

def square_root(x: float) -> float:
    if x == 1 or x == 0 : return x
    l = 1 if x >= 1 else x
    u = x if x >= 1 else 1
    while not math.isclose(l,u) :
        # print(l,m,u,m**2)
        m = (l+u)/2
        if m**2 < x :
            l = m
        else :
            u = m
    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
