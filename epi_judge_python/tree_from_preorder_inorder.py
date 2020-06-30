from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque
from typing import Optional

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    positionOf  = { k:v for v,k in enumerate(inorder) }
    n = len(inorder)

    def construct_tree(il :int, ir :int, pl :int, pr: int) -> Optional[BinaryTreeNode] :
        if ir < il :
            return None
        root = BinaryTreeNode(preorder[pl])
        if il == ir :
            return  root
        rootPosition = positionOf[preorder[pl]]
        il_l, ir_l = il, rootPosition-1
        pl_l, pr_l = pl+1, (rootPosition - il) + pl
        leftTree = construct_tree(il_l,ir_l,pl_l,pr_l)
        il_r, ir_r = rootPosition +1, ir
        pl_r,pr_r = pr_l +1, pr
        rightTree = construct_tree(il_r,ir_r,pl_r,pr_r)
        root.left, root.right = leftTree, rightTree
        return root

    return construct_tree(0,n-1,0,n-1)





def binary_tree_from_preorder_inorder_iterative(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if len(preorder) == 0 :
        return BinaryTreeNode()
    root = BinaryTreeNode(preorder[0])
    stack = deque([root], maxlen=len(inorder))
    i,p= 0,1
    while p < len(preorder) :
        if preorder[p] != inorder[i] :
            while preorder[p] != inorder[i]  :
                stack[-1].left = BinaryTreeNode[preorder[p]]
                stack.append(stack[-1].left)
                p +=1
        elif preorder[p] == inorder[i] :
            # iterate up call stack to first node with a right node
            curNode = BinaryTreeNode[preorder[p]]
            p += 1
            i += 1
            stack.append((curNode))
            curNode.right = BinaryTreeNode(preorder)

    return BinaryTreeNode()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
