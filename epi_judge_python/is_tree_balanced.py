from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    # return the height of the sub-tree, o/w -1 if un balanced
    def getHeightIfBalanced(node: BinaryTreeNode) -> int :
        if not node.left and not node.right :
            return 0

        lHeight = getHeightIfBalanced(node.left) if node.left else -1
        rHeight = getHeightIfBalanced(node.right) if node.right else -1
        if lHeight == -2 or rHeight == -2 :
            return -2

        return 1 + max(lHeight,rHeight) if abs(lHeight-rHeight) <= 1 else -2

    return getHeightIfBalanced(tree) >= 0 if tree else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
