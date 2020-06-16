from test_framework import generic_test


def square_root(k: int) -> int:
    if k <= 1: return k
    l,u= 0, k//2
    m = 0
    while l <= u and m**2 != k:
        m = (l+u)//2
        if m**2 < k :
            l = m+1
        elif m**2 > k :
            u = m-1
    return m if m**2 <= k else m-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
