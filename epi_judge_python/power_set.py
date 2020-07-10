from typing import List

from test_framework import generic_test, test_utils

from collections import deque
from math import log2

def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # if len(input_set) == 0 : return [[]]
    powerSet = deque([],maxlen=2**len(input_set))
    set = deque([],maxlen=len(input_set))
    def addToSet(i: int ) -> None :
        if i == len(input_set) :
            powerSet.append(list(set))
            return
        addToSet(i+1)
        set.append(input_set[i])
        addToSet(i+1)
        set.pop()
    addToSet(0)
    return list(powerSet)

def generate_power_set_nonrecursive(input_set: List[int]) -> List[List[int]]:
    powerSet = deque([],maxlen=2**len(input_set))
    for n in range(2**len(input_set)) :
        res = deque([],maxlen= len(input_set))
        while n >  0  :
            i = int(log2(n & ~(n-1)))
            n &= n-1
            res.append(input_set[i])
        powerSet.append(list(res))
    return list(powerSet)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set_nonrecursive,
                                       test_utils.unordered_compare))
