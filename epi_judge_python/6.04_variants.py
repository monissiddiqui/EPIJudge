"""
VARIANT 1
You have an array C of characters. The characters may be letters, digits,
blanks, and punctuation. The telex-encoding of the array C is an array T
of characters in which letters, digits, and blanks appear as before,
but punctuation marks are spelled out. For example, telex-encoding entails
replacing the character "." by the string "DOT", the character "," by
"COMMA", the character "?" by "QUESTION MARK", and the character "!" by
"EXCLAMATION MARK". Design an algorithm to perform telex-encoding with O(1)
space.

VARIANT 2
Write a program which merges two sorted arrays of integers, A and B. Specifically,
the final result should be a sorted array of length m + n, where n and m are the
lengths of A and B, respectively. Use O(1) additional storage-assume the result is
stored in A, which has sufficient space. These arrays are C-style arrays, i.e.,
contiguous preallocated blocks of memory.
"""

'''
VARIANT 1
'''
def telex_encoding(C : List[str], size: int) -> int :
    '''
    This is similar to 6.004, but we have a map from punctuations to
    their coresponding words. Since all of the replacements in this case
    increase the length of the final string, All of these must be
    done by backwards iteration.

    Now for each punctuation point, p,
    the number of points,n, must be found and then the new size of the
    final word would be len(word) + n*(len(word(p)-1). Then backfill
    from the new endpoint and iterate backwards from the original array end
    while replacing p with word(p) when inserting at the back. While iterating
    through the original indices, count the number of occurences of the
    next punctuation point to tackle so that the new size of the array for
    the next punctuation replacement can be calculated.
    '''

'''
VARIANT 2
'''
def merge_sorted_arrays(A,B: List[int]):
    '''
    This can be easily done by backfilling the array starting at index m+n in A and inserting
    the maximum among the current end pointers of A and B. When an element from A or B is inserted
    it must be inserted accordingly
    '''