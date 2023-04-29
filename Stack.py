# We will implement stack with list
# Stack follows a LIFO principle. The first element inserted is the first to get removed.

class Stack:
    def __init__(self, k):
        self.k = k
        self.storage = []

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is Full")
        else:
            self.storage.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def isEmpty(self):
        if len(self.storage) == 0:
            return True
        return False

    def isFull(self):
        if len(self.storage) == self.k:
            return True
        return False
