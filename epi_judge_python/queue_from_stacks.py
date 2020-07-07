from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

class Queue:

    def __init__(self):
        self.eStack = deque()
        self.dStack = deque()

    def enqueue(self, x: int) -> None:
        # if not self.eStack :
        #     while self.dStack :
        #         self.eStack.append(self.dStack.pop())
        self.eStack.append(x)

    def dequeue(self) -> int:
        if not self.dStack:
            while self.eStack :
                self.dStack.append(self.eStack.pop())
        if self.dStack : return self.dStack.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
