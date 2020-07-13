from typing import List

from test_framework import generic_test

from itertools import product

def fill_surrounded_regions(board: List[List[str]]) -> None:
    BLACK = "B"
    WHITE = "W"
    NOT_ENCLOSED = "N"
    adjacentVertices = ((-1,0),(0,-1),(1,0),(0,1))

    def markEnclosed(x: int, y :int) -> None :
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == WHITE :
            board[x][y] = NOT_ENCLOSED
            for dx,dy in adjacentVertices :
                markEnclosed(x+dx,y+dy)
        return

    # mark white regions connected to top and bottom boundaries as not enclosed
    for i in range(len(board[0])) :
        markEnclosed(0,i)
        markEnclosed(len(board)-1,i)
    # same for right and left boundaries
    for i in range(len(board)) :
        markEnclosed(i,0)
        markEnclosed(i,len(board[0])-1)

    # iterate through all pieces, marking white pieces as black and non-enclosed pieces as white
    # board[:] = [[BLACK if v != NOT_ENCLOSED else WHITE for v in row] for row in board]
    transformVertex = {BLACK: BLACK, WHITE : BLACK, NOT_ENCLOSED: WHITE}
    for x,y in product(range(len(board)), range(len(board[0]))) :
        board[x][y] = transformVertex[board[x][y]]
    return




def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
