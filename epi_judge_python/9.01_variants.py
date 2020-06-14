import binary_tree_node

'''
Variant: Write a program that returns the size of the largest subtree that is complete.

Variant: Define a node in a binary tree to be k-balanced if the difference in the number of nodes in its left and right 
subtrees is no more than k. Design an algorithm that takes as input a binary tree and positive integer k, and retums a 
node in the binary tree such that the node is not k-balanced, but all of its descendants are k-balanced. For example, 
when applied to the binary tree in Figure 9.1 on Page 112 if k = 3, your algorithm should return Node J.
'''

def largest_complete_subtree_size(tree: binary_tree_node) -> int :
    """
    The definition of a compplete tree is that all the
    :param tree:
    :return:

    This is a post-rder traversal since the node will have to know about the subtree's
    (number of nodes, height, and completeness) the recursive funciton on a node returns as (1,0,True);
    THen the status of each child is gathered. The node is returned as complete in any of
    the following two scenarios where both subtrees are complete:
        1. if left subtree is perfect (n = 2^(h+1)-1) and right subtree height is equal
        2. o/w if right subtree is perfect and left subtree height is one greater
    In either case (l.n + r.n + 1, max(l.h,r.h) +1, true) is returned and maxComplete
    subtree size is updated

    The node's subtree is incomplete in all other cases

    """

def is_tree_k_balanced(tree: binary_tree_node, k:int ) -> binary_tree_node :
    """
    :param tree:
    :return:

    Do a postorder traversal where the recursive function returns the number of nodes and if the
    tree is recursively k-balanced. The current tree is recursively k-balanced if BOTH:
     1) left and right subtrees are recursively k-balanced
     2) the difference in number of elements between both trees is at most k

    keep a global vairable for the binary_binary_tree_node to return. assign the binary tree only
    if the current node is not k-balanced. Avoid doign any more searching if an appropriate node has been
    recorded.
    """


if __name__ == '__main__' :
    print("Testing 9.01 Variants")