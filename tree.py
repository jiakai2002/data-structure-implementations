# Model each node in the tree as an instance of TreeNode class
# Each node will have 3 attributes : data, children node, parent node

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # to add a child node, we need to set child.parent and self.children attributes
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # print data of entire tree
    def print_tree(self):
        # print formatting to show indentations
        level = self.get_level()
        spaces = " " * 3 * level
        prefix = spaces + "|_ _" if self.parent else ""
        print(prefix + self.data)
        # recursive call on child nodes if they exist
        if self.children:
            for child in self.children:
                child.print_tree()

    # get level of node
    def get_level(self):
        level = 0
        current = self.parent
        while current != None:
            current = current.parent
            level += 1
        return level


def build_product_tree():
    root = TreeNode("Electronics")

    # create laptop and add child
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Razor"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Alienware"))
    laptop.add_child(TreeNode("ASUS"))

    # create smartphone and add child
    smartphone = TreeNode("Smartphone")
    smartphone.add_child(TreeNode("Apple"))
    smartphone.add_child(TreeNode("Samsung"))
    smartphone.add_child(TreeNode("HuaWei"))
    smartphone.add_child(TreeNode("Google Pixel"))

    # add to root's children
    root.add_child(smartphone)
    root.add_child(laptop)

    return root


# so that this script tree.py can be imported as a module without running
if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass
