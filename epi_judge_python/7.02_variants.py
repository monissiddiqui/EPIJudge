'''
EPI 7.02 Variants (p.85)

VARIANT 1
Write a function that reverses a singly linked list. The function should use
no more than constant storage beyond that needed for the list itself. The
desired transformation is illustrated in Figure 7.5 on the next page.

VARIANT 2
Write a program which takes as input a singly linked list L and a
nonnegative integer k, and reverses the list k nodes at a time.
If the number of nodes n in the list is not a multiple of k, leave the last
n mod k nodes unchanged. Do not change the data stored within a node.
'''


'''
VARIANT 1
This is simple. have a dummy node pointing to the head. Have a reference to 
tail, initially None. Then iterate while dummyHead.next not None and 
setting dummyHead.next = dummyHead.next.next and dummyHead.next.next = tail 
and tail = dummyHead.next 
'''
def reverse_linked_list() :
    return 0

'''
VARIANT 2

go through a while loop, while the next kth element is not null. Initialize
that value to the tail after the kth element.

if the while loop subTail is initialized to the first element and there is a second loop going from the current pointer 
and curr.next = subTail, and curr is iterated while curr is not the tail
'''
def reverse_groups_of_k():
    return 0