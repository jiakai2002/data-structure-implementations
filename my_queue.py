# Queue follow FIFO principle, first element that comes goes out first
# we use deque to implement queues as pop or append from both ends of a deque is fast T=O(1)

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self):
        self.buffer.appendleft()

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


# an alternative is to use list as queue
# while append and pop at end of list are fast
# insert or pop at beginning of list is slow because all of the other elements need to be shifted once T=O(n)
queue = [2, 3]

# enqueue
queue.insert(0, 1)

# dequeue
queue.pop()
