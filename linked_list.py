class LinkedList(object):
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head  # initially, tail and head points to the same memory location.
        self.length = 1

    def __str__(self):
        return f"head: {self.head} \ntail: {self.tail} \nlength: {self.length}"

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = {
            "value": value,
            "next": self.head
        }
        self.head = new_node
        self.length += 1


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.prepend(2)
print(my_linked_list)