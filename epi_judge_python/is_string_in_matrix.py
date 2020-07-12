from typing import List

from test_framework import generic_test

from itertools import product

def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    if not pattern : return True

    m = len(grid)
    n = len(grid[0])
    directions = ((-1,0),(0,-1),(1,0),(0,1))

    def searchForElement(x,y,i) -> bool :
        if i == len(pattern) : return True
        if (x,y,i) in previousAttempts: return False
        previousAttempts.add((x,y,i))
        for dx,dy in directions:
            if 0<= x+dx < m and 0 <= y+dy < n and \
            pattern[i] == grid[x+dx][y+dy] and searchForElement(x+dx,y+dy,i+1) :
                return True
        return False

    previousAttempts = set()

    for x,y in product(range(m),range(n)) :
        if grid[x][y] == pattern[0] and searchForElement(x,y,1) :
            return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
