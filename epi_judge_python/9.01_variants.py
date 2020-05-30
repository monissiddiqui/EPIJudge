import binary_tree_node

'''
Variant: Write a program that retums the size of the largest subtree that is complete.

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

    At each node, check if the left and right subtrees are complete and return the size
    return the node as benig complete if one of following occurs:
     1) left subtree is complete and the right subtree is perfect with height one less than left
     2) left subtree is perfect and right subtree is complete with heights the same
    unless both subtrees are perfect, return the current node as perfect and the height being the max
    of the child trees.
    """

def is_tree_k_balanced(tree: binary_tree_node, k:int ) -> binary_tree_node :
    """
    :param tree:
    :return:

    Do a postorder traversal where the recursive function returns the number of nodes and if the
    tree is k-balanced. On the current node, the tree is k-balanced if BOTH:
     1) left and right subtrees are k-balaned
     2) the difference in number of elements between both trees is at most k

    keep a global vairable for the binary_binary_tree_node to return. assign the binary tree only
    if the current node is not k-balanced.

    """


if __name__ == '__main__' :
    print("Testing 9.01 Variants")