import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:

    def iterate_k_nodes(node: ListNode, k: int) -> ListNode :
        for _ in range(k):
            node = node.next
        return node


    dummyHead = ListNode(0,head)
    # find a node in the cylce
    slow,fast = dummyHead, head
    while fast and fast.next and slow.data != fast.data:
        fast = fast.next.next
        slow = slow.next

    if not fast or slow.data != fast.data:
        return None

    # find the cycle length
    ptr = slow.next
    cycleLen = 1
    while ptr.data != slow.data :
        cycleLen += 1
        ptr = ptr.next

    #iterate from head k at a time to reach a point in the cycle
    prevNode = head
    nextNode = iterate_k_nodes(prevNode,cycleLen)
    if prevNode.data == nextNode.data :
        return prevNode
    while True :
        nextNextNode = iterate_k_nodes(nextNode,cycleLen)
        if nextNextNode.data == nextNode.data :
            break
        prevNode = nextNode
        nextNode = nextNextNode

    # Let n be index of beginning of cycle. prevNode and nextNode
    # should both be preciseley n % cycleLen nodes behind the start
    # of the cycle
    for _ in range(cycleLen) :
        prevNode = prevNode.next
        nextNode = nextNode.next
        if prevNode.data == nextNode.data :
            return prevNode
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
