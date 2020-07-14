from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    lhalf = ListNode(0)
    slow = L
    if not slow : return True
    fast = slow.next
    if not fast: return True

    while fast :
        temp = slow
        slow = slow.next
        lhalf.next, temp.next = temp, lhalf.next
        if fast.next :
            fast = fast.next
            if not fast.next :
                slow = slow.next
            fast = fast.next
        else :
            fast = fast.next

    lhalf= lhalf.next
    while lhalf and slow :
        if lhalf.data != slow.data :
            return False
        lhalf = lhalf.next
        slow = slow.next
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
