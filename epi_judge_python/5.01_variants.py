"""
# Page 42 of EPI.

Assuming that keys take one of three values, reorder the array so that all objects with the same
key appear together. The order of the subarrays is not important. For example, both Figures 5.1(b) and
5.1(c) on Page 40 are valid answers for Figure 5.1(a) on Page 40. Use O(1) additional sPace and o(n)
time.

Given an array A of n objects with keys that takes one of four values, reorder the array so that
all objects that have the same key appear together. Use O(1) additional space and O(n) time.

Given an array A of n objects with Boolean-valued keys, reorder the array so that objects that
have the key false appear first. Use O(1) additional space and O(n) time.

Given em array A of n objects with Boolean-valued keys, reorder the array so that objects that
have the key false appear first. The relative ordering of objects with key true should not change. Use
O(1) additional space and O(n) time.

"""

def partition_by_categories() :
    '''
    use the same underlying algorithm as the dutch national flag problem, but associate the keys to
    integer values via a map
    '''
    return

def partition_four_keys() :
    '''
    This is also the same idea as my Solution 1 for the dutch national flag problem. Keep partitionaing by
    one value on the left subarray, and when the rest of the values are put into the right sub-array,
    perform the partitioning again on the right sub array. We can do this for an arbitrary number of keys
    '''

def partition_by_boolean() :
    '''
    This is just a special case of the above two variations. fill the array by assigning false values to
    the left most available index in the array and the true values to the right-most available value in
    the array.
    :return:
    '''

def partition_by_boolean_preserve_ordering() :
    '''
    Have two incrementers, but instead of starting from the beginning, iterate from the end. This way when
    appending to the end of the array with the True-value keys, the order gets preserved.
    :return:
    '''

if __name__ == '__main__':
    print("Testing 5.01 Variants")

