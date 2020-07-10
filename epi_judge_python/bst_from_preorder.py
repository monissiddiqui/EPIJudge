from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

from collections import deque

def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    if len(preorder_sequence) == 0 : return None
    root = BstNode(preorder_sequence[0])
    searchPath = deque([root],maxlen=len(preorder_sequence))
    i = 1
    while i < len(preorder_sequence) :
        if preorder_sequence[i] < preorder_sequence[i-1] :
            node =  BstNode(preorder_sequence[i])
            searchPath[-1].left =  node
            searchPath.append(node)
        else :
            node = searchPath.pop()
            while len(searchPath) and searchPath[-1].data < preorder_sequence[i] :
                node = searchPath.pop()
            right = BstNode(preorder_sequence[i])
            node.right = right
            searchPath.append(right)
        i += 1
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
