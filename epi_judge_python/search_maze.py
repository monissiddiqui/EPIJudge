import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import deque

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

'''
Use DFS to iterate through maze and find the exit, marking visited nodes as 
we go along. Visited nodes can be marked in place for the most optimal 
space complexity. 
'''
def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    exitPath = deque()
    N = len(maze[0])
    M = len(maze)
    def neighboursOf(node: Coordinate) :
        if node.x +1 < M and maze[node.x+1][node.y] == WHITE: yield Coordinate(node.x+1,node.y)
        if node.y -1 >= 0 and maze[node.x][node.y-1] == WHITE: yield Coordinate(node.x,node.y-1)
        if node.x -1 >= 0 and maze[node.x-1][node.y] == WHITE: yield Coordinate(node.x-1,node.y)
        if node.y+1 < N and maze[node.x][node.y+1] == WHITE: yield Coordinate(node.x,node.y+1)

    def isOnExitPath(node : Coordinate) -> bool :
        maze[node.x][node.y] = BLACK # simulate marking as visited
        if node == e :
            exitPath.appendleft(node)
            return True
        for neighbour in neighboursOf(node) :
            if isOnExitPath(neighbour) :
                exitPath.appendleft(node)
                return True
        return False

    isOnExitPath(s)
    return list(exitPath)


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
