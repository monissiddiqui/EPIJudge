from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    res = [0] * (len(num1)+len(num2))
    sign = 1
    if num1[0] <0 :
        num1[0] *= -1
        sign *= -1
    if num2[0] < 0 :
        num2[0] *= -1
        sign *= -1
    for i in range(len(num1)) :
        for j in range(len(num2)) :
            res[~(i+j)] += num1[~i]*num2[~j]
            res[~(i+j+1)] += res[~(i+j)] //10
            res[~(i+j)] %= 10

    i = 0
    while i < len(res) :
        if res[i] != 0 :
            res [i] *= sign
            break
        i += 1
    return res[i:] if i < len(res) else [0]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
