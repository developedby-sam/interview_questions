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

    def insert(self, pos, value):
        # MAKE IT THE LAST ITEM IF INSERT POSITION IS GREATER THAN THE LIST LENGTH
        if pos >= self.length:
            return self.append(value)
        # MAKE IT HEAD IF THE INSERT POSITION IS 0
        if pos == 0:
            return self.prepend(value)
        if pos < 0:
            raise IndexError('Incorrect insert position, list index out of bound!!')
        new_node = Node(value)
        leader = self.traverse_to_index(pos - 1)
        next_holding_pointer = leader.next
        leader.next = new_node
        new_node.next = next_holding_pointer
        self.length += 1

    def remove(self, index):
        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1

    def traverse_to_index(self, index):
        current_pos = 0
        current_node = self.head
        while current_pos != index:
            current_node = current_node.next
            current_pos += 1
        return current_node


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.prepend(2)
my_linked_list.insert(2, 75)
my_linked_list.insert(200, 75)
my_linked_list.insert(0, 750)
print(my_linked_list)
my_linked_list.remove(2)
print(my_linked_list)
