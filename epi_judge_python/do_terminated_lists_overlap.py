import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if not (l0 and l1) : return None
    n0, n1 = l0, l1
    o0, o1, = 0,0

    # find intersection point, count extra pointers once end is reached
    while n0 is not n1 and (n0.next or n1.next ) :
        if not n0.next :
            o0 += 1
        else :
            n0 = n0.next
        if not n1.next :
            o1 += 1
        else :
            n1 = n1.next
    # cases where pointer's reached together or didn't meet at all based on offset values
    if o0 + o1 == 0:
        if n0 == n1 :
            return n1
        else :
            return None
    # for list that accumulated offset, delay iterating on that list for o iterations.
    s,l,o = (l0,l1,o0) if o0 >0 else (l1,l0,o1)
    while s is not l :
        if o >0 :
            o -=1
        else :
            s = s.next
        l = l.next
    return s


    return ListNode()


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
