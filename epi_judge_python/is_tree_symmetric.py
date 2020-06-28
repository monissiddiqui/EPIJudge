from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from typing import Optional

def is_symmetric(tree: BinaryTreeNode) -> bool:
    def mirrorTraversal(ltree: Optional[BinaryTreeNode], rtree : Optional[BinaryTreeNode]) -> bool :
        if ltree is None and rtree is None : return True
        if not ltree or not rtree : return False
        if  ltree.data ==  rtree.data and \
            mirrorTraversal(ltree.right,rtree.left) and \
            mirrorTraversal(ltree.left,rtree.right) :
                return True
        return False

    return not tree or mirrorTraversal(tree.left,tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
