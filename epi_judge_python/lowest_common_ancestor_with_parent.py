import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


'''
To solve this, we can iterate both nodes in tandem all the way to the parent. 
If the node's meet along the way return the node.
O/W one node will reach the parent before the other and the other node will be Y-X nodes
away from the parent. Once a node reaches the root, increment an offest for that node 
instead of incrementing along it's search path.

Then iterate from both nodes, but hold off on iterating on the node by offset iterations so that
eventually the two nodes meet

                 X
        node0 ->....-v       n
                     lca -> .... -> root
node 1 -> ..........-^
              Y
              
'''
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    a0,a1 = node0, node1
    o0, o1 = 0,0
    while a0 is not a1 and (a0.parent or a1.parent) :
        if not a0.parent :
            o0 +=1
        else :
            a0 = a0.parent
        if not a1.parent:
            o1 += 1
        else :
            a1 = a1.parent
    # return if nodes if counts are 0 since the ancestor pointers met along iteration
    if o0 + o1 == 0:
        return a0
    # o/w iterate with less depth node having offset
    s,l,o = (node0,node1,o0) if o0 else (node1,node0,o1)

    while l is not s :
        if o :
            o -= 1
        else :
           s = s.parent
        l = l.parent
    return l



@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
