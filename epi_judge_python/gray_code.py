import functools
from typing import List, Deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from epi_judge_python_solutions.gray_code import  differ_by_1_bit

from collections import deque

def gray_code_bu(num_bits: int) -> List[int]:
    if num_bits == 0 : return [0]
    # grayCodeCache : Dict[int,List[int]] = {0:[]}
    def getGrayCode(n: int) -> List[int] :
        if n == 1 : return [0,1]
        MASK = 1 << n-1
        bit = MASK
        res : Deque[int] = deque([],maxlen=2**n)
        for num in getGrayCode(n-1) :
            res.extend([bit | num, bit^ MASK | num])
            bit ^= MASK
        return list(res)
    return getGrayCode(num_bits)

# does not work
def gray_code_td(num_bits: int) -> List[int]:
    if num_bits == 0 : return [0]
    num = 0
    res : Deque[int] = deque([],maxlen=2**num_bits)
    def constructGrayCode(n : int) -> None :
        nonlocal num
        if n == num_bits :
            res.append(num)
            return
        MASK = 1 << n
        constructGrayCode(n+1)
        num ^= MASK
        constructGrayCode(n+1)
    constructGrayCode(0)
    return list(res)




@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code_td, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure('Length mismatch: expected ' + str(expected_size) +
                          ', got ' + str(len(result)))
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure('Two adjacent entries are equal')
            else:
                raise TestFailure(
                    'Two adjacent entries differ by more than 1 bit')

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure('Not all entries are distinct: found ' +
                          str(len(result) - len(uniq)) + ' duplicates')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('gray_code.py', 'gray_code.tsv',
                                       gray_code_wrapper))
