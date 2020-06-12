from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummyHead = ListNode()
    dummyHead.next = L
    head = dummyHead
    tail =  L
    count = 1
    # get sublist bounds. Head points right before the first element in sublist
    # and tail should point after last element in sublist
    while tail and count <= finish :
        if count < start :
            head = head.next
        tail = tail.next
        count +=1

    curr = head.next
    end = tail
    while curr != tail :
        tmp = curr
        curr = curr.next
        tmp.next = end
        end = tmp
    head.next = end

    return dummyHead.next

def reverse_sublist_one_pass(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummyHead = ListNode(0,L)
    sHead = dummyHead
    for _ in range(1,start) :
        sHead = sHead.next

    '''
    original before first iteration
     ptr -v
    sH -> s - > (s+1) -> ... -> f -> t
    iterate only if f > s
    
    After 1st iteration, before second iteration
          ptr -v   
    sH -v      s -> (s+2) -> ... -> f -> t
        (s+1) -^
        
    After ith iteration, before i+1th iteration
                                     ptr -v
    sH -v                                 s -> (s +i + 1) -> ... -> f
        (s+i) -> (s+i-1) -> ... -> (s+1) -^
    
    
    '''
    ptr = sHead.next
    for _ in range(finish-start) :
        temp = ptr.next
        ptr.next = temp.next
        temp.next = sHead.next
        sHead.next = temp

    return dummyHead.next





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist_one_pass))
