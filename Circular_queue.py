# a regular queue will have wasted memory in the indexes from 0 to head
# they will only be restored when we check head == tail and we reset them back to 0
# in circular queue, we use circular incrementation rather than normal incrementation to find head and tail
# so no wasted memory

class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*k
        self.head = 0
        self.tail = -1  # because we the queue is empty
        self.size = 0

    # inserts element into circular queue
    def enQueue(self, value: int):

        # error message if queue is full
        if self.isFull():
            raise Exception("Circular queue is Full")

        else:
            # circular incrementation
            self.tail = (self.tail + 1) % self.k

            # insert element into circular queue
            self.queue[self.tail] = value

            # increment size
            self.size += 1

            print(self.tail)
            print(self.queue)

    # deletes an element from the circular queue

    def deQueue(self):

        # error message if empty
        if self.isEmpty():
            raise Exception("Circular queue is Empty")
        else:
            # delete element from queue
            self.queue[self.head] = None

            # decrement size
            self.size -= 1

            # circular incrementation
            self.head = (self.head + 1) % self.k

            print(self.queue)

    # returns front item, if empty return -1
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    # returns rear item, if empty return -1

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    # check if empty
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    # check if full
    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
