class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"[value: {self.value} next: {self.next}]"


class Queue:
    # CONSTRUCTOR
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return f"first: {self.first} \nlast: {self.last} \nlength: {self.length}"

    # GET THE TOPMOST ITEM
    def peek(self):
        return self.first

    # ADD ITEM TO THE QUEUE
    def enqueue(self, value):
        new_node = Node(value)

        if not self.length:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

        return self

    def dequeue(self):
        if not self.first:
            return None

        if self.length == 1:
            self.last = None

        holding_pointer = self.first
        self.first = self.first.next
        self.length -= 1

    def isEmpty(self):
        if not self.length:
            return True


my_queue = Queue()
print(my_queue.peek())
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(9)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue)
