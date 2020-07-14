import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from typing import Optional
from collections import deque

def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    i = 0
    def construct_tree() -> Optional[BinaryTreeNode] :
        nonlocal i
        if i == len(preorder) : return None
        i += 1
        if preorder[i-1] is None :
            return None
        return BinaryTreeNode(preorder[i-1], construct_tree(),construct_tree())
    return construct_tree()

def reconstruct_preorder_iterative(preorder: List[int]) -> BinaryTreeNode:
    goLeft = True
    if len(preorder) == 0 : return None
    root = BinaryTreeNode(preorder[0]) if preorder[0] is not None else None
    stack = deque([root],maxlen=len(preorder))
    i = 1
    while i < len(preorder) :
        if preorder[i] is None :
            if goLeft :
                goLeft = False
            else :
                node = stack.pop()
                while stack and node is stack[-1].right :
                    node = stack.pop()
        else :
            if goLeft :
                stack[-1].left = BinaryTreeNode(preorder[i])
                stack.append(stack[-1].left)
            else :
                stack[-1].right = BinaryTreeNode(preorder[i])
                stack.append(stack[-1].right)
                goLeft = True

        i += 1
    return root

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder_iterative, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
