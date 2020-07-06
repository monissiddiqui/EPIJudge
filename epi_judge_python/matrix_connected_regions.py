from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    COLOUR = image[x][y]
    adjacentBlocks = ((-1,0),(0,-1),(1,0),(0,1))
    def dfs(i :int , j :int ) -> None :
        if not ( 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == COLOUR ) :
            return
        image[i][j] = not COLOUR
        for di,dj in adjacentBlocks :
            dfs(i+di,j+dj)
    dfs(x,y)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
