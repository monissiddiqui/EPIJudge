from test_framework import generic_test

from collections import deque

def is_well_formed(s: str) -> bool:
    stack = deque([],maxlen=len(s))
    # openSymbols = set('{[(')
    matchingOpenSymbolOf = {'}':'{',']':'[',')':'('}

    for c in s :
        if c not in matchingOpenSymbolOf :
            stack.append(c)
        elif len(stack) == 0 :
            return False
        else :
            if matchingOpenSymbolOf[c] != stack.pop() :
                return False
    return len(stack) == 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
