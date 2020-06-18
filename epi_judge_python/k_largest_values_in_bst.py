from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

from collections import deque

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    kLargest = deque([],maxlen=k)
    def reverse_in_order(node: BstNode) :
        if not node: return
        reverse_in_order(node.right)
        if len(kLargest) < k :
            kLargest.append(node.data)
        if len(kLargest) < k :
            reverse_in_order(node.left)
        return
    reverse_in_order(tree)
    return list(kLargest)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
