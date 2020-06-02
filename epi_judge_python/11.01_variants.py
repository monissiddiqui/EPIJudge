from typing import List

'''
11.01 Variants EPI p. 146

1
Design an efficient algorithm that takes a sorted array and a key,
and finds the index of the first occurrence of an element greater than 
that key. For example, when applied to the array in Figure 11.1 on the 
preceding page your algorithm should return 9 if the key is 285; 
if it is -13, your algorithm should return 1

2.
Let A be an unsorted array of n integers, with A[0] >= A[1] and 
A[n - 2] =< A[n - 1]. Call an index I a local minimum if A[i] is 
less than or equal to its neighbors. How would you efficiently find a 
local minimum, if one exists?

3. 
Write a program which takes a sorted array A of integers, and an integer k, 
and returns the interval enclosing k, i.e., the pair of integers L and U 
such that L is the first occurrence of k in A and U is the last occurrence 
of k in A. If k does not appear in A, return [-1, -1]. 

For example if 1= (7,2,2,4,4,4,7,11,'1.1.,13) and k = 77, 
you should retum [7,8].

4. 
Write a program which tests if p is a prefix of a string in an array 
of sorted strings.
'''

def search_first_greater_than_k(A: List[int], k : int) -> int :
    '''
    VARIANT 1
    This is going to be a similar approach as the search_first_of_k
    problem in 11.01. The difference here is that we have to return
    the right bisect instead of the left isect index.

    So when the middle element is k, we want to get the last one that
    occurs, which means that the new array to search will be setting
    L = M. so setting the lower bound of the array to be the middle
    including the middle. Then when the index for k is retrieved
    if the final index isn't k, return it, otherwise return the
    next index if it is less than the length
    '''

def local_minimum_in_valley_array() :
    '''
    VARIANT 2
    The input array, A, has special characteristics where the first elements
    is greater than the second and the second last is less than the last
    element, hence the valley shape of the array.

    Since A[0] >= A[1], and A[n-2] <= A[n-1], we see that there must be
    a point somewhere in the middle of the array that is <= both elements
    it is adjacent to.

    The intuition is that after we select a partition point, whichever
    adjacent element is less than the middle, that side must contain
    the local minimum. This is because the other end of the subarray will
    mirror the same relation, i.e the element on the outside is g.e the
    element on the inside.

    Take the element in the middle, m,:
        if the left side is less than the m, then resume on the left subarray
        if the right side is less than m, then resume on the right subarray
        otherwise m must be a local minimum

    once the lower and upper bound converge, element must be a local minimum.

    :return:
    '''

def search_interval_conatining_k(A :List[int], k: int) -> (int,int) :
    """
    VARIANT 3
    This can be done in O (n). First do search_first_of_k to get the first
    index. if it doesn't exist, return -1. Then do another pass that is
    similar to search_first_greater_than_k but pass the index of the last
    occurrance of k instead.
    """

def is_p_a_prefix_in_array(A: List[str], p: str ) -> bool :
    '''
    Variant 4

    Simple binary search with deault string comparisons except that equality
    is p in s instead of p
    :param A:
    :param p:
    :return:
    '''

if __name__ == '__main__':
    print("TESTING 11.01 variants")
