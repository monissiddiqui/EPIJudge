from typing import List

from test_framework import generic_test

from math import sqrt,isclose

def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    if k == 0 : return []
    SQRT2 = sqrt(2)
    res = [0] * k
    res[0] = 0.0
    m,n = 0,0
    i = 1
    while i < k :
        print(m,n)
        print(res[m] + 1,res[n] + SQRT2 )
        if isclose(res[m] + 1 , res[n] + SQRT2) :
            res[i] = res[m] + 1
            m += 1
            n += 1
        elif res[m] + 1 < res[n] + SQRT2 :
            res[i] = res[m] + 1.0
            m += 1
        elif res[m] +1 > res[n] + SQRT2 :
            res[i] = res[n] + SQRT2
            n += 1

        i += 1
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
