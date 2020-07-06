import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    n = len(items)
    t = [ [0] *n for _ in range(capacity+1) ]
    # first column values are only considering the i=0 item, so any suitable capacity will do
    if n > 0 :
        for w in range(items[0].weight,capacity+1) :
            t[w][0] = items[0].value

    # Now maximum value for any items through i, either i can be added to a maximal set from items through i-1
    # of at most weight (w-items[i].weight) or only items up to i-1 can be considered up to a weight of
    # w. Get max among those two options
    for w in range(1,capacity+1) :
        for i in range(1,n) :
            t[w][i] = t[w][i-1]
            if items[i].weight <= w : t[w][i] = max(t[w][i],t[w-items[i].weight][i-1] + items[i].value)

    return t[-1][-1]

def optimum_subject_to_capacity_column(items: List[Item], capacity: int) -> int:
    n = len(items)
    if n == 0 : return 0
    t = [ items[0].value if w >=items[0].weight else 0 for w in range(capacity+1) ]
    t = [0] * (capacity+1)

    # Now maximum value for any items through i, either i can be added to a maximal set from items through i-1
    # of at most weight (w-items[i].weight) or only items up to i-1 can be considered up to a weight of
    # w. Get max among those two options
    for i in range(n) :
        valuesUpToCurrentItem = t.copy()
        for w in range(capacity+1) :
            addItemValue = (t[w-items[i].weight] + items[i].value) if items[i].weight <= w else 0
            valuesUpToCurrentItem[w] = max(t[w],addItemValue)
        t = valuesUpToCurrentItem

    return t[-1]

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity_column, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
