from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

from  collections import deque

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree: return []
    res =  deque()
    node = tree
    while node.left :
        node = node.left

    # add node, then get successor :
    while node :
        res.append(node.data)

        # get successor with parent references
        if node.right :
            # get left-most of right subtree
            node = node.right
            while node.left :
                node = node.left
        else :
            while node.parent and node.parent.right is node :
                node = node.parent
            node = node.parent if node.parent else None

    return list(res)

def inorder_traversal_redo(tree: BinaryTreeNode) -> List[int]:
    if not tree : return []
    first = tree
    while first.left :
        first = first.left

    inOrderList = deque()
    node = first
    while node :
        inOrderList.append(node.data)
        if node.right :
            node = node.right
            while node.left :
                node = node.left
        else :
            while node.parent and node.parent.right is node :
                node = node.parent
            node = node.parent
    return list(inOrderList)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
