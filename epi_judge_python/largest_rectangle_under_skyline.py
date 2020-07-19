from typing import List, Deque, Tuple

from test_framework import generic_test

from collections import deque

def calculate_largest_rectangle(heights: List[int]) -> int:
    incrQ : Deque[int]= deque([],maxlen=len(heights))
    maxArea = 0
    for i in range(len(heights) +1 ) :
        val = 0 if i == len(heights) else heights[i]
        while  incrQ and  heights[incrQ[-1]] >= val:
            pillar = incrQ.pop()
            if heights[pillar] != val :
                l = incrQ[-1] if incrQ else -1
                maxArea = max(maxArea, heights[pillar]*(i-l-1))

        if i < len(heights):
            incrQ.append(i)
    return maxArea


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
