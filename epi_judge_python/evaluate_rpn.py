from test_framework import generic_test

from collections import deque
from typing import Deque, Callable
from operator import add, floordiv, mul, sub

def evaluate(expression: str) -> int:
    stack : Deque[int]  =  deque([],maxlen=len(expression))
    functionOfOperator : Callable = {'+':add, '*':mul, '-':sub , '/':floordiv}
    for s in expression.split(',') :
        if s in functionOfOperator :
            r = stack.pop()
            l = stack.pop()
            stack.append(functionOfOperator[s](l,r))
        else :
            stack.append(int(s))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
