from typing import List

from test_framework import generic_test

from collections import deque

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    M = len(square_matrix)
    if M == 0:
        return []
    N = len(square_matrix[0])

    arr = deque(maxlen=M*N)
    k = min((M+1)//2,(N+1)//2)
    for i in range(k) :
        # top of layer i
        arr.extend(square_matrix[i][i:N-i])
        # right side of layer i
        sideRows = range(i+1,M-i)
        for j in sideRows:
            arr.append(square_matrix[j][~i])

    # bottom Row if separate from top, inserted in reverse
        if (M-i) != i :
            arr.extend(square_matrix[~i][N-1-i-1:i:-1])

    # left row if seperate from right, inserted in reverse
        if (N-i) != i:
            for j in reversed(sideRows):
                arr.append(square_matrix[j][i])

    return list(arr)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
