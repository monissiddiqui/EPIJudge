from typing import Optional
from doubly_list_node import DoublyListNode

"""
Similar to the original problem, but when adding the next element to the mergedNodes curent tail
the added element's previous value should equal to curr, then curr is updated after
"""
def merge_two_sorted_lists(L1, L2 : Optional[DoublyListNode]) -> Optional[DoublyListNode] :

    dumy_head = DoublyListNode()
    return dumy_head.next