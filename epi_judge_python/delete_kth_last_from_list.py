from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # if k <= 0 : return None
    dummyHead = ListNode(0,L)
    q = dummyHead
    for _ in range(k) :
        q = q.next
    p = dummyHead
    while q.next :
        q = q.next
        p = p.next
    # res = p.next
    p.next = p.next.next
    # res.next = None
    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
