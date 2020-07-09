from typing import List

from test_framework import generic_test

import math
def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:

    S = 0
    T = target_payroll
    cap = 0
    p = 0
    n = len(current_salaries)
    count = 0
    while not math.isclose(S,T) :
        count+= 1
        r = n-p
        if r == 0 : return -1
        diff = abs(T-S) /r
        if S < T :
            # cap += diff
            j = p
            while j < n :
                if current_salaries[j] < cap + diff :
                    current_salaries[p] , current_salaries[j] = current_salaries[j], current_salaries[p]
                    S += current_salaries[p] - cap
                    p += 1
                else :
                    S += diff
                j += 1
            cap += diff
        else :
            # cap -= diff
            S -= r * diff
            j = p-1
            while j >= 0 :
                if current_salaries[j] >= cap - diff :
                    p -=1
                    current_salaries[j], current_salaries[p] = current_salaries[p], current_salaries[j]
                    S += cap -diff + current_salaries[p]
                j -= 1
            cap -= diff
    return cap


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
