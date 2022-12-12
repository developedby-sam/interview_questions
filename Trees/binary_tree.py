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

    def breadth_first_search(self):
        current_node = self.root
        output = []
        queue = []

        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            output.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return output

    def breadth_first_search_R(self, queue, output):
        if not len(queue):
            return output

        current_node = queue.pop(0)
        output.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_R(queue, output)

    


binary_tree = BinarySearchTree()
binary_tree.insert(9)
binary_tree.insert(4)
binary_tree.insert(12)
binary_tree.insert(19)
binary_tree.insert(19)
binary_tree.insert(2)
# print(binary_tree)
print(binary_tree.breadth_first_search())
print(binary_tree.breadth_first_search_R([binary_tree.root], []))