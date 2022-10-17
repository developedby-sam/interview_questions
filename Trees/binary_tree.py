class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"[value: {self.value} left: {self.left} right: {self.right}]"

class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def __str__(self):
        return f"root: {self.root}"

    def insert(self, value):
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return self.root

        current_node = self.root
        while True:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    return False
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return False
                current_node = current_node.right

    def lookup(self, value):
        if not self.root:
            return False
        
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return current_node
        return False


binary_tree = BinarySearchTree()
binary_tree.insert(9)
binary_tree.insert(4)
binary_tree.insert(12)
binary_tree.insert(19)
binary_tree.insert(19)
binary_tree.insert(2)
print(binary_tree.lookup(22))