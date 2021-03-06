from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque


# def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
#     if not tree : return True
#     if tree.left and tree.left.data > tree.data : return False
#     if tree.right and tree.right.data < tree.data : return False
#
#     prev = float("-inf")
#     def in_order_traversal(node : BinaryTreeNode) -> bool :
#         nonlocal prev
#         if not node : return True
#         if node.left and not in_order_traversal(node.left) :
#             return False
#         if node.data < prev : return False
#         prev = node.data
#         if node.right and not in_order_traversal(node.right) :
#             return False
#         return True
#
#     return in_order_traversal(tree)

# redo question
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    prevVal = float("-inf")
    def in_order(node: BinaryTreeNode) -> bool :
        nonlocal prevVal
        if not node : return True
        is_left_bst =  in_order(node.left)
        if not is_left_bst : return False
        if node.data < prevVal :
            return False
        prevVal = node.data
        return  in_order(node.right)
    return in_order(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
