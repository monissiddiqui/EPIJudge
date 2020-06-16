'''
EPI(p.154)

VARIANT 1
Design an algorithm for finding the median of an array

VARIANT 2
Design an algorithm for finding the kth largest element of A in the presence of duplicates.
The kth largest element is defined to be A[k - 1] after A has been sorted in a stable manner,
i.e., if A[i] = A[j] and i < j then A[i] must appear before A[j]) after stable sorting.

VARIANT 3
A number of apartment buildings are coming up on a new street. The postal service wants to place
a single mailbox on the street. Their objective is to minimize the total distance that residents
have to walk to collect their mail each day. (Different buildings may have different numbers of
residents.)
Devise an algorithm that computes where to place the mailbox so as to minimize the total distance,
that residents travel to get to the mailbox. Assume the input is specified as an array of building
objects, where each building object has a field indicating the number of residents in that building,
and a field indicating the building's distance from the start of the street.
'''

# Variant 1
def median_of_array() :
    '''
    IF the length of the array is odd, return the N//2th largest element
    If the length of the array is even, return the mean of the N//2 and N//2-th
    largest elements.
    '''

# Variant 2
def kth_largest_with_duplictes() :
    '''
    This is similar to the 11.08, but when doing the partitioning step the faithfulness
    of the elements equal to the pivot needs to be maintained. This is not a big deal
    because if we jsut keep track of the final index of the original pivot variable
    that was used and continue to partitition the left side by le elements, then
    the kth largest element is the pivot variable after paritioning and the end of the left
    partition is at n-k.

    Do similar recursions on the left and right subarrays whenenver the upper index of the left
    partition is less than the
    '''

# Variant 3
def 