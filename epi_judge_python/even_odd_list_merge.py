from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    dummyHead = ListNode(0,L)
    oddHead = dummyHead
    size = 0
    while oddHead.next :
        size += 1
        oddHead = oddHead.next
    if size < 3 : return L
    i = 0
    ptr = dummyHead
    while i < size :
        if i %2 == 0 :
            ptr = ptr.next
        elif i %2 == 1 :
            odd = ptr.next
            ptr.next = odd.next
            odd.next = None
            oddHead.next = odd
            oddHead = odd
        i += 1
    return dummyHead.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
