from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    def searchSubMatrix(l:int,r:int,b:int,t:int) -> bool :
        if l > r or b > t : return False
        j = (l+r)//2
        i = (b+t)//2
        if A[i][j] == x :
            return True
        elif l==r and b==t :
            return False
        elif A[i][j] > x :
            if searchSubMatrix(l, r, b, i-1) or searchSubMatrix(l,j-1,i,t) :
                return True
        else :
            if searchSubMatrix(l,r,i+1,t) or searchSubMatrix(j+1,r,b,i) :
                return True
        return False

    return searchSubMatrix(0,len(A[0])-1,0,len(A)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
