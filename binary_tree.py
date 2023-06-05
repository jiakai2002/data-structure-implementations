class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    # to add a child node, we
    def add_child(self, data):

        # no duplicates allowed
        if data == self.data:
            return

        elif data > self.data:
            # recursive call to right subtree
            if self.right:
                self.right.add_child(data)
            # add data to right subtree
            else:
                self.right = BinarySearchTreeNode(data)

        else:
            # recursive call to left subtree
            if self.left:
                self.left.add_child(data)
            # add data to left subtree
            else:
                self.left = BinarySearchTreeNode(data)

    # return a list of elements in binary tree in order
    # left subtree -> root -> right subtree
    def in_order_traversal(self):
        elements = []

        # recurisve call to left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # terminal condition met, append data then traverse right subtree recursively
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # return a list of elements in binary tree in pre-order
    # root -> left subtree -> right subtree
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        # recurisve call to left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # terminal condition met, travese right first then append data
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # return a list of elements in binary tree in post-order
    # left subtree -> right subtree -> root

    def post_order_traversal(self):
        elements = []

        # recurisve call to left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # terminal condition met, travese right first then append data
        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        # found value
        if self.data == val:
            return True
        # search right subtree
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            # right subtree empty
            else:
                return False
        # search left subtree
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            # left subtree empty
            else:
                return False

    def find_min(self):
        min = self.data
        if self.left:
            return self.left.find_min()
        else:
            return min

    def find_max(self):
        max = self.data
        if self.right:
            return self.right.find_max()
        else:
            return max

    def find_sum(self):
        sum = 0
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        else:
            sum += self.data
        return sum


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in elements:
        root.add_child(i)
    return root


if __name__ == "__main__":
    numbers = [15, 12, 7, 14, 20, 23, 27, 88]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.search(12))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.find_sum())
    print(numbers_tree.search(7))
