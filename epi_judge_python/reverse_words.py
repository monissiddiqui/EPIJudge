import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # reverse entire string
    for i in range(len(s)//2) :
        s[i],s[~i] = s[~i],s[i]

    # now reverse the individual words to get their correct order.
    i,k = 0,0
    while k < len(s) :
        # find end of first word
        while k< len(s) and s[k].isalnum() :
            k += 1
        # swap characters in word to get in correct order
        j = k-1
        while i < j :
            s[i], s[j] = s[j], s[i]
            i += 1
            j -=1
        # find beginning of next word
        i = k
        while i < len(s) and not s[i].isalnum() :
            i += 1
        k = i
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
