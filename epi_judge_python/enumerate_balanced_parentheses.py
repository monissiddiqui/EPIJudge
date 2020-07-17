from typing import List

from test_framework import generic_test, test_utils

from collections import deque
from itertools import product

from typing import Set, List, Dict, Deque

def generate_balanced_parentheses_cacheable(num_pairs: int) -> List[str]:

    parensList : Dict[int,Set[str]]= {0:[""]}
    def construct_pairs(n : int) -> Set[str]:
        if n in parensList :
            return parensList[n]
        res = set()
        res.update(["(" + parens + ")" for parens in construct_pairs(n-1)])
        if n % 2 == 0 :
            res.update([a + b for a,b in product(construct_pairs(n//2),repeat=2)])
        i,j = 1, n-1
        while i < j :
            smaller = construct_pairs(i)
            larger = construct_pairs(j)
            res.update([a + b for b in larger for a in smaller])
            res.update([b + a for b in larger for a in smaller])
            i +=1
            j-=1
        parensList[n] = res
        return parensList[n]

    return list(construct_pairs(num_pairs))

def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    res : Deque[str] = deque([])
    parens : Deque[str] = deque([],maxlen=num_pairs*2)
    def construct_parens(n: int, m: int) -> None :
        nonlocal parens
        if len(parens) == num_pairs*2:
            res.append(''.join(parens))
            return
        if n < num_pairs :
            parens.append("(")
            construct_parens(n+1,m)
            parens.pop()
        if n > m :
            parens.append(")")
            construct_parens(n,m+1)
            parens.pop()


    construct_parens(0,0)
    return list(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
