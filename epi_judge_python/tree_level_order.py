from typing import List
from typing import Deque
from typing import Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from  collections import deque


'''
Do BFS on the nodes and record the depth along with the node reference when storing into the bfs node 
When the next depth value is encountered in the array, then make the new array 
'''
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree : return []
    bfsQueue : Deque[Tuple[BinaryTreeNode,int]] = deque()
    res = deque([deque()])
    currentDepth = 0
    bfsQueue.append((tree,0))
    while bfsQueue :
        node = bfsQueue.popleft()
        if not node[0] : continue

        if node[1] != currentDepth :
            currentDepth = node[1]
            res.append(deque())
        bfsQueue.append((node[0].left,node[1]+1))
        bfsQueue.append((node[0].right,node[1]+1))
        res[-1].append(node[0].data)
    return [list(q) for q in res]

def binary_tree_depth_order_pythonic(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree: return []
    depthListQ : Deque[List[int]]= deque()
    bfsQ : List[BinaryTreeNode] = [tree]
    def childrenOf(node: BinaryTreeNode) -> List[BinaryTreeNode] :
        return

    while bfsQ :
        depthListQ.append([node.data for node in bfsQ])
        bfsQ = [child
                for node in bfsQ
                    for child in [node.left,node.right] if child
                ]
    return list(depthListQ)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order_pythonic))
