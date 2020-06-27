from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity  = capacity
        self.queue = [0]*self.capacity
        self._size = 0
        self.head = 0
        self.tail = -1
        return

    def enqueue(self, x: int) -> None:
        if self._size == self.capacity :
            newQueue = [0] * self.capacity*2
            for i in range(self.capacity) :
                newQueue[i] = self.queue[self.head]
                self.head = (self.head +1) % self.capacity
            self.head, self.tail = 0,self.capacity-1
            self.capacity *= 2
            self.queue = newQueue

        self.tail = (self.tail +1) % self.capacity
        self.queue[self.tail] = x
        self._size += 1

    def dequeue(self) -> int:
        x = self.queue[self.head]
        self._size -= 1
        self.head = (self.head +1) % self.capacity
        return x

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
