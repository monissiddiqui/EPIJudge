import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))

from collections import Counter

def group_by_age_no_space(people: List[Person]) -> None:
    i,j = 0,0
    while i < len(people) :
        pivot = people[i].age
        i += 1
        j=i
        while j < len(people) :
            if people[j].age == pivot :
                people[i], people[j] = people[j], people[i]
                i += 1
            j += 1
    return

def group_by_age_buckets(people: List[Person]) -> None:
    ageCounts = Counter([person.age for person in people])
    ageBucket = {}
    offset = 0
    for age in ageCounts :
        ageBucket[age] = offset
        offset += ageCounts[age]

    for person in people[:] :
        age = person.age
        people[ageBucket[age]] = person
        ageBucket[age] += 1
        # if ageBucket[age]['index'] == ageBucket[age]['end'] :
    return people

def group_by_age(people: List[Person]) -> None:
    ageCounts = Counter([person.age for person in people])
    ageBucket, index =  {}, 0
    for age in ageCounts :
        ageBucket[age] = index
        index += ageCounts[age]

    while ageBucket :
        from_age = next(iter(ageBucket))
        from_idx = ageBucket[from_age]
        to_age = people[from_idx].age
        to_idx = ageBucket[to_age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        ageCounts[to_age] -= 1
        ageBucket[to_age] += 1
        if ageCounts[to_age] == 0 :
            del ageBucket[to_age]
    return people


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
