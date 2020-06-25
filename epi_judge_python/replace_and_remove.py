import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

'''
iterate through the array and have the index be less thanthe size. 
whenever an a is encountered, then s[i:size+1] = ["d"]*2 + s[i+1:size]  
and the size increases by one and the index is incrmented by 2

whenever b is encountered, s[i:size-1] = s[i+1:size] and size is decremented

The above method would be O(N^2) complexity for time. One way to improve is
to go through a first pass and find the number of a's and b's and then 
find the resultant size of the output array. Then fill the resultant
array while iterating from the original array backwards.

Whenever an a is encountered, the end is filled with two d's 
whenever a b is encountered, the original array index is decremented
whenever any other element is encountered, it is inserted into the end
'''
# def replace_and_remove(size: int, s: List[str]) -> int:
#     # shift all characters to the left after deletions accounted
#     newSize = size
#     i = 0
#     for j in range(size):
#         if s[j] == 'a':
#             newSize += 1
#             s[i] = s[j]
#             i += 1
#         elif s[j] == 'b':
#             newSize -= 1
#         else :
#             s[i] = s[j]
#             i += 1
#     # shift all characters to the end to account for replacements and new size.
#     size = i
#     i,j = size-1, newSize -1
#     while i >= 0 :
#         if s[i] == "a" :
#             s[j-1:j+1] = ["d"] *2
#             j -=2
#             i -=1
#         else:
#             s[j] = s[i]
#             i -=1
#             j -=1
#     return newSize

# redo 6.4
def replace_and_remove(size: int, s: List[str]) -> int:
    aCount = 0
    i=0
    j = 0
    while j < size :

        if s[j] == 'a' :
            aCount += 1
        if s[j] != 'b' :
            s[i] = s[j]
            i += 1
        j += 1
    newSize = i + aCount
    j = newSize -1
    i = i-1
    while i < j :
        if s[i] == 'a' :
            s[j] = 'd'
            s[j-1] = 'd'
            j -=1
        else :
            s[j] = s[i]
        i -= 1
        j -= 1
    return newSize



@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
