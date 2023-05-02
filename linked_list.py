# A linkedlist is made up of nodes
# Each node has 2 attributes: data and reference to next node

class Node:
    def __init__(self, data):
        self.data = data  # data being passed in
        self.next = None     # reference to next node

# a linked list has 3 attributes: head points to first node, tail points to end node, size is number of nodes


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # prepend adds a node to the head of the linkedlist
    def prepend(self, data):
        # create a new node to insert within our list
        n = Node(data)
        # check if linkedlist is empty
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            # link new node to old node, link head to new node
            n.next = self.head
            self.head = n
        self.size += 1

    # append adds a node to the tail of the linkedlist
    def append(self, data):
        # create a new node to insert within out list
        n = Node(data)
        # check if linkedlist is empty
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            # create temp to store old node
            temp = self.tail
            # link tail to new node
            self.tail = n
            # link old node's next to tail
            temp.next = self.tail
        self.size += 1

    # print the linked list
    def print_list(self):
        data = ""
        current = self.head
        while current != None:
            data = data + str(current.data) + ""
            current = current.next
        return data

    # remove the first node from linked list, garbage collected once no references
    def remove_first(self):

        # check if list is empty
        if self.size == 0:
            raise("Error. Linked list is empty")
        # check if only one node in list, which means empty list after removal
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.size -= 1

    # remove last node from list, garbage collected once no reference
    def remove_last(self):

        # check if list is empty
        if self.size == 0:
            raise("Error. Linked list is empty")

        # check if only one node in list, which means empty list after removal
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            # do .next down the linkedlist till second last node
            current = self.head
            while current.next.next != None:
                current = current.next

            # set reference of second last node to None
            current.next = None

            # point tail to second last node
            self.tail = current
            self.size -= 1

    def insert_at(self, pos, data):
        if pos < 0 or pos > self.size:
            raise("Error: Invalid position.")
        # insert at front of list
        elif pos == 0:
            self.prepend(data)
        # insert at end of list
        elif pos == self.size:
            self.append(data)
        else:
            # create new node to insert into list
            n = Node(data)
            # prev points to node before current node
            prev = None
            current = self.head
            counter = 0
            # traverse pos = k times starting from self.head to reach node after new node
            while counter < pos:
                prev = current
                current = current.next
                counter += 1
            n.next = current
            prev.next = n
            self.size += 1

    def remove_at(self, pos):
        if pos < 0 or pos > self.size:
            raise("Error: Invalid position.")

        # remove at front of list
        elif pos == 0:
            self.remove_first()

        # remove at end of list
        elif pos == self.size:
            self.remove_last()
        else:
            current = self.head
            counter = 0
            prev = None
            # traverse pos times to reach the node you want to remove
            while counter < pos:
                prev = current
                current = current.next
                counter += 1
            prev.next = current.next
            self.size -= 1


l = Linkedlist()
l.append(2)
print(l.print_list())
l.prepend(1)
print(l.print_list())
l.append(4)
print(l.print_list())
l.insert_at(2, 3)
print(l.print_list())
l.remove_at(2)
print(l.print_list())
