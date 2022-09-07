class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"[value: {self.value} next: {self.next}]"


class LinkedList(object):
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head  # initially, tail and head points to the same memory location.
        self.length = 1

    def __str__(self):
        return f"head: {self.head} \ntail: {self.tail} \nlength: {self.length}"

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.prepend(2)
print(my_linked_list)