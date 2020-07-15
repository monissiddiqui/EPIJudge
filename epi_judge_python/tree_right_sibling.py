import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque

class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling_extra_space(tree: BinaryTreeNode) -> None:
    if tree is None : return None
    bfsQ = deque([tree])
    while bfsQ :
        siblen = 2 *len(bfsQ)
        prev = bfsQ.popleft()
        isDeepest = prev.left is None
        sibQ = deque([],maxlen=0 if isDeepest else siblen)
        while prev :
            if not isDeepest :
                sibQ.append(prev.left)
                sibQ.append(prev.right)
            prev.next = bfsQ.popleft() if bfsQ else None
            prev = prev.next
        bfsQ=sibQ
    return

def construct_right_sibling(tree: BinaryTreeNode) -> None:

    def setNextForSiblings(node) :
        if not (node and node.left) : return
        while node :
            node.left.next = node.right
            if node.next :
                node.right.next = node.next.left
            node = node.next

    while(tree) :
        setNextForSiblings(tree)
        tree = tree.left


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
