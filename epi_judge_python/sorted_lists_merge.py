from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Solution 1 merging the list piece by piece. 
"""
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    curr = head
    while L1 and L2 :

        if L1.data < L2.data :
            curr.next = L1
            curr = L1
            L1 = L1.next
        else :
            curr.next = L2
            curr = L2
            L2 = L2.next

    if L1 :
       curr.next = L1
    elif L2:
       curr.next = L2

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
