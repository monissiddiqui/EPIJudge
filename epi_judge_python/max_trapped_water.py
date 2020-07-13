from typing import List

from test_framework import generic_test

def get_max_trapped_water_n_squared(heights : List[int]) -> int :
    maxWater = 0
    for i in range(len(heights)) :
        for j in range(i+1, len(heights)) :
            maxWater =  max(maxWater,min(heights[j],heights[i])*(j-i))
    return maxWater


def get_max_trapped_water(heights: List[int]) -> int:
    if len(heights) < 2 : return 0
    i,j = 0, len(heights) -1
    maxWater = 0
    while i < j :
        maxWater = max(maxWater, (j-i)*min(heights[j],heights[i]))
        if heights[i] > heights[j] :
            j -=1
        else :
            i += 1
    return maxWater


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
